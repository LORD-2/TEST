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
    command(["سورس","المطور","لورد","السورس", "سورس لورد"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ba49699e0baee040f3737.jpg",
        caption=f"""╭──── • ◈ • ────╮
么 [َ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐨𝐫𝐝 ](https://t.me/m_r_zc)
么 [َ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐋𝐨𝐫𝐝 ](https://t.me/M_R_C2)
么 [َ 𝐆𝐫𝐨𝐮𝐩 𝐒𝐨𝐮𝐫𝐜𝐞 ](https://t.me/m_4_m_c)
么 [َ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ](https://t.me/OOOJ30)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "✇ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐨𝐫𝐝 ✇", url=f"https://t.me/m_r_zc"),
                ],[
                    InlineKeyboardButton(
                        "𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐋𝐨𝐫𝐝", url=f"https://t.me/M_R_C2"), 
                    InlineKeyboardButton(
                        "𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐒𝐨𝐮𝐫𝐜𝐞", url=f"https://t.me/OOOJ30"),
                ],[
                    InlineKeyboardButton(
                        "✇ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ✇", url=f"https://t.me/M_R_Z4BOT?startgroup=true"),
            ]
        ]
         ),
     )
  
