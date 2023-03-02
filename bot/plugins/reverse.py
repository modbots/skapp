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
class REV:
   def reverse(self, cidr, inpFile):
      total=""
      page = 0
      urx = f'https://rapiddns.io/s/{cidr}?full=1&down=1#result'
      try :
         r = requests.get(urx, verify=False, allow_redirects=False)
         resp = re.sub("<th scope=\"row \">.*",">>>>>>>>>>>>>>>>>>urx",r.text).replace ("<div style=\"margin: 0 8px;\">Total: <span style=\"color: #39cfca; \">","XP>>>>>>>>>>>>>").replace ("</span></div>","")
         urxc = resp.splitlines( )
         urls = ""
         nm = 0
         for xc in urxc:
            nm += 1
            if ">>>>>>>>>>>>>>>>>>urx" in xc:
               urls = urls+urxc[nm]+"\n"
         with open(os.path.join('', f'{inpFile}-ipv4.txt'), 'a') as output:
            output.write(f'{urls.replace("<td>","").replace ("</td>","")}')
         print(f"[SAVED] : {cidr}")
      except Exception as e:
         print(e)
@Client.on_message(filters.private & filters.incoming & filters.command(BotCommands.Reverse))

async def reverse(client, message):
  chat_id = message.chat.id

  rev = message.text.split()[-1]
  editable = await client.send_message(chat_id,f"သင်ပေးပို့လာသော {rev} မှ အင်တာနက် လိပ်စာများကိုထုတ်ယူနေပါသည်")
  threads = [1000]
  while(True):
      try:
         inpFile = rev
         with open(inpFile + ".txt") as urlList:
            argFile = urlList.read().splitlines()
         break
      except:
         pass
  for data in argFile:
      try:
        REV().reverse(data, inpFile)
        time.sleep(10)
        await editable.edit(f"{data} မှ အင်တာနက် လိပ်စာများကိုထုတ်ယူပြီးပါပြီ")
      except:
        pass

  await editable.edit(f"{rev} မှ အင်တာနက် လိပ်စာအားလုံးကိုထုတ်ယူပြီးပါပြီ")
 