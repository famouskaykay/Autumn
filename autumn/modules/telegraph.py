from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client 
import os
import asyncio
from autumn import kaykay as app
from autumn.kay.decorators.errors import capture_err
from autumn import telegraph


@app.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.edited,
    group=2,
)

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
    if len(message.photo):
        msg = await message.reply_text("Uploading To Telegraph...")
        download_location = await client.download_media(
        message=message, file_name='root/jetg')
        try:
        response = upload_file(download_location)
        except:
        await msg.edit_text("Photo size should be less than 5mb!") 
        else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\nJoin **',
            disable_web_page_preview=True,
        )
        finally:
        os.remove(download_location)

        
    
