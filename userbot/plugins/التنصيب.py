from userbot.utils import admin_cmd


@borg.on(admin_cmd("التنصيب"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "مرحبا بـك عزيـزي** \n⌔︙ رابط التنصيب - [اضغط هنا](https://dashboard.heroku.com/new?template=https://github.com/ICETHON-AR/ICE-PACK/)\n⌔︙ قناة السورس - @ICE16"
        )
