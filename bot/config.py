import os
class config:
    BOT_TOKEN = "5845293690:AAHA0_BHSZsK2xWBQwyEGvaAQBq_sHk6ta4"
    APP_ID = "7810305"
    API_HASH = "2f25ab3cb4ea9708817581fbde570821"
    SUDO_USERS = "1844031429" # Sepearted by space.
    SUPPORT_CHAT_LINK = ""
    DOWNLOAD_DIRECTORY = "./downloads/"
    DATABASE_URL = ""

class BotCommands:
  Start = ['auth', 'Start']
  Asn = ['asn', 'Asn']
  Reverse = ['reverse', 'reverses']
  Env = ['env', 'Env']
  Get = ['get', 'Get']
  
class Messages:
    
    DOWNLOAD_TG_FILE  = "🔒 **DOWNLOADING CREDENIAL FILE.**"

    DOWNLOADED_SUCCESSFULLY = "🔒 **SUCCESSFULLY DOWNLOADED CREDENIAL FILE.**\n__Send /auth to authenticate.__"

    ALREADY_AUTH = "🔒 **Already authorized your Google Drive Account.**\n__Use /revoke to revoke the current account.__\n__Send me a direct link or File to Upload on Google Drive__"
   
    AUTH_SUCCESSFULLY = '🔐 **Authorized Google Drive account Successfully.**'
    
    INVALID_AUTH_CODE = '❗ **Invalid Code**\n__The code you have sent is invalid or already used before. Generate new one by the Authorization URL__'
    
    AUTH_TEXT = "⛓️ **To Authorize your Google Drive account visit this [URL]({}) and send the generated code here.**\n__Visit the URL > Allow permissions > you will get a code > copy it > Send it here__"
    
   