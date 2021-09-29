from autumn import kaykay as autumn
import asyncio
from pyrogram import filters

@autumn.on_message(filters.command(["help", "start"]))
async def hello(client, message):
    await message.reply_text(f"Hello {message.from_user.mention}  !")
