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

class ASN :
   def scan (self, asn):
      str = "";
      try:
         r = requests.get(f'https://api.bgpview.io/asn/{asn}/prefixes', verify=False, timeout=10, allow_redirects=False)
         resp = r.text
         rn = ""
         obj = json.loads(resp)
         obj2 = json.dumps(obj["data"])
         obj3 = json.loads(obj2)
         obj4 = json.dumps(obj3["ipv4_prefixes"])
         oc = re.sub(".*\"prefix\":\"","prefix::",obj4.replace("{",""). replace ("}","").replace("[",""). replace ("]","").replace(",","\n"). replace (" ","")). replace ("\"","")
         cv = oc.splitlines()
         for cn in cv:
            if "prefix::" in cn :
               rn = rn+cn+"\n"
         sasn = rn.replace("prefix::","")
         with open(os.path.join('', f'{asn}.txt'), 'a', encoding='utf-8') as output:
            output.write(f'{sasn}')
         print(f"ASN : {asn}")
      except Exception as e :
            print(f"ERROR : {e}")

@Client.on_message(filters.private & filters.incoming & filters.command(BotCommands.Asn))

async def asn(client, message):
  chat_id = message.chat.id

  asn = message.text.split()[-1]
  editable = await client.send_message(chat_id,f"သင်ပေးပို့လာသော {asn} မှ ipv4 လိပ်စာများကိုထုတ်ယူနေပါသည်")
  threads = [1000]
  #data = "AS26496"
  with ThreadPoolExecutor(max_workers=1000) as executor:
    threads.append(executor.submit(ASN().scan, asn))

  await client.send_document(chat_id, f"{asn}.txt")
  await editable.edit(f"{asn} မှ ipv4 လိပ်စာများကိုထုတ်ယူပြီးပါပြီ")