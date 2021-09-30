import importlib
from kaysconfig import LOG_GROUP_ID
import asyncio
import uvloop
from autumn import kaykay
from autumn.modules import *
from pyrogram import idle, Client
import time
from autumn.modules import ALL_MODULES

loop = asyncio.get_event_loop()


async def start_bot():
    bot_modules = ""
    j = 1
    for i in ALL_MODULES:
        if j == 4:
            bot_modules += "|{:<15}|\n".format(i)
            j = 0
        else:
            bot_modules += "|{:<15}".format(i)
        j += 1
    print(
        "+_________________________________________________________________"
    )
    print(
        "|                           Autumn                               |"
    )
    print(
        "+_________________________________________________________________+"
    )
    print(bot_modules)
    print(
        "+_________________________________________________________________+"
    )
    print(f"[INFO]: BOT STARTED !"))
    try:
        print("[INFO]: SENDING ONLINE STATUS")
        await kaykay.send_message(LOG_GROUP_ID, "autumn has started!")
    except Exception:
        pass
    await idle()
    print("[INFO]: STOPPING BOT  ")   

print("[INFO]: INITIALIZING ")




if __name__ == "__main__":
    uvloop.install()
    loop.run_until_complete(start_bot())
