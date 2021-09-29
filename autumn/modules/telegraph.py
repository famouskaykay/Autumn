from pyrogram import filters
from pyrogram.types import Message

import asyncio
from autumn import kaykay as app
from autumn.kay.decorators.errors import capture_err
from telegraph import Telegraph




kevin = app.get_me()

BOT_NAME = kevin.first_name + (kevin.last_name or "")
BOT_USERNAME = kevin.username
BOT_MENTION = kevin.mention

telegraph = Telegraph()
telegraph.create_account(short_name=BOT_USERNAME)


@app.on_message(filters.command("telegraph"))
@capture_err
async def paste(_, message: Message):
    reply = message.reply_to_message

    if not reply or not reply.text:
        return await message.reply("Reply to a text message")

    if len(message.command) < 2:
        return await message.reply("**Usage:**\n /telegraph [Page name]")

    page_name = message.text.split(None, 1)[1]
    page = telegraph.create_page(page_name, html_content=reply.text.html)
    return await message.reply(
        f"**Posted:** {page['url']}",
        disable_web_page_preview=True,
    )


