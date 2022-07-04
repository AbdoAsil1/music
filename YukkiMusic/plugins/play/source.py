import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")


@app.on_message(
    command(["سورس زيرو","سورس","السورس","يا سورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/dbb2278bb834ad830c1ac.jpg",
        caption=f"""[WelCoMe To SoUrCe ZerO 🌐](https://t.me/XTIORY)\n\n[ThE BesT SoUrCe oN TelEGrAM 🌐](https://t.me/XTIORY)\n\n[ FoLLOw ThE BuTtOns BeLoW ⚡️](https://t.me/XTIORY)\n\n||[𝗔𝗕𝗗𝗢 𝗔𝗦𝗜𝗟 - ســـــــــيزر](https://t.me/ttccss)||""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗔𝗕𝗗𝗢 𝗔𝗦𝗜𝗟 - ســـــــــيزر", url=f"https://t.me/ttccss"), 
                ],[
                    InlineKeyboardButton(
                        "• 𝙎𝙊𝙐𝙍𝘾𝙀 𝙕𝙀𝙍𝙊 •⚡️", url=f"https://t.me/XTIORY"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك✅.", url=f"https://t.me/Rep0obot?startgroup=true"),
                ],

            ]

        ),

    )
