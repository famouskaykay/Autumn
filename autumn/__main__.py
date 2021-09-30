import importlib
import asyncio
import uvloop
from autumn import kaykay
from autumn.modules import *
from pyrogram import idle, Client
import time
from autumn.modules import ALL_MODULES

loop = asyncio.get_event_loop()

print("[INFO]: INITIALIZING ")




if __name__ == "__main__":
    uvloop.install()
    loop.run_until_complete(start_bot())
