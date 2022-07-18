# Gardevoir PokeBot
# Copyright (C) 2022 KuuhakuTeam
#
# This file is a part of < https://github.com/KuuhakuTeam/Gardevoir/ >
# PLease read the GNU v3.0 License Agreement in 
# <https://www.github.com/KuuhakuTeam/Gardevoir/blob/master/LICENSE/>

import asyncio
from typing import Union

from pyrogram import filters
from pyrogram.types import Message, CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton

from gardevoir import ralts, trg
from gardevoir.helpers import db, get_response, check_user, add_to_pokebag, is_shiny, find_bag, find_user, add_user


USERS = db("USERS")

MSG = "<b>Hello there, welcome to the world of pokemon. My name is Oak.\n\nBefore starting your adventure as a pokemon master, you first need to define your starting pokemon. Choose wisely as he will be your companion until the end of your journey.</b>"


@ralts.on_callback_query(filters.regex(pattern=r"^_start_adventure\|(.*)"))
@ralts.on_message(filters.command("adventure", trg))
async def adventure(_, m: Union[Message, CallbackQuery]):
    btn_ = [
        [
            InlineKeyboardButton("Start Adventure", callback_data=f"_adventure|{m.from_user.id}")
        ]
    ]
    if isinstance(m, Message):
        if not await find_user(m.from_user.id):
            await add_user(m.from_user.id)
        if await find_bag(m.from_user.id):
            return await m.reply("<b>You already started your pokemon journey</b>")
        await m.reply_photo("https://telegra.ph/file/dded46ce66300898eb023.jpg", caption=MSG, reply_markup=InlineKeyboardMarkup(btn_))
    elif isinstance(m, CallbackQuery):
        data, uid = m.data.split("|")
        if not uid == m.from_user.id:
            return await m.answer("This is not for you!!!",show_alert=True)
        await m.message.delete()
        await ralts.send_photo(m.message.chat.id, photo="https://telegra.ph/file/dded46ce66300898eb023.jpg", caption=MSG, reply_markup=InlineKeyboardMarkup(btn_))


@ralts.on_callback_query(filters.regex(pattern=r"^_adventure\|(.*)"))
@check_user
async def select_poke(_, c_q: CallbackQuery):
    btn_ = [
        [
            InlineKeyboardButton("Bulbasaur", callback_data=f"_starter|1|{c_q.from_user.id}"),
            InlineKeyboardButton("Charmander", callback_data=f"_starter|4|{c_q.from_user.id}"),
            InlineKeyboardButton("Squirtle", callback_data=f"_starter|7|{c_q.from_user.id}")
        ],
        [
            InlineKeyboardButton("Chikorita", callback_data=f"_starter|152|{c_q.from_user.id}"),
            InlineKeyboardButton("Cyndaquil", callback_data=f"_starter|155|{c_q.from_user.id}"),
            InlineKeyboardButton("Totodile", callback_data=f"_starter|158|{c_q.from_user.id}")
        ],
        [
            InlineKeyboardButton("Treecko", callback_data=f"_starter|252|{c_q.from_user.id}"),
            InlineKeyboardButton("Torchic", callback_data=f"_starter|255|{c_q.from_user.id}"),
            InlineKeyboardButton("Mudkip", callback_data=f"_starter|258|{c_q.from_user.id}")
        ],
    ]
    await c_q.edit_message_media(media=InputMediaPhoto(media="https://telegra.ph/file/e0a52ab73cfe98a7fd398.jpg", caption="<b>To start your adventure in the pokemon world first choose your starter pokemon.</b>"), reply_markup=InlineKeyboardMarkup(btn_))


@ralts.on_callback_query(filters.regex(pattern=r"_starter\|(.*)"))
@check_user
async def confirm_poke(_, c_q: CallbackQuery):
    data, pid, uid = c_q.data.split("|")
    view_data = await get_response.json(link=f"https://pokeapi.co/api/v2/pokemon/{pid}")
    status, types = "", ""
    name = (view_data["name"])
    for type in view_data["types"]:
        types += f"│- <i>{type['type']['name'].capitalize()}</i>\n"
    for stat in view_data["stats"]:
        status += f"│- <i>{stat['stat']['name'].capitalize()}:</i> <code>{stat['base_stat']}</code>\n"
    msg = f"╭─❑ 「 <b>{name.capitalize()}</b> 」 ❑──\n{types}╰❑\n╭─❑ 「 <b>Status Base</b> 」 ❑──\n{status}╰❑\n\n<b>Would you like to choose this pokemon as your starter?</b>"
    btn_ = [
        [
            InlineKeyboardButton("Yes, I'm sure", callback_data=f"add_to_bag|{pid}|{c_q.from_user.id}")
        ],
        [
            InlineKeyboardButton("Choose another", callback_data=f"_adventure|{c_q.from_user.id}")
        ]
    ]
    await c_q.edit_message_media(media=InputMediaPhoto(media=view_data["sprites"]["other"]["home"]["front_default"], caption=msg), reply_markup=InlineKeyboardMarkup(btn_))


@ralts.on_callback_query(filters.regex(pattern=r"add_to_bag\|(.*)"))
@check_user
async def confirm_poke(_, c_q: CallbackQuery):
    data, pid, uid = c_q.data.split("|")
    view_data = await get_response.json(link=f"https://pokeapi.co/api/v2/pokemon/{pid}")
    name = view_data["name"]
    await asyncio.gather(
        add_to_pokebag(c_q.from_user.id, pid, name, name, 1, 0, is_shiny()),
        c_q.edit_message_caption(caption=f"<b>Congratulations, you chose {name} as your starter. take good care of him</b>")
    )


