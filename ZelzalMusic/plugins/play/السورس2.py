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
    command(["اللورد","المطور","لورد","عمك","مبرمج السورس","مستر لورد"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/3580afbb997b5d2fd8ca1.jpg",
        caption=f"""𝅄 𓏺 𝖭𝖺𝗆𝖾 : › 𝖬𝖱 𝖫𝖮𝖱𝖣
𝅄 𓏺 𝖴𝗌𝖾𝗋 : › @M_R_C2
𝅄 𓏺 𝖲𝗈𝗎𝗋𝖼𝖾 : › @M_R_ZC
𝅄 𓏺 𝖡𝗂𝗈 : ›𝖬𝗒 𝖡𝗋𝗈 : › « @MR_1X0 » 𓏺 « @P_O_C » 𓏺 « @M_Lr1 » ᯾ 𝖬𝗒 𝖶𝗈𝗋𝗅𝖽 : › «@OOOJ30»""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐋𝐨𝐫𝐝", url=f"https://t.me/M_R_C2"),
            ]
        ]
         ),
     )
  
