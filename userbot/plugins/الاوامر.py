from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio

ICE50 = ("الامر 1")
CATAR = ("الامر 2")
ICE50 = ("الامر 3")  

@borg.on(admin_cmd("الاوامر"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("• اوامـر سـورس آيس ثون\n• هذه هي قائمة اوامر البوت الخاصة بك \n• تستـطيع من هـنا رؤيـة جميع اوامر الـبوت .\n\n ⦏  اوامر ، الكتم والحظر ارسل  ⇦ `.الامر 1` ⦐ \n ⦏  اوامر ، المجموعة ارسل  ⇦ `.الامر 2` ⦐ \n ⦏  اوامر ، الترحيب ارسل  ⇦ `.الامر 3` ⦐ \n ⦏  اوامر ، اضافة الردود ارسل  ⇦ `.م4` ⦐ \n ⦏  اوامر ، حماية الخاص ارسل  ⇦ `.م5` ⦐ \n ⦏  اوامر ، التلكراف ارسل  ⇦ `.م6` ⦐ \n ⦏  اوامر ، القفل ارسل  ⇦ `.م7` ⦐ \n ⦏  اوامر ، المنشن ارسل  ⇦ `.م8` ⦐ \n ⦏  اوامر ، الانتحال ارسل  ⇦ `.م9` ⦐ \n ⦏  اوامر ، تحويل الصيغ ارسل  ⇦ `.م10` ⦐ \n ⦏  اوامر ، الترجمه ارسل  ⇦ `.م11` ⦐ \n ⦏  اوامر ، البحث والتحميل ارسل  ⇦ `.م12` ⦐ \n ⦏  اوامر ، المجمـوعة ارسل  ⇦ `.م13` ⦐\n ⦏  اوامر ، التشغيل ارسل  ⇦ `.م14` ⦐ \n ⦏  اوامر ، المنع ارسل  ⇦ `.م15` ⦐ \n ⦏  اوامر ، التسلية ارسل  ⇦ `.م16` ⦐ \n ⦏  اوامر ، التنظيف والمسح   ⇦ `.م17` ⦐ \n ⦏  اوامر ، الحساب الوقتي ارسل  ⇦ `.م18` ⦐ \n ⦏  اوامر ، هيروكو والفار ارسل  ⇦ `.م19` ⦐ \n ⦏  اوامر ، الارسال ارسل  ⇦ `.م20` ⦐ \n ⦏  لا شي هنا ⇦ `.م21` ⦐ \n ⦏  اوامر ، الملصقات ارسل  ⇦ `.م22` ⦐ \n ⦏  اوامر ، المساعده ارسل  ⇦ `.م23` ⦐ \n ⦏  اوامر ، الروابط ارسل  ⇦ `.م24` ⦐ \n ⦏  اوامر ، التخصيص ارسل  ⇦ `.م25` ⦐ \n ⦏  اوامر ، التكرار والسبام ارسل  ⇦ `.م26` ⦐ \n ⦏  اوامر ، آيس او وهمسة ارسل  ⇦ `.م27` ⦐ \n\n⌔︙ CH - @ICE16 ")

@borg.on(admin_cmd(ICE50))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ امر الادمن للحظر والطرد\n\n⌔︙الاستخدام   :  `.كتم`  <بالرد/معرفه/ايدي>\n ⌔︙الامر  : يقوم بكتم الشخص في مجموعه معينه ويمنعه من ارسال الرسائل\n\n ⌔︙الاستخدام  :  `.الغاء كتم`  <بالرد/معرفه/ايدي>\n⌔︙الامر  :  الغاء كتم الشخص والسماح له بالتحدث بِحريـة\n\n ⌔︙ الامر :  `.حظر` <بالرد/معرفه/ايدي>\n ⌔︙الاستخدام    :  لحـظر شخص في مجمـوعة معـينة وعدم السماح له بالـدخول مجـددا\n\n⌔︙ الامر   :  `.الغاء حظر`  <بالرد/معرفه/ايدي> \n⌔︙ الاستخدام  : يقوم بالغاء حظر الشخص في المجموعه والسماح له بالدخول مجددا \n\n⌔︙ الامر  :  `.طرد` <بالرد/معرفه/ايدي> \n⌔︙ الاستخدام  : يقوم بطرد شخص من المجموعه والسماح لهد بالدخول مجددا \n\n ⌔︙الامر  :  `.كتم_مؤقت`  + الوقت \n⌔︙ الاستخدام  :  لكتم شخص مؤقتا في مجموعه معينه و تقييده\n\n ⌔︙ الاضافة  : \n⌔︙ لكتم الشخص بالدقائق اكتب مع الامر  m والوقت \n⌔︙ لكتم الشخص بالثواني اكتب مع الامر  s والوقت\n ⌔︙ لكتم الشخص بالساعات اكتب مع الامر  h والوقت\n\n⌔︙ مثال  :  `.كتم_مؤقت 5h` لكتمه 5 ساعات مؤقتا\n\n⌔︙الامر  :  `.حظر_مؤقت`  + الوقت\n⌔︙الاستخدام  :  لحظر شخص مؤقتا من المجموعه والسماح له بالدخول بعد انتهاء الوقت \n⌔︙الاضافة  :  كما في الكتم المؤقت\n\n⌔︙ قـناة السورس  :  \n@ICE16")
        
@borg.on(admin_cmd(CATAR))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامر المجموعه\n\n⌔︙الاستخدام   :  `.رفع مشرف`  <بالرد/معرفه/ايدي>\n ⌔︙الامر  : يقوم برفع شخص مع صلاحيات الحظر والحذف وغيرها في المجموعه\n\n⌔︙الاستخدام  :  `.تك` <بالرد/معرفه/ايدي>\n ⌔︙الامر  :  تنزيل الشخص من صلاحيات الاشراف في المجموعه\n\n ⌔︙ الامر :  `.تثبيت`  <بالرد على الرسالة>\n ⌔︙الاستخدام  :  لتثـبيت رسـالة في مجموعة معينة\n\n ⌔︙الامر  :  `.الاحداث` \n⌔︙ الاستخدام  : يقوم بعرض احداث المجموعه تحتاج صلاحيات \n ⌔︙ الاستخدام²  : `.الاحداث -ر`  + عدد رسائل بين 0-15\n ⌔︙الأمر:  ليقوم بعرض الرسائل والرد عليك رسالة رسالة\n\n ⌔︙.الامر  :  `.ضع تكرار  + عدد التكرار`\n ⌔︙ الاستخدام  : يقوم بوضع تكرار في الكروب واذا شخص تجاوز التكرار يقيده\n⌔︙ولالغاء التكرار ارسل  `.ضع تكرار 999999`\n\n\n⌔︙الامر  :  `.الغاء التثبيت`  <للكل>\n⌔︙الاستخدام  :  لالغاء تثبيت رسالة في الكروب ويستخدم مع للكل لالغاء تثبيت جميع الرسائل\n\nالسورس  :  \n@ICE16")
        
@borg.on(admin_cmd(ICE50))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامر الترحيب\n\n ⌔︙ الاستخدام   :  .ترحيب <ترحيبك>\n⌔︙ الامر  : يقوم بالترحيب بالمستخدمين الجدد في مجموعتك فقط ارسل الامر في المجموعة\n⌔︙ مثـال :  .ترحيب ههـلـو عـمـري ♥َ🦋ِ . \n\n⌔︙ الامر  :  .حذف ترحيب <الترحيب>\n⌔︙ الاستخدام  :  لحذف ترحيب معين من المجموعه فقط اكتب الامر والترحيب\n⌔︙ مثال : .حذف ترحيب  ههـلـو عـمـري ♥َ🦋\n\n ⌔︙ الامر : .حذف الترحيبات \n ⌔︙ الاستخدام  :  فقط اكتب الامر ليقوم بحذف جميع الترحيبات في المجموعه\n⌔︙ الامر : `.الترحيب السابق تشغيل`\n ⌔︙ الاستخدام  :  إذا كنت ترغب في حذف رسالة الترحيب السابقة وإرسال رسالة ترحيب جديدة ، فقم بتشغيلها \n⌔︙ ملاحـظة  : اذا حدث تـكرار في الـترحيب قم بحذف الترحيب واضافته مجددا\n\n⌔︙ السورس  :  \n⌔︙ @ICE16")
        
@borg.on(admin_cmd("م4"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامر اضافة الردود\n\n⌔︙ الاستخدام   :  .اضف رد  <ردك>\n⌔︙ الامر  : يقوم بحفظ رد في مجموعه معينه  اكتب الامر والرد شاهد شرح\n⌔︙   ︙ الاستخدام  :  .حذف رد <الرد الذي اضفته>\n⌔︙ الامر  :  يقوم بحذف الرد الذي اضفته اكتب الامر مع ردك \n\n⌔︙ الامر :  .الردود \n⌔︙ الاستخدام  :  لعـرض قائمة ردود مجموعه معينة \n\n⌔︙ الامر  :  .حذف الردود\n⌔︙ الاستخدام  : يقوم بحذف جميع الردود التي اضفتها في مجموعه معينه\n\nالسورس  :  \n @ICE16")
                
@borg.on(admin_cmd("م5"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(" ⌔︙ اوامر حماية الخاص\n\n⌔︙ الاستخدام   :  .الحماية  on\n⌔︙ الامر  : يقوم بتفعيل ميزه حمايه الخاص التي تقوم بتحذير شخص من ارسال رسائل وحظره اذا تجاوز عدد 6 رسائل \n\n⌔︙ الامر  :  .الحماية off\n⌔︙ الاستخدام  :   يقوم بتعطيل امر حماية الخاص والغاؤها فقط ارسل الامر\n\n⌔︙ الامر :  .سماح  او  .س\n ⌔︙ الاستخدام  :  للموافقه على الشخص وجعله يتكلم بحرية في الخاص \n\n⌔︙ الامر  :  .رفض  او  .ر\n⌔︙ الاستخدام  : يقوم برفض الشخص من الخاص واذا كرر سيتم حظره تلقائيا\n\n⌔︙ الامر :  .بلوك <السبب>  <بالرد>\n⌔︙ الاستخدام  : بالرد على الشخص لحظره من الخاص يمكنك فك الحظر يدوي \n\n⌔︙ الامر :  .انبلوك  <بالرد>\n ⌔︙ الاستخدام :   يستخدم هذا الامر لالغاء حظر شخص من الخاص فقط قم بالرد عليه \n\n⌔︙ الامر :  .المسموح لهم\n⌔︙ الاستخدام  : يقوم بأرسال ملف يتضمن  قائمه الاشخاص الذي تم الموافقة عليهم والذي تم رفضهم من الخاص\n\n⌔︙ قـناة السـورس  :\n@ICE16")
                
@borg.on(admin_cmd("م6"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامر تحويل التلكراف \n\n⌔︙ الامر  :  .تلكراف t\n⌔︙ الاستخدام :  ليقوم بصنع رابط تلكراف لمقالة او موضوع معين او نص \n⌔︙ الشرح  :  قم بالرد على النص المراد تحويله الى رابط تلكراف\n\n⌔︙ الامر  :  .تلكراف m \n⌔︙ الاستخدام  :  ليقوم بصنع رابط تلكراف لصورة او فيديو او متحركه\n⌔︙ الشرح  :  قم بالرد على الصورة المراد تحويلها الى رابط تلكراف\n\n⌔︙ قـناة السورس  : \n ⌔︙ @ICE16")
                
@borg.on(admin_cmd("م7"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامر صلاحيـات المجموعه \n\n⌔︙ الامر  :   .قفل <الاضافة> \n⌔︙ الاستخدام  :  تكتب الامر مع الاضافة لقفل شي معين في المجموعة\n\n ⌔︙ الامر  :   .فتح <الاضافة> \n⌔︙ الاستخدام  :  تكتب الامر مع الاضافة لقتح شي معين في المجموعة\n\n⌔︙ الاضافة  :  \n ⌔︙ الدردشه  : لقفل ارسال الرسائل \n⌔︙ الوسائط   : لقفل ارسال الوسائط\n ⌔︙ الملصقات  : لقفل ارسال الملصقات\n⌔︙ الروابط  : لقفل ارسال الروابط\n⌔︙ المتحركه  : لقفل ارسال المتحركه\n⌔︙ الالعاب  : لقفل ارسال الالعاب الانلاين\n⌔︙ الانلاين  : لقفل ارسال البوتات الانلاين\n⌔︙ التصويت  : لقفل ارسال التوصيتات \n⌔︙ الكل :  لقفل ارسال كل شي\n\n⌔︙ قـناة السورس  : \n⌔︙ @ICE16")
                
@borg.on(admin_cmd("م8"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامر التاك والمنشن \n\n⌔︙ الامر  :  .تاك <معرف الشخص>  <الرسالة> \n⌔︙ الاستخدام  :  لعمل تاك لشخص ووضع التاك داخل الرسالة شاهد المثال وجرب بنفسك\n⌔︙ مثال :  .تاك @ICE16  ههلا\n\n⌔︙.للكل  <النص> \n⌔︙ الاستخدام  :  لعمل تاك لجميع الاعضاء بالرسالة\n⌔︙ مثال  :   .للكل هلا\n\n⌔︙ الامر  :  .ابلاغ \n⌔︙ الاستخدام  :  لابلاغ المشرفين اذا ما حصل شي ما\n\n⌔︙ اوامـر الكشف والايدي\n\n⌔︙ الامر  :  .الايدي  <بالرد/المعرف>\n⌔︙ الاستخدام  :  لاظهار ايدي الشخص و المجموعه فقط قم بالرد على الشخص او وضع معرفه\n\n⌔︙ .ايدي <بالرد/معرف/ايدي> \n⌔︙ الاستخدام  :  يقوم باظهار معلومات عن الشخص\n\n⌔︙ الامر  :  .كشف  <بالرد/معرف/ايدي>  \n⌔︙ الاستخدام : لعرض معلومات الشخص بسكل مبسط\n\n⌔︙ الامر  :  .رابط الحساب  <بالرد/معرف/ايدي> \n⌔︙ الاستخدام:  للحصول على رابط حساب الشخص\n\n⌔︙ السورس  : \n⌔︙ @ICE16")

@borg.on(admin_cmd("م9"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامـر التقلـيد والانتحـال\n\n⌔︙ الأمـر  :  `.انتحال`  <بالرد/معرف/ايدي> \n⌔︙ الاستـخدام :  الانتحال شخص ونسخ حساب الشخص بالكامل من صورة اسم وبايو..... والخ \n\n⌔︙ الأمـر  :  `.اعادة`\n ⌔︙ الاستـخدام : لاعادة حسـابك الى وضـعه الطبيعـي\n\n ⌔︙ اوامـر التقليـد\n ⌔︙ الأمـر  :   `.تقليد` <بالرد/معرف/ايدي> \n ⌔︙ الاستـخدام : يستخدم هذا الامر ليقوم بتكرار جميع رسائل الشخص الذي فعلت عليه الامر\n ⌔︙ الأمـر  :   `.الغاء التقليد` \n ⌔︙ الاستـخدام : لالغاء تقليد الشخص وعدم ارسال رسائله\n\n⌔︙ الأمـر  :  `.المقلدهم`\n⌔︙ الاستـخدام : فقط اكتب الامر ليقوم بعرض الاشخاص الي تم تقليدهم\n\n⌔︙ قـناة الـسورس  :  @ICE16")
        
@borg.on(admin_cmd("م10"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامر تحويل الصيغ\n\n⌔︙ الامـر • .تحويل صورة  <بالرد>\n⌔︙ الاستـخدام  • الرد على الملصق لتحويله صورة \n\n⌔︙ الامـر  •  .تحويل ملصق  <بالرد>\n⌔︙ الاستـخدام •  بالرد على الصورة لتحويله ملصق \n\n⌔︙ الامـر  •  .تحويل متحركة  <بالرد>\n⌔︙ الاستـخدام  • بالرد على الفيـيديو لتحويله متحركه \n\n⌔︙ الامـر  •  .تحويل voice  <بالرد>\n⌔︙ الاستـخدام  • بالرد على الاغنيه لتحويلها على شكل بصمة \n\n⌔︙ الامـر  •  .تحويل mp3  <بالرد>\n⌔︙ الاستـخدام  • بالرد على البصمه او المقطع الصوتي لتحويله على شكل اغنية \n\n⌔︙ CH  -  @ICE16")

@borg.on(admin_cmd("م11"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامر الترجمه والتكلم الصوتي\n\n⌔︙ الامر  :  .ترجمه ar\n⌔︙ الاستخدام:  بالرد على النص لترجمته للغه العربية \n\n⌔︙ الامر  :   .ترجمه en\n⌔︙ الاستخدام :  بالرد على النص لترجمته للغه الانكليزية\n\n⌔︙ الامر  :   .تكلم ar\n⌔︙ الاستخدام  :  يقوم بتسجيل الكتابه باللغه العربيه وارسالها على شكل بصمه صوتية\n\n⌔︙ الامر  :   .تكلم en\n⌔︙ الاستخدام  :  يقوم بتسجيل الكتابه باللغه الانكليزية وارسالها على شكل بصمه صوتية\n\n⌔︙ السورس  :  \n⌔︙ @ICE16")

@borg.on(admin_cmd("م12"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامر البحث والتحميل  \n\n⌔︙ الامر  • `.بحث`  <اسم اغنيه>\n⌔︙ الاستخدام • بكتابة اسم الاغنية مع الامر لارسال الاغنيه مباشرا واذا ما اشتغل جرب اوامر التحميل الاخرى\n\n⌔︙ الامر  • `.يوت`  <اسم الفيديو او  اغنية>\n⌔︙ الاستخدام • كتابة الامر مع اسم الفيديو او الاغنية ليعطيك نتائج البحث وروابط من يوتيوب تستخدم مع اوامر التحميل\n\n⌔︙ الامر • `.تحميل ص`  <رابط اغنية>\n⌔︙ استخدامه • لتحميل اغنيه من خلال وضع الرابط مع الامر\n\n⌔︙ الامر • `.تحميل ف ` <رابط فيديو>\n⌔︙ استخدامه • كتابة الامر مع رابط المقطع لتحميله وارساله لك\n\n⌔︙ الامر • `.انستا`  <رابط>\n⌔︙ استخدامه • يستخدم هذا الامر لتحميل من الانستا فقط اكتب الامر مع رابط الفيديو ليحمله\n\n⌔︙ CH  :  @ICE16")

@borg.on(admin_cmd("م13"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**⌔︙ اوامر المجمـوعة**\n\n⌔︙ الامر  • `.معلومات`  <معرف المجموعة>\n⌔︙ الاستخدام  • ارسال الامر في المجموعه لرؤية معلومات المجموعه او اكتب الامر مع معرف المجموعة\n\n⌔︙ الامر  • `.البوتات` <معرف المجموعه>\n⌔︙ الاستخدام • ارسل الامر لرؤية البوتات الموجوده في المجموعه او اكتب الامر مع معرف الكروب\n\n⌔︙ الامر  •  `.المشرفين` <معرف المجموعه>\n⌔︙ الاستخدام  • كتابة الامر فقط في المجموعه لرؤية مشرفين الكروب  او اكتب الامر مع معرف الكروب\n\n⌔︙ الامر  •  `.الاعضاء` <معرف المجموعه>\n⌔︙ الاستخدام  • كتابة الامر فقط لرؤية معرفات اعضاء الكروب  او اكتب الامر مع معرف الكروب\n\n⌔︙ الامـر  • `.اطردني` \n⌔︙ الاستـخدام  • فقـط ارسل الامر في المجموعة لمغادرة المجموعه التي تم ارسال الامر فيها\n\n⌔︙ الامـر  • `.تفليش بالطرد` \n ⌔︙ الاستـخدام • ارسل  الامـر لطرد جميع الاعضاء من المجموعه\n\n⌔︙ الامـر  •  `.تفليش بالحظر` \n⌔︙ الاستـخدام  • كتابة  الامـر فقط في المجموعه لحظر جميع الاعضاء \n\n⌔︙ الامـر  •  `.حذف المحظورين`\n⌔︙ الاستـخدام  • كتابة  الامـر في الكروب لالغاء حظر جميع الاعضاء\n\n⌔︙ الامـر • .المحذوفين \n⌔︙ الاستـخدام • لعرض الحسابات المحذوفة في مجمـوعة معيـنة ولحذفهم ارسل `.المحذوفين اطردهم`\n\n⌔︙ الامر  • `.احصائيات الاعضاء`\n ⌔︙ الاستخدام  • فقط ارسل الامر لرؤية احصائيات الاعضاء في الكروب\n\n⌔︙ CH :  @ICE16")
