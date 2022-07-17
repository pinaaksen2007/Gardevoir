# Gardevoir PokeBot
# Copyright (C) 2022 KuuhakuTeam
#
# This file is a part of < https://github.com/KuuhakuTeam/Gardevoir/ >
# PLease read the GNU v3.0 License Agreement in 
# <https://www.github.com/KuuhakuTeam/Gardevoir/blob/master/LICENSE/>

import asyncio

from pyrogram import filters
from pyrogram.types import Message

from gardevoir import ralts, trg
from gardevoir.helpers import db, find_user, add_user

POKEBAG = db("POKEBAG")
USERS = db("USERS")


@ralts.on_message(filters.command("pokebag", trg))
async def pokebg(_, m: Message):
    x = await POKEBAG.find_one({"user_id": m.from_user.id})
    if not x:
        return await m.reply("<i>You don't have pokemons</i>")
    y = await ralts.get_users(m.from_user.id)
    msg = f'<b>{y.mention} pokebag:</b>\n\n'
    pokemons = x["pokebag"]
    for pokes in pokemons:
        msg += f'<b>#{pokes["dex_id"]} {(pokes["name"]).capitalize()} level {pokes["level"]}</b>\n'
        msg += f'• Exp: <code>{pokes["exp"]}</code>\n'
        msg += f'• Nature: <code>{pokes["nature"]}</code>\n'
        msg += f'• Caught: <code>{pokes["caught_date"]}</code>\n\n'
    await m.reply(msg)


@ralts.on_message(filters.command("profile", trg))
async def profile(_, m: Message):
    uid = m.from_user.id
    if not await find_user(uid):
        await add_user(uid)
    await asyncio.sleep(1)
    x = await USERS.find_one({"user_id": uid})
    y = await ralts.get_users(uid)
    msg = f'<b>{y.mention} profile:</b>\n\n'
    msg += f'• Exp: <code>{x["exp"]}</code>\n'
    msg += f'• Pokedolars: <code>{x["pokedolar"]}</code>\n'
    msg += f'• Caught Pokemons: <code>{x["caught_count"]}</code>\n\n'
    await m.reply(msg)