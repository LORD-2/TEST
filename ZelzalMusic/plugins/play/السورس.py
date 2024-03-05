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
        photo=f"https://graph.org/file/3580afbb997b5d2fd8ca1.jpg",
        caption=f"""╭۪ᰲ╍ׂ╌ׂ╍۪ᰲ╮╌ᰲ┄ׅ╍╌ᰲ┄ׅ╍╌ᰲ┄ׅ╍╌ᰲ┄ׅׅ╍╌ᰲ┄ׅׅ╍╌ᰲ╌ׅ╮
┊  💫    ꪝ𝖾𝗅𝖼𝗈𝗆𝖾  𝖨𝗇 𝖲𝗈𝗎𝗋𝖼𝖾 ♡ •. ❜ 
╰۫᷼╍ׅ╌ׅ╍۫᷼╯╌᷼┄۫╍╌᷼┄۫╍╌᷼┄۫╍╌᷼┄۫╍╌ᰲ┄ׅׅ╍╌᷼╌۫╯""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "✇ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐨𝐫𝐝 ✇", url=f"https://t.me/m_r_zc"),
                ],[
                    InlineKeyboardButton(
                        "𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐋𝐨𝐫𝐝", url=f"https://t.me/M_R_C2"),
                ],[
                    InlineKeyboardButton(
                        "𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐒𝐨𝐮𝐫𝐜𝐞", url=f"https://t.me/OOOJ30"),
                    InlineKeyboardButton(
                        "𝐆𝐫𝐨𝐮𝐩 𝐒𝐨𝐮𝐫𝐜𝐞", url=f"https://t.me/OOOJ30"),
                ],[
                    InlineKeyboardButton(
                        "✇ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ✇", url=f"https://t.me/{app.username}?startgroup=true"),
            ]
        ]
         ),
     )
  
