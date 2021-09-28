from pyrogram import Client, errors
from autumn.config import Config
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)



APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN
BOT_ID = Config.BOT_ID
OWNER_ID = Config.OWNER_ID

cb = Client("Chatbot", api_id=APP_ID, api_hash=API_HASH, bot_token=TOKEN)
