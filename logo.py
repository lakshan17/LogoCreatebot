from pyrogram import filters, Client
from pyrogram.types import Message
from requests import get
import os
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

logo = Client("logo Bot", bot_token = BOT_TOKEN, api_id = API_ID, api_hash = API_HASH)


caption = """
✍️ Logo Created Successfully✅

◇───────────────◇

🚀 **Created By** : **[LOGO CREATE BOT 🔅](https://t.me/TG_Logo_Create_bot)**

🌺 **Requestor** : ** {} **


◇───────────────◇️  
    """
#◇───────────────────────────────────────◇ 

#◇───────────────────────────────────────◇ 

@logo.on_message(filters.command("start"))
async def start(client,message):
    await message.reply_chat_action("typing")
    await message.reply("🍀 Hi I am Logo Create Bot Telegram...")

    
@logo.on_message(filters.command("help"))
async def help(client,message):
    await message.reply_chat_action("typing")
    await message.reply("☘️ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅꜱ

 🔸/start- ꜱᴛᴀʀᴛ ʙᴏᴛ.

 🔸 ᴜsᴇ /write - ᴡʀɪᴛᴇ ᴛᴏ ʏᴏᴜʀ ᴛᴇxᴛ

 🔸 ᴜsᴇ /logo - ᴍᴀᴋᴇ ʀᴏɴᴅᴏᴍ ʟᴏɢᴏ ɪɴ ʏᴏᴜʀ ᴛᴇxᴛ

 🔸 ᴜsᴇ /logohq - ᴍᴀᴋᴇ 4ᴋ ʟᴏɢᴏ ɪɴ ʏᴏᴜʀ ᴛᴇxᴛ

 🔸 ᴜsᴇ /glogo - ᴍᴀᴋᴇ ɢʜᴏꜱᴛɪꜱᴛ ʟᴏɢᴏ ɪɴ ʏᴏᴜʀ ᴛᴇxᴛ")

#◇───────────────────────────────────────◇ 

@logo.on_message(filters.command("logo"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://host.single-developers.software/logo?name={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await logo.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍀 Open In Google 🍀", url=f"{photo}"
                    )
                ]
            ]
          ),
    )

#◇────────────────────────────────────◇ 
  
@logo.on_message(filters.command("logohq"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://host.single-developers.software/logohq?name={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await logo.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍀 Open In Google 🍀", url=f"{photo}"
                    )
                ]
            ]
          ),
    )

#◇──────────────────────────────────────◇ 


@logo.on_message(filters.command("wall"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://host.single-developers.software/wallpaper?search={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await logo.send_photo(message.chat.id, photo=photo, caption=caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍀 Open In Google 🍀", url=f"{photo}"
                    )
                ]
            ]
          ),
    )


logo.run()

logo.start()
LOGGER.info("Bot Work Now")
idle()
