#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ʑᴇʟᴢᴀʟ_ᴍᴜsɪᴄ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  T.me/ZThon   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ T.me/Zelzal_Music ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

from pyrogram.enums import ParseMode

from ZelzalMusic import app
from ZelzalMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>━━━━━━━━━━━━━━━<b>
<b> ◍ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗟𝗼𝗿𝗱 ◍ <b>
<b>━━━━━━━━━━━━━━━<b>
<b>🌹️ اسم المجموعة :<b> {message.chat.title} <code>[{message.chat.id}]</code>
<b>━━━━━━━━━━━━━━━<b>
<b>🥀 اسم المستخدم :<b> › {message.from_user.mention}
<b>━━━━━━━━━━━━━━━<b>
<b>🌸 يوزر المستخدم :<b> › @{message.from_user.username}
<b>━━━━━━━━━━━━━━━<b>
<b>🌷 ايدي المستخدم  :<b> › <code>{message.from_user.id}</code>
<b>━━━━━━━━━━━━━━━<b>
<b>🌿 رابط الجروب:<b> > @{message.chat.username}
<b>━━━━━━━━━━━━━━━<b>
<b>🌻 المطلوب:<b> {message.text.split(None, 1)[1]}
<b>━━━━━━━━━━━━━━━<b>
<b>💐 نوع التشغيل:<b> {streamtype}
<b>━━━━━━━━━━━━━━━<b>"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
