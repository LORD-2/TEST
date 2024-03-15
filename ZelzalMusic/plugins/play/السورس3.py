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
        photo=f"https://graph.org/file/322c8079807064c5ca960.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪َِ⤹᧗َِᖇ˛ َِ⋆˛ َِ𝙓.˛ᯤ‌❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @MR_1X0❫
◉ 𝙲𝙷      : ❪ @T3_IG_AR_2 ❫
◉ 𝙱𝙸𝙾    : ❪ 【 https://telegra.ph/Mr-x-03-09-2】ᶠᵒʳ⤸ٰ.【 @M_R_1X_0 】 #ꪔy_ხᖇ᥆【 @M_R_C2 】【 @B_Og_3Y 】【 @T3_ig_3R 】. #ρ᥆ƚ_ꪔᥙ᥉【 @M8_SI_Xbot 】ᶠᵒʳ #ƒᥙᥴƙ_᥆ƒƒ • ❫""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "َِ⤹᧗َِᖇ˛ َِ⋆˛ َِ𝙓", url=f"https://t.me/MR_1X0"),
            ]
        ]
         ),
     )
  
