#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ʑᴇʟᴢᴀʟ_ᴍᴜsɪᴄ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  T.me/ZThon   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ T.me/ZThon_Music ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

from pyrogram.types import InlineKeyboardButton

import config
from ZelzalMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["ZTHON_BUTTON3"],
                url=f"https://t.me/M_R_C2",
            )
        ],
        [
            InlineKeyboardButton(text=_["ZTHON_BUTTON"], url="https://t.me/OOOJ30"),
            InlineKeyboardButton(text=_["ZTHON_BUTTON2"], url="https://t.me/T3_ig_3R"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_1"], url="https://t.me/{app.username}?startgroup=true"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["ZTHON_BUTTON3"],
                url=f"https://t.me/M_R_C2",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="zzzback")],
        [
            InlineKeyboardButton(text=_["ZTHON_BUTTON"], url="https://t.me/OOOJ30"),
            InlineKeyboardButton(text=_["ZTHON_BUTTON2"], url="https://t.me/T3_ig_3R"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_1"], url="https://t.me/{app.username}?startgroup=true"),
        ],
    ]
    return buttons
