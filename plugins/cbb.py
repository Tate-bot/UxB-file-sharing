# btn : about and close change here

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>ᴍɪᴋᴇʏ</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/tate_botX'>Channel</a>\n○ ᴍᴏᴠɪᴇs ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Tate_movie_group'>MovizTube</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/supptrt_group'>Chat</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "CLOSE ⚡️"),
                        InlineKeyboardButton('SOURCE CODE 🧑‍💻', url='https://t.me/+h3Y6dZqgL5A5NGE9')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
