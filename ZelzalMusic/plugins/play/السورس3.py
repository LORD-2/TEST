import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZelzalMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZelzalMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["اكس","مستر اكس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/062b500d6fcf955015633.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪َِ⤹᧗َِᖇ˛ َِ⋆˛ َِ𝙓.˛ᯤ‌❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @MR_1X0❫
◉ 𝙲𝙷      : ❪ @T3_IG_AR_2 ❫
◉ 𝙱𝙸𝙾    : ❪ ➤ᘜᴼᴰ ძᴼᴱˢ #ꪀᴼᵀ ძᴵˢᴬᴾᴾᴼᴵᴺᵀ ᴬ #᥉ᴱᴿⱽᴬᴺᵀ ᭙ᴴᴼ ᴵˢ #᥆ᴾᵀᴵᴹᴵˢᵀᴵᶜ ᥲᴮᴼᵁᵀ #ɦᴵᴹ َِ⤹🖤.⇣𓅛⁘ـــــَِ˛ َِ𝗫 .ـــــ⁘ #ꪔy ხᖇ᥆【 @M_R_C2 】 • ❫""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "َِ⤹᧗َِᖇ˛ َِ⋆˛ َِ𝙓", url=f"https://t.me/MR_1X0"),
            ]
        ]
         ),
     )
  
