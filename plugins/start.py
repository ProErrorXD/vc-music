from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME as bn
from helpers.filters import other_filters2
from time import time
from datetime import datetime
from helpers.decorators import authorized_users_only
from config import BOT_USERNAME, ASSISTANT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**Hey, I'm {bn} ð
I Cá´É´ PÊá´Ê Má´sÉªá´ IÉ´ Yá´á´Ê GÊá´á´á´© Vá´Éªá´á´ CÊá´á´. Dá´á´ á´Êá´á´©á´á´ BÊ [ð ðð§ð-ððð¯](https://t.me/i_kishu).
Aá´á´ Má´ Tá´ Yá´á´Ê GÊá´á´á´© AÉ´á´ PÊá´Ê Má´sÉªá´ FÊá´á´ÊÊ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ðð¨ð¦ð¦ðð§ð ðð¢ð¬ð­ð§°", url="https://t.me/iv?url=http%3A%2F%2Fiv.iamidiotareyoutoo.com%2F18e34158fab943759a75f69edcb60b27_vTelegraphBot&rhash=c58a0d15a68464")
                  ],[
                    InlineKeyboardButton(
                       " ðð®ð©ð©ð¨ð«ð­ð¿", url="https://t.me/gana_Support"
                    ),
                    InlineKeyboardButton(
                        "ðð©ððð­ðð¬", url="https://t.me/gana_updates"
                    )
                ],[
                    InlineKeyboardButton(
                        "â ððð ðð ðð¨ ðð¨ð®ð« ðð«ð¨ð®ð©â",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )
