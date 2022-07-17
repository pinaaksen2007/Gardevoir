# Gardevoir PokeBot
# Copyright (C) 2022 KuuhakuTeam
#
# This file is a part of < https://github.com/KuuhakuTeam/Gardevoir/ >
# PLease read the GNU v3.0 License Agreement in 
# <https://www.github.com/KuuhakuTeam/Gardevoir/blob/master/LICENSE/>

__all__ = ["db"]

import asyncio

from motor.core import AgnosticClient, AgnosticCollection, AgnosticDatabase
from motor.motor_asyncio import AsyncIOMotorClient

from gardevoir import Config

print("Connecting to Database ...")

DATABASE_URL = Config.DB_URI

_MGCLIENT: AgnosticClient = AsyncIOMotorClient(DATABASE_URL)
_RUN = asyncio.get_event_loop().run_until_complete

if "gardevoir" in _RUN(_MGCLIENT.list_database_names()):
    print("Gardevoir db Found :) => Now Logging to it...")
else:
    print("Gardevoir db Not Found :( => Creating New db...")

_DATABASE: AgnosticDatabase = _MGCLIENT["gardevoir"]


def db(name: str) -> AgnosticCollection:
    """Create or Get Collection from your database"""
    return _DATABASE[name]


def _close_db() -> None:
    _MGCLIENT.close()
