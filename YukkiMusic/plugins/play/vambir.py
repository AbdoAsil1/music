import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["مبرمج السورس","سيزر","المبرمج"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/64517838feecdab936379.jpg",
        caption=f"""◍ الزرار الاول: قناه السورس \n◍ الزرار الثاني: هو مبرمج السورس\n√""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "• 𝙎𝙊𝙐𝙍𝘾𝙀 𝙕𝙀𝙍𝙊 •⚡️", url=f"https://t.me/XTIORY"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "𝗔𝗕𝗗𝗢 𝗔𝗦𝗜𝗟 - ســـــــــيزر", url=f"https://t.me/ttccss"),
                ],
            ]
        ),
    )


@app.on_message(
     command(["مطور السورس","جيكا","المطور"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/91f4c5688d1634741cf90.jpg",
        caption=f"""◍ الزرار الاول: قناه السورس \n◍ الزرار الثاني: هو مطور السورس\n√""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "• 𝙎𝙊𝙐𝙍𝘾𝙀 𝙕𝙀𝙍𝙊 •⚡️", url=f"https://t.me/XTIORY"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "𓆩🖤𓆪 ᎫᎬᏦᎪ ✶ ٖوِٰحَٖــَ͜ـٰـٖـެيـِٚـٰٚــٖ͜ـٰد 𓆩🖤𓆪", url=f"https://t.me/DevJeka"),
                ],
            ]
        ),
    )
