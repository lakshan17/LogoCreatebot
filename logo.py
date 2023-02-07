from pyrogram import filters, Client
from pyrogram.types import Message
from requests import get
import os
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.environ.get("API_ID",10432339))
API_HASH = os.environ.get("API_HASH","a6d7561a8ed9f505a47672c6bd8a2426")
BOT_TOKEN = os.environ.get("BOT_TOKEN",5494032967:AAEKl5p5xY9XgWPMWn3spx2Q9hKcN4UoXMI")

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
async def start(client, message):
   if message.chat.type == 'private':
       await logo.send_message(
               chat_id=message.chat.id,
               text.format(message.from_user.mention)="""<b>Hey👋 {} , I'm Logo Create Bot

🎨I Can Create A Logo , 4k Logo

Hit help button to find out more about how to use me</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Help", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Channel", url="https://t.me/Lakshan_Pathum")
                                    ],[
                                      InlineKeyboardButton(
                                            "Source Code", url="https://github.com/lakshan17/LogoCreatebot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@logo.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await logo.send_message(
               chat_id=message.chat.id,
               text="""<b>☘️ Help Commands

🔸Use /logo - Make Random Logo In Your Text
🔸Use /logohq - Make 4k Logo In Your Text

🔸Use /write - Write To Your Text

  ⚜This Commands Useing The Make Your Logo</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back ⬅", callback_data="start"),
                                        InlineKeyboardButton(
                                            "About ❕", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "Source Code 📦", url="https://github.com/https://github.com/lakshan17/LogoCreatebot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@logo.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await logo.send_message(
               chat_id=message.chat.id,
               text="""<b>--**About Me**-- 😎

🤖 **Name :** [Logo Create Bot](https://t.me/{})

👨‍💻 **Developer :** [Lakshan](https://github.com/lakshan17)

📢 **Channel :** [Lakshan Pathum](https://t.me/Lakshan_Pathum)

☎️**Contact Me :** [Assistant Bot](https://t.me/Lakshan_Pathum_Bot)

📝 **Language :** [Python3](https://python.org)

📕 **Library :** [Pyrogram](https://pyrogram.org)

🛠️ **Logo Creater Api :** [SingleDevelopers](https://t.me/SingleDevelopers)

📡 **Server :** [Heroku](https://heroku.com)</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back ⬅", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Source Code 📦", url="https://github.com/https://github.com/lakshan17/LogoCreatebot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")
            
  
#◇───────────────────────────────────────◇ 

@logo.on_message(filters.command("logo"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://api.single-developers.software/logo?name={text}").history[1].url
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
    photo = get(f"https://api.single-developers.software/wallpaper?search={text}").history[1].url
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
    
@logo.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)
        
        
        
logo.run()

logo.start()
print("Bot Start ✅")
