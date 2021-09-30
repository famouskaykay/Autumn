from autumn import kaykay as kevin
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
        
@kevin.on_message(filters.command(["help", "start"]))
async def hello(client, message):
    await message.reply_text(f"Hello {message.from_user.mention},", reply_markup=InlineKeyboardMarkup(buttons))

    
@kevin.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.edited,
    group=2,
)  
async def kays(client, message):
  msg = message.text
  chat_id = message.chat.id

  autumn =   requests.get(f"https://kuki-api.tk/api/botname/owner/message={msg}").json()

  kay = f"{autumn['reply']}"
      
  await client.send_chat_action(message.chat.id, "typing")
  await message.reply_text(kay)



kevin.run()
