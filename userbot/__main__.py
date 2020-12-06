import os
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterDocument

from userbot import bot
from userbot.utils import load_module, start_assistant
from var import Var, sh1vam
Hehe = sh1vam

LOAD_USERBOT = os.environ.get("LOAD_USERBOT", True)
LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)    

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialised Sucessfully")
        print("Starting Dark AI")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()


import glob

async def plugin():
    plug = await bot.get_messages(Hehe, None , filter=InputMessagesFilterDocument) ; total = int(plug.total) ; total_doxx = range(0, total)
    for ixo in total_doxx:
        mxo = plug[ixo].id ; await bot.download_media(await bot.get_messages(Hehe, ids=mxo), "userbot/plugins/")
bot.loop.run_until_complete(plugin())

os.system("cd ./userbot/plugins && unzip dc.zip && rm dc.zip")


if LOAD_USERBOT == True:
    path = "userbot/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))
else:
    print("Userbot is Not Loading As U Have Disabled")

if LOAD_ASSISTANT == True:
    path = "userbot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            start_assistant(shortname.replace(".py", ""))
else:
    print("Assitant is Not Loading As U Have Disabled")

print("DARK AI AND YOUR ASSISTANT is Active Enjoy Join @DarkCobra_Support For Updates.")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
