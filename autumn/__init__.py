from pyrogram import Client, errors
from autumn.config import APP_ID, API_HASH, TOKEN, BOT_ID, OWNER_ID
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


kaykay = Client("Chatbot", api_id=APP_ID, api_hash=API_HASH, bot_token=TOKEN)
