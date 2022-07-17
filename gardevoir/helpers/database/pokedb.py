# Gardevoir PokeBot
# Copyright (C) 2022 KuuhakuTeam
#
# This file is a part of < https://github.com/KuuhakuTeam/Gardevoir/ >
# PLease read the GNU v3.0 License Agreement in
# <https://www.github.com/KuuhakuTeam/Gardevoir/blob/master/LICENSE/>

import uuid
import random

from datetime import datetime

from gardevoir.helpers import const
from gardevoir.helpers.database.data import USERS
from .core import db

USERS = db("USERS")
POKEBAG = db("POKEBAG")


def random_iv(): return random.randint(0, 31)
def random_nature(): return random.choice(const.NATURES)
def rand_key(): return uuid.uuid4().hex

def ivs():
    ivs = [random_iv() for _ in range(6)]
    ivs_base = {
    "iv_hp": ivs[0],
    "iv_atk": ivs[1],
    "iv_defn": ivs[2],
    "iv_satk": ivs[3],
    "iv_sdef": ivs[4],
    "iv_spd": ivs[5],
    }
    return ivs_base

def is_shiny() -> bool:
    return random.randint(1, 4096) == 1


async def add_to_pokebag(uid: int, dex_id: int, name: str, nickname: str, level: int, exp: int, shiny: bool):
    user = {"user_id": uid}
    poke_info = [
        {
            "id_": rand_key(),
            "dex_id": dex_id,
            "name": name,
            "nickname": nickname,
            "level": level,
            "exp": exp,
            "caught_date": datetime.now().strftime("%Y-%m-%d"),
            "nature": random_nature(),
            "ivs": ivs(),
            "shiny": shiny
        }
    ]
    insert_poke = {"$push": {"pokebag": {"$each": poke_info}}}
    await POKEBAG.update_one(user, insert_poke, upsert=True)


async def add_to_user(uid: int, xp: int, pokedolar: int):
    user = {"user_id": uid}
    find = await USERS.find_one(user)
    xp_ = find["exp"]
    pokedolar_ = find["pokedolar"]
    caught_ = find["caught_count"]
    insert_value = {
        "$set": {
            "exp": xp_+xp,
            "pokedolar": pokedolar_+pokedolar,
            "caught_count": caught_+1
        }
    }
    await USERS.update_one(user, insert_value)