from datetime import datetime
from math import floor

from telethon.utils import get_display_name

from userbot import jmthon

from ..Config import Config
from ..core.logger import logging
from ..helpers import reply_id
from ..helpers.utils import _format
from ..sql_helper.bot_blacklists import add_user_to_bl, rem_user_from_bl
from ..sql_helper.bot_pms_sql import get_user_id
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)

plugin_category = "bot"
botusername = Config.TG_BOT_USERNAME


async def get_user_and_reason(event):
    id_reason = event.pattern_match.group(1)
    replied = await reply_id(event)
    user_id, reason = None, None
    if replied:
        users = get_user_id(replied)
        if users is not None:
            for usr in users:
                user_id = int(usr.chat_id)
                break
            reason = id_reason
    elif id_reason:
        data = id_reason.split(maxsplit=1)
        if len(data) == 2:
            user, reason = data
        elif len(data) == 1:
            user = data[0]
        if user.isdigit():
            user_id = int(user)
        if user.startswith("@"):
            user_id = user
    return user_id, reason


# taken from https://github.com/code-rgb/USERGE-X/blob/f95766027ef95854d05e523b42cd158c2e8cdbd0/userge/plugins/bot/bot_forwards.py#L420
def progress_str(total: int, current: int) -> str:
    percentage = current * 100 / total
    prog_arg = "**العـملية** : `{}%`\n" "```[{}{}]```"
    return prog_arg.format(
        percentage,
        "".join((Config.FINISHED_PROGRESS_STR for i in range(floor(percentage / 5)))),
        "".join(
            (Config.UNFINISHED_PROGRESS_STR for i in range(20 - floor(percentage / 5)))
        ),
    )


async def ban_user_from_bot(user, reason, reply_to=None):
    try:
        date = str(datetime.now().strftime("%B %d, %Y"))
        add_user_to_bl(user.id, get_display_name(user), user.username, reason, date)
    except Exception as e:
        LOGS.error(str(e))
    banned_msg = (
        f"**تم حظرك من ااستخدام هذا البوت\nالسبب** : {reason}"
    )
    await jmthon.tgbot.send_message(user.id, banned_msg)
    info = f"**#المستخدمين_المحظورين**\
            \n\n👤 {_format.mentionuser(get_display_name(user) , user.id)}\
            \n**الاسم الاول:** {user.first_name}\
            \n**الايدي:** `{user.id}`\
            \n**السبب:** `{reason}`"
    if BOTLOG:
        await jmthon.send_message(BOTLOG_CHATID, info)
    return info


async def unban_user_from_bot(user, reason, reply_to=None):
    try:
        rem_user_from_bl(user.id)
    except Exception as e:
        LOGS.error(str(e))
    banned_msg = f"**تم الغاء حظرك من البوت يمكنك التواصل مع مالك البوت.**"
    if reason is not None:
        banned_msg += f"\n**السبب:** __{reason}__"
    await jmthon.tgbot.send_message(user.id, banned_msg)
    info = f"**#المستخدمين_غير_المحظورين**\
            \n\n👤 {_format.mentionuser(get_display_name(user) , user.id)}\
            \n**الأسم الاول:** {user.first_name}\
            \n**الايدي:** `{user.id}`"
    if BOTLOG:
        await jmthon.send_message(BOTLOG_CHATID, info)
    return info
