import re
import sys
import os
import time
import socket
import urllib3
import json
import os.path
import requests
from os import path
from concurrent.futures import ThreadPoolExecutor
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from httplib2 import Http
from bot import LOGGER
from json import loads
from bot.config import Messages
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.config import BotCommands
@Client.on_message(filters.private & filters.incoming & filters.command(BotCommands.Get))

async def getsk(client, message):
    chat_id = message.chat.id
    editable = await client.send_message(chat_id,f"SK Live  လိပ်စာများကိုထုတ်ယူနေပါသည်")
    if os.path.exists("SK_LIVE.TXT"):
        await client.send_document(chat_id, f"SK_LIVE.TXT")
        await client.send_document(chat_id, f"SK_ENV.TXT")
    else:
       await editable.edit("ဘာ SK မှ မတွေ့ပါ")