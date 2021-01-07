# Thanks to Sipak bro.. 
# animation Idea by @(ItzSipak) 
# Made by @errored_bachha ....TEAM DC
# Kang with credits else gay...
# inline alive
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from userbot import bot as borg
from telethon.tl.custom import Button
from telethon.tl.types import ChannelParticipantsAdmins
ok = borg.get_me()
ghanti = ok.id

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK COBRA"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO" , None)

dc_text=(f"** 𝙳𝙰𝚁𝙺 𝙲𝙾𝙱𝚁𝙰 MOD 𝙸𝚂 𝙾𝙽𝙻𝙸𝙽𝙴**\n\n**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n✘ About My System ✘\n\n➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ 1.17.5\n➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/Dark_cobra_support)\n➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [The Terminal](https://github.com/The-Terminal)\n➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [The-Terminal](https://github.com/The-Terminal/DARKCOBRA)\n\n➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={ghanti})\n")
TG_BOT_USER_NAME_BF_HER = os.environ.get("ALIVE_PHOTTO", None)
if TG_BOT_USER_NAME_BF_HER is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await borg.get_me()
        if query.startswith("dcmod") and event.query.user_id == me.id:
            buttons = [
                [
                    Button.url("Repo", "https://github.com/The-Terminal/DARKCOBRA"),
                    Button.url("Deploy", "https://heroku.com/deploy?template=https://github.com/The-Terminal/DARKCOBRA/blob/master")],
                    [Button.url("String", "https://repl.it/@Danish00/DarkCobra#main.py"),
                    Button.url("Channel", "https://t.me/fryplugins"),
                ]
            ]
            if ALIVE_PHOTTO and ALIVE_PHOTTO.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALIVE_PHOTTO,
                    # title="Shivam",
                    text=dc_text,
                    buttons=buttons,
                )
            elif ALIVE_PHOTTO:
                result = builder.document(
                    ALIVE_PHOTTO,
                    title="DC Mod",
                    text=dc_text,
                    buttons=buttons,
                )
            else:
                result = builder.article(
                    title="DC Mod",
                    text=dc_text,
                    buttons=buttons,
                )
            await event.answer([result] if result else None)
