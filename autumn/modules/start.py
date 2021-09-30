from autumn import kaykay as autumn
import asyncio
from pyrogram import filters, Client 


from pyrogram.types import (
  Message, 
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import os
import re



@autumn.on_message(filters.command(["help", "start"]))
async def hello(client, message):
    await message.reply_text(f"Hello {message.from_user.mention}  !")

    
    
async def autumnai(client: Client, message: Message):
  msg = message.text
  chat_id = message.chat.id

  autumn =   requests.get(f"https://kuki-api.tk/api/botname/owner/message={msg}").json()

  kaykay = f"{autumn['reply']}"
      
  await client.send_chat_action(message.chat.id, "typing")
  await message.reply_text(kaykay)


messageprivate = '''
Hi, I'm autumn Chat Bot
'''

messagegroup = '''
Hi, I'm autumn Chat Bot
'''


@autumn.on_message(filters.command("start"))
async def start(_, message):
    self = await autumn.get_me()
    busername = self.username
    if message.chat.type != "private":
        await message.reply_text(messagegroup)
        return
    else:
        buttons = [[InlineKeyboardButton("Github", url="https://github.com/kaykay/Autumn"),
                    ]]
        await message.reply_text(messageprivate, reply_markup=InlineKeyboardMarkup(buttons))

autumn.run()
