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

from typing import Union
from time import time
from uuid import uuid4

from pyrogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait, MessageNotModified

from gardevoir import Config, ralts
from gardevoir.helpers import db

USER_JSON = {}
IGNORE = db("IGNORED_USERS")


def check_user(func):
    async def wrapper(_, c_q: Union[Message ,CallbackQuery]):
        if isinstance(c_q, Message):
            pass
        if isinstance(c_q, CallbackQuery):
            cq = json.loads(str(c_q))
            user = cq['from_user']['id']
            if await IGNORE.find_one({"user_id": user}):
                return
            if user in Config.DEV_USERS or user==int(c_q.data.split("|").pop()):
                if user not in Config.DEV_USERS:
                    nt = time()
                    try:
                        ot = USER_JSON[user]
                        if nt-ot<1.8:
                            await c_q.answer(
                                "Stop spamming bot!!!\nElse you will be blacklisted",
                            )
                            x = await ralts.get_users(user)
                            await ralts.send_log(f"#Gardevoir #SPAM\n\nUser: {x.mention}\nUserID: {user}")
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