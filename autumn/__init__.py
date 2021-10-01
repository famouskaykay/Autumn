print("[INFO]: INITIALIZING")
from pyrogram import Client, errors
from autumn.config import APP_ID, API_HASH, TOKEN, BOT_ID, OWNER_ID
import logging
from telegraph import Telegraph
import asyncio
from kaysconfig import LOG_GROUP_ID
import time
from os import path
from aiogram import Bot, Dispatcher, types
from pyromod import listen

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

kaykay = Client("autumn", api_id=APP_ID, api_hash=API_HASH, bot_token=TOKEN)


LOG_GROUP_ID = LOG_GROUP_ID

MOD_LOAD = []
MOD_NOLOAD = []
bot_start_time = time.time()

kevin = kaykay.get_me()

BOT_NAME = kevin.first_name


telegraph = Telegraph()
telegraph.create_account(short_name=BOT_NAME)

print("[INFO]: STARTING BOT CLIENT ")
kaykay.start()
