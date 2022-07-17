# Gardevoir PokeBot
# Copyright (C) 2022 raltsTeam
#
# This file is a part of < https://github.com/raltsTeam/Gardevoir/ >
# PLease read the GNU v3.0 License Agreement in
# <https://www.github.com/raltsTeam/Gardevoir/blob/master/LICENSE/>

import asyncio

from gardevoir import ralts
from gardevoir.helpers import db


USERS = db("USERS")
GROUPS = db("GROUPS")
POKEBAG = db("POKEBAG")



# Users
async def find_user(uid):
    if await USERS.find_one({"user_id": uid}):
        return True


async def find_bag(uid):
    if await POKEBAG.find_one({"user_id": uid}):
        return True


async def add_user(uid):
    try:
        x = await ralts.get_users(uid)
        user_start = f"#Gardevoir #NEW_USER #LOGS\n\n<b>User:</b> {x.mention}\n<b>ID:</b> {x.id}"
        await asyncio.gather(
            USERS.insert_one(
                {
                    "user_id": x.id,
                    "user": x.first_name,
                    "caught_count": 0,
                    "exp": 0,
                    "pokedolar": 0
                }
            ),
            ralts.send_log(
                user_start, disable_notification=False, disable_web_page_preview=True
            ),
        )
    except Exception as e:
        await ralts.send_err(e)


# Groups
async def find_gp(gid):
    if await GROUPS.find_one({"chat_id": gid}):
        return True


async def add_gp(m):
    user = f"<a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name}</a>"
    user_start = f"#Gardevoir #NEW_GROUP #LOGS\n\n<b>Group</b>: {m.chat.title}\n<b>ID:</b> {m.chat.id}\n<b>User:</b> {user}"
    try:
        await GROUPS.insert_one({"chat_id": m.chat.id, "title": m.chat.title}),
        await ralts.send_log(
            user_start, disable_notification=False, disable_web_page_preview=True
        )
    except Exception as e:
        await ralts.send_err(e)


async def del_gp(m):
    del_txt = f"#Gardevoir #LEFT_GROUP #LOGS\n\n<b>Group</b>: {m.chat.title}\n<b>ID:</b> {m.chat.id}"
    try:
        await GROUPS.delete_one({"chat_id": m.chat.id})
        await ralts.send_log(
            del_txt, disable_notification=False, disable_web_page_preview=True
        )
    except Exception as e:
        await ralts.send_err(e)
