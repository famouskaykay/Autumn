from autumn import kaykay 
import asyncio
from pyrogram import filters, Client 


from pyrogram.types import (
  Message, 
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import os
import re

buttons = [[InlineKeyboardButton("Github", url="https://github.com/famouskaykay/Autumn"),]]
        

@kaykay.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.edited,
    group=2,
)
async def kukiai(client: Client, message: Message):
    msg = message.text
    chat_id = message.chat.id

    Kuki =   requests.get(f"https://kuki-api.tk/api/botname/owner/message={msg}").json()

    moezilla = f"{Kuki['reply']}"
      
    await client.send_chat_action(message.chat.id, "typing")
    await message.reply_text(moezilla)
 
  
    
@kaykay.on_message(filters.command(["help", "start"]))
async def hello(client, message):
    await message.reply_text(f"Hello {message.from_user.mention},", reply_markup=InlineKeyboardMarkup(buttons))

    
