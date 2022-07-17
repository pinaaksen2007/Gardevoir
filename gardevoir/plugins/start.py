# Gardevoir PokeBot
# Copyright (C) 2022 KuuhakuTeam
#
# This file is a part of < https://github.com/KuuhakuTeam/Gardevoir/ >
# PLease read the GNU v3.0 License Agreement in 
# <https://www.github.com/KuuhakuTeam/Gardevoir/blob/master/LICENSE/>

import time
import asyncio
from typing import Union

from pyrogram.enums import ChatType
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from gardevoir import ralts, version, START_TIME, trg
from gardevoir.helpers import db, uptime, find_user, add_user

BOT_START = db("BOT_START")
USERS = db("USERS")


@ralts.on_callback_query(filters.regex(pattern=r"^start_back$"))
@ralts.on_message(filters.command("start", trg))
async def start_(c: ralts, m: Union[Message, CallbackQuery]):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Info", callback_data="infos"),
                InlineKeyboardButton(
                    text="Help", url=f"https://t.me/{c.me.username}?start=help_"),
            ],
            [
                InlineKeyboardButton(
                    text="✾ Add to a group ✾",
                    url=f"https://t.me/{c.me.username}?startgroup=new",
                ),
            ],
        ]
    )
    if isinstance(m, Message):
        if not m.chat.type == ChatType.PRIVATE:
            return
        if not await find_user(m.from_user.id):
            await add_user(m.from_user.id)
        await c.send_photo(m.chat.id, photo="https://telegra.ph/file/deb86993e7aa61c7d4383.png", caption="soon", reply_markup=keyboard)
    if isinstance(m, CallbackQuery):
        await c.edit_message_caption(
            chat_id=m.message.chat.id,
            message_id=m.message.id,
            caption="soon",
            reply_markup=keyboard
        )


@ralts.on_callback_query(filters.regex(pattern=r"^infos$"))
async def infos(c: ralts, m: CallbackQuery):
    info_text = f"""
**✾ Bot Status ✾**

• **Version:** `{version.__ralts_version__}`
• **Uptime:** `{uptime()}`
• **Python:** `{version.__python_version__}`
• **Pyrogram:** `{version.__pyro_version__}`
"""
    button = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Back", callback_data="start_back"),
                ]
            ]
        )
    await c.edit_message_caption(
        chat_id=m.message.chat.id,
        message_id=m.message.id,
        caption=info_text,
        reply_markup=button
    )
