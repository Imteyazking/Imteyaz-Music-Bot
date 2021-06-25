from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAANtYNSn-I7nk-0lQBhveIbeiARhnXUAAnsFAAJxW5BWCWy-W5gXdSkfBA")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can [play music](https://telegra.ph/file/5e25cfa7dfd7a628a9139.jpg) in your group's voice call. Developed by [Imteyaz_king For Telegram voice chat's](https://t.me/Imteyaz_support).

Add me and my assistant to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡ Add Music Bot in Your Group ⚡", url="t.me/KING_FIGHTER_MUSIC_BOT?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/King_fighter_Bot_support"
                    ),
                    InlineKeyboardButton(
                        "♥️ Music bot Assistant", url="t.me/KING_FIGHTER_MUSIC_ASSISTANT"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Help", url="https://telegra.ph/KING-FIGHTER--VC-MUSIC-06-21-2"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨𝑪𝒓𝒆𝒂𝒕𝒐𝒓✨", url="https://t.me/Imteyaz_king")
                ]
            ]
        )
   )


