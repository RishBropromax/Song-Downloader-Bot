

#๐๐๐๐โค๐๐๐ฅ๐โ๐ค๐ป๐พ๐๐๐ก๐๐๐๐๐๐๐๐๐ก๐ฎโ๐ท๐ฑ๐ฒ๐โโ๐๐๐๐โโญ๐โ

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from Bot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Bot import Bot as app
from Bot import LOGGER

pm_start_text = """

๐ Hello [{}](tg://user?id={}),

I'm TG YT Music Downloader Bot
I have been created by **Emo Bot Developers** and **SDBOTS Infinity** to download Christmas Songs for you this Christmas.
โ Just send me the song name you want to download.๐

      eg:```/song Faded```

**๐ฅPowerd By - [</> ัะผฯ ะฒฯั โัฮฝฯโฯฯัสั](t.me/EmoBotDevolopers) & [SD Bots](t.me/SDBOTs_inifinity)**
**๐งโ๐ปDevoloper - @ImRishmika**

"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="โ๏ธโโโโโโMerry Christmasโโโโโโโ๏ธ", url="https://www.youtube.com/watch?v=XaJaztbTugo"
                    )
                ],
                  [
                     InlineKeyboardButton(
                        text="๐ฅัะผฯ ะฒฯั โัฮฝฯโฯฯัสั", url="https://t.me/EmoBotDevolopers"
                    ),
                    InlineKeyboardButton(
                        text="๐SD Bots", url="https://t.me/SDBOTS_Inifinity"
                    )
                ],
                 InlineKeyboardButton(
                        text="๐งโ๐ปOwner", url="https://t.me/ImRishmika"
                    )
                ],
                   InlineKeyboardButton(
                        text="๐ฅ Youtube ๐ฅ", url="https://youtube.com/@Rish_Bro"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

app.start()
LOGGER.info("โ Your Bot is Connected On Emo Network")
idle()
