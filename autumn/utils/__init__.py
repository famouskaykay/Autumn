import asyncio
import math
import shlex
import sys
import time
import traceback
from typing import Callable, Coroutine, Dict, List, Tuple, Union

from pyrogram import Client
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Chat, Message, User

from autumn import OWNER_ID
from autumn import kaykay


from .misc import paginate_modules  
from .read_lines import random_line  

def admins_only(func: Callable) -> Coroutine:
    async def wrapper(client: Client, message: Message):
        if message.from_user.id == OWNER_ID:
            return await func(client, message)
        admins = await get_administrators(message.chat)
        for admin in admins:
            if admin.id == message.from_user.id:
                return await func(client, message)

    return wrapper
  
async def edit_or_reply(message, text, parse_mode="md"):
    if message.from_user.id:
        if message.reply_to_message:
            kk = message.reply_to_message.message_id
            return await message.reply_text(
                text, reply_to_message_id=kk, parse_mode=parse_mode
            )
        return await message.reply_text(text, parse_mode=parse_mode)
    return await message.edit(text, parse_mode=parse_mode)
