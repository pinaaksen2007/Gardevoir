# Gardevoir PokeBot
# Copyright (C) 2022 KuuhakuTeam
#
# This file is a part of < https://github.com/KuuhakuTeam/Gardevoir/ >
# PLease read the GNU v3.0 License Agreement in 
# <https://www.github.com/KuuhakuTeam/Gardevoir/blob/master/LICENSE/>
#
# functions retired from < https://github.com/lostb053/anibot >

import json
import asyncio

from time import time
from uuid import uuid4

from pyrogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait, MessageNotModified

from gardevoir import Config, ralts
from gardevoir.helpers import db

USER_WC = {}
USER_JSON = {}
ANON_JSON = {}
IGNORE = db("IGNORED_USERS")


def rand_key():
    return str(uuid4())[:8]

def control_user(func):
    async def wrapper(_, message: Message):
        msg = json.loads(str(message))
        if func.__name__ not in ["pong_", "quote", "feed_", "help_", "list_disabled", "start_", "auth_link_cmd", "logout_cmd", "list_tags_genres_cmd"]:
            try:
                msg['sender_chat']
                key = rand_key()
                ANON_JSON[key] = [func, message, msg]
                await message.reply_text('Click the below button to get results', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Click Here', callback_data=f"confirm_{key}")]]))
                return
            except KeyError:
                pass
        try:
            user = msg['from_user']['id']
        except KeyError:
            user = msg['chat']['id']
        if await IGNORE.find_one({'_id': user}):
            return
        nut = time()
        if user not in Config.DEV_USERS:
            try:
                out = USER_JSON[user]
                if nut-out<1.2:
                    USER_WC[user] += 1
                    if USER_WC[user] == 3:
                        await message.reply_text(
                            "Stop spamming bot!!!\nElse you will be blacklisted",
                        )
                        await ralts.send_log(f"#Gardevoir #SPAM\n\nUserID: {user}")
                    if USER_WC[user] == 5:
                        await IGNORE.insert_one({'_id': user})
                        await message.reply_text('You have been exempted from using this bot now due to spamming 5 times consecutively!!!')
                        await ralts.send_log(f"#Gardevoir #SPAM #BLOCKED\n\nUserID: {user}")
                        return
                    await asyncio.sleep(USER_WC[user])
                else:
                    USER_WC[user] = 0
            except KeyError:
                pass
            USER_JSON[user] = nut
        try:
            await func(_, message, msg)
        except FloodWait as e:
            await asyncio.sleep(e.x + 5)
        except MessageNotModified:
            pass
    return wrapper


def check_user(func):
    async def wrapper(_, c_q: CallbackQuery):
        cq = json.loads(str(c_q))
        user = cq['from_user']['id']
        if await IGNORE.find_one({'_id': user}):
            return
        if user in Config.DEV_USERS or user==int(cq['data'].split("|").pop()):
            if user not in Config.DEV_USERS:
                nt = time()
                try:
                    ot = USER_JSON[user]
                    if nt-ot<1.4:
                        await c_q.answer(
                            "Stop spamming bot!!!\nElse you will be blacklisted",
                        )
                        await ralts.send_log(f"#Gardevoir #SPAM\n\nUserID: {user}")
                except KeyError:
                    pass
                USER_JSON[user] = nt
            try:
                await func(_, c_q)
            except FloodWait as e:
                await asyncio.sleep(e.x + 5)
            except MessageNotModified:
                pass
        else:
            await c_q.answer(
                "This is not for you!!!",
                show_alert=True,
            )
    return wrapper