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

  if message.text and not message.document:
        if not kuki_message(context, message):
            return
        Message = message.text
        kuki.send_chat_action(chat_id, action="typing")
        kukiurl = requests.get('https://kuki-api.tk/api/Raiden/moezilla/message='+Message)
        Kuki = json.loads(kukiurl.text)
        kuki = Kuki['reply']
        sleep(0.3)
        message.reply_text(kuki, timeout=60)
    
@kaykay.on_message(filters.command(["help", "start"]))
async def hello(client, message):
  
    await message.reply_text(f"Hello {message.from_user.mention},", reply_markup=InlineKeyboardMarkup(buttons))

    
