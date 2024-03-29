# Copyright (C) 2021 ICE16 TEAM
# FILES WRITTEN BY  @ICE50

import io
import sys
import traceback

from . import ICE16, edit_or_reply

plugin_category = "utils"


@ICE16.ar_cmd(
    pattern="حساب ([\s\S]*)",
    command=("حساب", plugin_category),
    info={
        "header": "To solve basic mathematics equations.",
        "description": "Solves the given maths equation by BODMAS rule.",
        "usage": "{tr}calc 2+9",
    },
)
async def calculator(event):
    "To solve basic mathematics equations."
    cmd = event.text.split(" ", maxsplit=1)[1]
    event = await edit_or_reply(event, "⌔︙ يتـم الـحساب أنتـظر قـليلا")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    san = f"print({cmd})"
    try:
        await aexec(san, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "⌔︙ عـذرا لأ اسـتطيع ايجـاد حـل لهـكذا معـادلات"
    final_output = "⌔︙ السـؤال: `{}` \n\n ⌔︙ الـحل: \n`{}` \n".format(cmd, evaluation)
    await event.edit(final_output)


async def aexec(code, event):
    exec(f"async def __aexec(event): " + "".join(f"\n {l}" for l in code.split("\n")))
    return await locals()["__aexec"](event)
