from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client 
import os
import asyncio
from autumn import kaykay as app
from autumn.kay.decorators.errors import capture_err
from autumn import telegraph









@app.on_message(filters.photo)
@capture_err
async def telegraphphoto(client, message):
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

@app.on_message(filters.video)
@capture_err
async def telegraphvid(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Video size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\nJoin **',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)
