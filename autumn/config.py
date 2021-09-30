import os

from os import getenv
from dotenv import load_dotenv

load_dotenv()
APP_ID = int(os.getenv("API_ID", "6"))
API_HASH = os.getenv("API_HASH", "eb06d4abeb98ae0f581e")
TOKEN = os.getenv("BOT_TOKEN")
BOT_ID = os.getenv("BOT_ID")
OWNER_ID = os.getenv("OWNER_ID")
LOG_GROUP_ID = os.getenv(LOG_GROUP_ID)

