import asyncio
import emoji

IBM_WATSON_CRED_URL = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/bd6b59ba-3134-4dd4-aff2-49a79641ea15"
IBM_WATSON_CRED_PASSWORD = "UQ1MtTzZhEsMGK094klnfa-7y_4MCpJY1yhd52MXOo3Y"
url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"
import re

import aiohttp
from google_trans_new import google_translator
from pyrogram import filters

from autumn import BOT_ID
from autumn.utils.arh import arq
from autumn.utils import admins_only, edit_or_reply
from autumn import kaykay

translator = google_translator()


async def lunaQuery(query: str, user_id: int):
    luna = await arq.luna(query, user_id)
    return luna.result


def extract_emojis(s):
    return "".join(c for c in s if c in emoji.UNICODE_EMOJI)


async def fetch(url):
    try:
        async with aiohttp.Timeout(10.0):
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    try:
                        data = await resp.json()
                    except:
                        data = await resp.text()
            return data
    except:
        print("AI response Timeout")
        return


kaykay_chats = []
en_chats = []
# AI Chat (C) 2020-2021 by @InukaAsith

@kaykay.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.edited
    & ~filters.via_bot
    & ~filters.forwarded,
    group=2,
)
async def chatbot_function(client, message):
    if not message.reply_to_message:
        return
    try:
        senderr = message.reply_to_message.from_user.id
    except:
        return
    if senderr != BOT_ID:
        return
    msg = message.text
    chat_id = message.chat.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    if chat_id in en_chats:
        test = msg
        test = test.replace("autumn", "Aco")
        test = test.replace("autumn", "Aco")
        response = await lunaQuery(
            test, message.from_user.id if message.from_user else 0
        )
        response = response.replace("Aco", "autumn")
        response = response.replace("aco", "autumn")

        pro = response
        try:
            await cb.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError:
            return

    else:
        u = msg.split()
        emj = extract_emojis(msg)
        msg = msg.replace(emj, "")
        if (
            [(k) for k in u if k.startswith("@")]
            and [(k) for k in u if k.startswith("#")]
            and [(k) for k in u if k.startswith("/")]
            and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
        ):

            h = " ".join(filter(lambda x: x[0] != "@", u))
            km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
            tm = km.split()
            jm = " ".join(filter(lambda x: x[0] != "#", tm))
            hm = jm.split()
            rm = " ".join(filter(lambda x: x[0] != "/", hm))
        elif [(k) for k in u if k.startswith("@")]:

            rm = " ".join(filter(lambda x: x[0] != "@", u))
        elif [(k) for k in u if k.startswith("#")]:
            rm = " ".join(filter(lambda x: x[0] != "#", u))
        elif [(k) for k in u if k.startswith("/")]:
            rm = " ".join(filter(lambda x: x[0] != "/", u))
        elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
            rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
        else:
            rm = msg
            # print (rm)
        try:
            lan = translator.detect(rm)
        except:
            return
        test = rm
        if not "en" in lan and not lan == "":
            try:
                test = translator.translate(test, lang_tgt="en")
            except:
                return
        # test = emoji.demojize(test.strip())

        test = test.replace("Naoto")
        test = test.replace("naoto")
        response = await lunaQuery(
            test, message.from_user.id if message.from_user else 0
        )
        response = response.replace("autumn")
        response = response.replace("Autumn")
        pro = response
        if not "en" in lan and not lan == "":
            try:
                pro = translator.translate(pro, lang_tgt=lan[0])
            except:
                return
        try:
            await kaykay.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError:
            return


@kaykay.on_message(
    filters.text & ~filters.edited & filters.reply & ~filters.bot
)
async def lol(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
    try:
        lan = translator.detect(rm)
    except:
        return
    test = rm
    if not "en" in lan and not lan == "":
        try:
            test = translator.translate(test, lang_tgt="en")
        except:
            return

    # test = emoji.demojize(test.strip())

    # Kang with the credits bitches @InukaASiTH

    test = test.replace("Naoto", "naoto")
    test = test.replace("naoto", "naoto")
    
    response = await lunaQuery(test, message.from_user.id if message.from_user else 0)
    response = response.replace("Naoto", "naoto")
    response = response.replace("naoto", "naoto")

    pro = response
    if not "en" in lan and not lan == "":
        pro = translator.translate(pro, lang_tgt=lan[0])
    try:
        await kaykay.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except CFError:
        return


@kaykay.on_message(
    filters.regex("Autumn|autumn")
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.reply
    & ~filters.channel
    & ~filters.edited
)
async def chat(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
    try:
        lan = translator.detect(rm)
    except:
        return
    test = rm
    if not "en" in lan and not lan == "":
        try:
            test = translator.translate(test, lang_tgt="en")
        except:
            return

    # test = emoji.demojize(test.strip())

    test = test.replace("Naoto", "naoto")
    test = test.replace("naoto", "naoto")
    response = await lunaQuery(test, message.from_user.id if message.from_user else 0)
    response = response.replace("Naoto", "naoto")
    response = response.replace("naoto", "naoto")

    pro = response
    if not "en" in lan and not lan == "":
        try:
            pro = translator.translate(pro, lang_tgt=lan[0])
        except Exception:
            return
    try:
        await kaykay.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except CFError:
        return
