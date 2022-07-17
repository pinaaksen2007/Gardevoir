# Gardevoir PokeBot
# Copyright (C) 2022 KuuhakuTeam
#
# This file is a part of < https://github.com/KuuhakuTeam/Gardevoir/ >
# PLease read the GNU v3.0 License Agreement in 
# <https://www.github.com/KuuhakuTeam/Gardevoir/blob/master/LICENSE/>

from pyrogram import Client
from . import version, Config

import time
import os

from dotenv import load_dotenv


if os.path.isfile("config.env"):
    load_dotenv("config.env")

START_TIME = time.time()

class GardevoirPokeBot(Client):
    def __init__(self):
        kwargs = {
            'name': "gardevoir",
            'api_id': Config.API_ID,
            'api_hash': Config.API_HASH,
            'bot_token': Config.BOT_TOKEN,
            'in_memory': True,
            'plugins': dict(root="gardevoir.plugins")
        }
        super().__init__(**kwargs)

    async def start(self):
        await super().start()
        self.me = await self.get_me()
        text_ = f"#Gardevoir #Logs\n\n__Gardevoir i choose you!__\n\n**Version** : `{version.__ralts_version__}`\n**System** :` {self.system_version}`"
        await self.send_message(chat_id=Config.GP_LOGS, text=text_)
        print("Gardevoir i choose you!")

    async def stop(self):
        text_ = f"#SLEEPING #LOGS\n\n__Gardevoir returned to pokeball.__**"
        await self.send_message(chat_id=Config.GP_LOGS, text=text_)
        await self.export_session_string()
        await super().stop()
        print("Gardevoir returned to pokeball.")

    async def send_log(self, text: str, *args, **kwargs):
        await self.send_message(
            chat_id=Config.GP_LOGS,
            text=text,
            *args,
            **kwargs,
        )

    async def send_err(self, e: str):
        await self.send_message(
            chat_id=Config.GP_LOGS,
            text="#ERROR #LOGS\n\n{}".format(e)
        )

ralts = GardevoirPokeBot()
