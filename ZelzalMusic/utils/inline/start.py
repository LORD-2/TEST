#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ʑᴇʟᴢᴀʟ_ᴍᴜsɪᴄ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  T.me/ZThon   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ T.me/ZThon_Music ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

from pyrogram.types import InlineKeyboardButton

import config
from ZelzalMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url="https://t.me/M_r_zC"),
            InlineKeyboardButton(text=_["𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐒𝐨𝐮𝐫𝐜𝐞"], url="https://t.me/OOOJ30"),
        ],[
            InlineKeyboardButton(text=_["𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐋𝐨𝐫𝐝"], url="https://t.me/M_R_C2"),
        ],
        ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="zzzback")],
        [
            InlineKeyboardButton(text=_["S_B_6"], url="https://t.me/M_r_zC"),
            InlineKeyboardButton(text=_["𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐒𝐨𝐮𝐫𝐜𝐞"], url="https://t.me/OOOJ30"),
        ],[
            InlineKeyboardButton(text=_["𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐋𝐨𝐫𝐝"], url="https://t.me/M_R_C2"),
        ],
        ]
    return buttons
