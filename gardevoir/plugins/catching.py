# Gardevoir PokeBot
# Copyright (C) 2022 KuuhakuTeam
#
# This file is a part of < https://github.com/KuuhakuTeam/Gardevoir/ >
# PLease read the GNU v3.0 License Agreement in 
# <https://www.github.com/KuuhakuTeam/Gardevoir/blob/master/LICENSE/>

import random
import asyncio

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from gardevoir import ralts, trg
from gardevoir.helpers import input_str, db, find_bag, add_to_pokebag, add_to_user


BASE_NORMAL = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"
BASE_SHINY = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/"
BASE_API = "https://pokeapi.co/api/v2/pokemon/"

CATCH = db("TEMP_CATCH")


@ralts.on_message(filters.command("catch", trg))
async def catch_(c: ralts, m: Message):
    query = input_str(m)
    if not query:
        return
    found = await CATCH.find_one({"chat_id": m.chat.id})
    if found:
        if not await find_bag(m.from_user.id):
            msg = "<b>You still don't have registration in our pokemon academy, talk to Professor Oak to enter the pokemon world</b>"
            btn_ = [
                [
                    InlineKeyboardButton("Talk to Oak", callback_data=f"_start_adventure|{m.from_user.id}")
                ]
            ]
            return await m.reply(msg, reply_markup=InlineKeyboardMarkup(btn_))
        name = found["pokemon"]
        level = min(max(int(random.normalvariate(20, 10)), 1), 100)
        id_ = found["id"]
        xp_ = found["exp"]
        shiny = found["shiny"]
        if name == query:
            user = await c.get_users(m.from_user.id)
            if shiny == True:
                name = f"✨ {name}"
            await asyncio.gather(
                m.reply(f"<b>🌟 Congratulations {user.mention}!</b>\n\n<i>You caught a level {level} {name}! Added to Pokebag.\nYou received {xp_} Experience and 35 Pokedolars!</i>"),
                CATCH.delete_one({"chat_id": m.chat.id}),
                add_to_pokebag(user.id, id_, name, name, level, 0, shiny),
                add_to_user(user.id, xp_, 35)
            )
        else:
            await m.reply("That is the wrong pokémon!")
    else:
        return

