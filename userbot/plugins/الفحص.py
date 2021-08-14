import random
import re
import time
from platform import python_version

from telethon import version, Button
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from userbot import StartTime, ICE16, catversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "utils"

@ICE16.ar_cmd(
    pattern="فحص$",
    command=("فحص", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    ICE16 = gvarstatus("ALIVE_EMOJI") or "  - "
    ICE16_TEXT = gvarstatus("ALIVE_TEXT") or "**- ICE16 USERBOT.**"
    ICE16_IMG = gvarstatus("ALIVE_PIC") or " https://telegra.ph/file/6094170a833051afc2924.jpg "
    if ICE16_IMG:
        ICE50 = [x for x in ICE16_IMG.split()]
        A_IMG = list(ICE50)
        PIC = random.choice(A_IMG)
        ICE50_caption = f"**{ICE16_TEXT}**\n"
        ICE50_caption += f"✛━━━━━━━━━━━━━✛\n"
        ICE50_caption += f"**{ICE16} قاعدة البيانات ›** تـعمل بنجـاح\n"
        ICE50_caption += f"**{ICE16} نسخـۿ التليثون  ›** {version.__version__}\n"
        ICE50_caption += f"**{ICE16} نسخـۿ جـمثون ›** {catversion}\n"
        ICE50_caption += f"**{ICE16} نسخـۿ البايثون ›** {python_version()}\n"
        ICE50_caption += f"**{ICE16} مدة التشغيل ›** {uptime}\n"
        ICE50_caption += f"**{ICE16} المستخدم ›** {mention}\n"
        ICE50_caption += f"**{ICE16}**  **[مطور السورس]**(t.me/ICE50)   \n"
        ICE50_caption += f"✛━━━━━━━━━━━━━✛\n"
        await event.client.send_file(
            event.chat_id, PIC, caption=ICE50_caption, reply_to=reply_to_id
        )
        await event.delete()
    else:
        await edit_or_reply(
            event,
            f"**{ICE16_TEXT}**\n\n"
            f"**{ICE16} قاعدۿ البيانات ›** `تـعمل بنجـاح`\n"
            f"**{ICE16} نسخۿ تليثون ›** `{version.__version__}\n`"
            f"**{ICE16} نسخـۿ آيس ›** `{catversion}`\n"
            f"**{ICE16} نسخـۿ البايثون ›** `{python_version()}\n`"
            f"**{ICE16} الوقت ›** `{uptime}\n`"
            f"**{ICE16} المنشئ›** {mention}\n",
        )

@ICE16.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await catalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
