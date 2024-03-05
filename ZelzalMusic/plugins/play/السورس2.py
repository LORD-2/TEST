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
    command(["اللورد","المطور","لورد","عمك",])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/3580afbb997b5d2fd8ca1.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪ᗰᖇ ᒪOᖇᗪ❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @M_R_C2 ❫
◉ 𝙸𝙳      : ❪ 6443044496 ❫
◉ 𝙱𝙸𝙾    : ❪ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : @M_R_ZC • ❫""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐋𝐨𝐫𝐝", url=f"https://t.me/M_R_C2"),
            ]
        ]
         ),
     )
  
