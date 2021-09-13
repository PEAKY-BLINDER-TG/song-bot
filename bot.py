import os
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

bot = Client(
  "message-bot",
  bot_token="11952122501:AAH-Ig7MeRdvrmoM4l_76Q9Jn6ck3LqOiM4",
  api_id="3020564",
  api_hash="91c026fadfdc442f504a0bd3e5c8cd18",
  )
  
  @bot.on_message(filters.command(['start']))
  def start (Client, message):
    message.reply(f"hey bruhh how are you)",
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton("owner" url="https://t.me/XXXTENTACION_TG"),
          InlineKeyboardButton("GROUP" url="https://t.me/XXXTENTACION_TG")
        ],
        [
          InlineKeyboardButton("CHANNEL" url="https://t.me/XXXTENTACION_TG")
        ]
      ]
      )
      
bot.run()   