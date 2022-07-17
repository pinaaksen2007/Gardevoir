# Gardevoir PokeBot
# Copyright (C) 2022 KuuhakuTeam
#
# This file is a part of < https://github.com/KuuhakuTeam/Gardevoir/ >
# PLease read the GNU v3.0 License Agreement in 
# <https://www.github.com/KuuhakuTeam/Gardevoir/blob/master/LICENSE/>


import os
import random
import asyncio

from wget import download
from PIL import Image

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import ChatIdInvalid, ChannelInvalid, ChatWriteForbidden

from gardevoir import ralts, Config, trg
from gardevoir.helpers import get_response, db, is_dev, is_shiny


BASE_NORMAL = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"
BASE_SHINY = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/"
BASE_API = "https://pokeapi.co/api/v2/pokemon/"


CATCH = db("TEMP_CATCH")
GROUPS = db("GROUPS")

@ralts.on_message(filters.command("spawn", ))
async def sp(_, m: Message):
    if not is_dev(m.from_user.id):
        return
    await m.reply("<i>Starting spawn pokemons..</i>")
    while True:
        await spawn_()
        await asyncio.sleep(3600)


async def spawn_():
    dex_id = random.choice(range(0,898))
    data = await get_response.json(link=f"{BASE_API}{dex_id}")
    shiny  = False
    name = data["name"]
    exp = data["base_experience"]
    if (data["sprites"]["front_shiny"]) != None:
        shiny = is_shiny()
    poke_spawn = {
        "$set": {
            "id": dex_id,
            "pokemon": name,
            "exp": exp,
            "shiny": shiny
            }
        }
    image = await draw_catching(dex_id, shiny)
    glist = GROUPS.find()
    async for chats in glist:
        if chats == None:
            return
        else:
            try:
                await CATCH.update_one({"chat_id": chats["chat_id"]}, poke_spawn, upsert=True)
                await asyncio.sleep(1)
                await ralts.send_photo(chat_id=chats["chat_id"], photo=image)
            except ChatIdInvalid:
                pass
            except ChatWriteForbidden:
                pass
            except ChannelInvalid:
                pass
    os.remove(image)


async def draw_catching(dex_id: int, shiny: bool):
    """ draw sprite """
    filename = f"{dex_id}.png"
    img = Image.open("gardevoir/resources/template_catch.png")
    if shiny:
        spr_ = download(BASE_SHINY + filename, Config.DOWN_PATH)
    else:
        spr_ = download(BASE_NORMAL + filename, Config.DOWN_PATH)
    try:
        spr_convert = Image.open(spr_).convert("RGBA")
        img.paste(spr_convert, (155, 2), spr_convert)
        os.remove(spr_)
        img.save(filename, format="png")
        final_img = filename
    except Exception as ex:
        print(ex)
    return final_img
