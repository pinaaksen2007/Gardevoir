# Gardevoir PokeBot
# Copyright (C) 2022 KuuhakuTeam
#
# This file is a part of < https://github.com/KuuhakuTeam/Gardevoir/ >
# PLease read the GNU v3.0 License Agreement in 
# <https://www.github.com/KuuhakuTeam/Gardevoir/blob/master/LICENSE/>

import psutil

from pyrogram.errors import ChatWriteForbidden
from pyrogram.types import Message
from pyrogram.enums import ChatType
from pyrogram import filters

from gardevoir import ralts, trg
from gardevoir.helpers import db, is_dev, find_gp, del_gp, add_gp


USERS = db("USERS")
GROUPS = db("GROUPS")


@ralts.on_message(filters.command(["stats", "status"], trg))
async def status_(_, m: Message):
    user_id = m.from_user.id
    if not is_dev(user_id):
        return
    msg = await m.reply("`Processing ...`")
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    glist = await GROUPS.estimated_document_count()
    ulist = await USERS.estimated_document_count()
    await msg.edit(f"""
╭─❑ 「 **Bot Stats** 」 ❑──
│- __Users:__ `{ulist}`
│- __Groups:__ `{glist}`
╰❑

╭─❑ 「 **Hardware Usage** 」 ❑──
│- __CPU Usage:__ `{cpu_usage}%`
│- __RAM Usage:__ `{ram_usage}%`
╰❑
""")


@ralts.on_message(filters.new_chat_members)
async def thanks_for(c: ralts, m: Message):
    if c.me.id in [x.id for x in m.new_chat_members]:
        if not await find_gp(m.chat.id):
            await add_gp(m)
        try:
            await c.send_message(
                chat_id=m.chat.id,
                text="<i>Thanks for adding me to the group\n\nsome functions are still under development report bugs and errors at -> @fnixsup</i>",
                disable_notification=True,
            )
        except ChatWriteForbidden:
            ralts.send_err("\n[ ERROR ] Bot cannot send messages\n")
            print("\n[ ERROR ] Bot cannot send messages\n")


@ralts.on_message(filters.left_chat_member)
async def left_chat_(c: ralts, m: Message):
    if c.me.id == m.left_chat_member.id:
        if await find_gp(m.chat.id):
            await del_gp(m)
        else:
            return


@ralts.on_message()
async def thanks_for(_, m: Message):
    if m.chat.type == ChatType.GROUP or ChatType.SUPERGROUP:
        if not await find_gp(m.chat.id):
            await add_gp(m)
