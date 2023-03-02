from httplib2 import Http
from bot import LOGGER
from json import loads
from bot.config import Messages
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.config import BotCommands
@Client.on_message(filters.private & filters.incoming & filters.command(BotCommands.Start))
async def _auth(client, message):
  sent_message = await message.reply_text("🕵️**Checking received code...**", quote=True)
