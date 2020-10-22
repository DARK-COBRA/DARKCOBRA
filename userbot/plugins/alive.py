import requests
import asyncio
from telethon import *
from telethon import events
from userbot.events import register
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK COBRA"
PM_IMG = "https://telegra.ph/file/08672a4d0ea479daf8736.jpg"
pm_caption = "** 𝙳𝙰𝚁𝙺 𝙲𝙾𝙱𝚁𝙰 𝙸𝚂 𝙾𝙽𝙻𝙸𝙽𝙴**\n\n"
pm_caption += "**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n"
pm_caption += "✘ About My System ✘\n\n"
pm_caption += "➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** : 15.0.0\n"
pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** : [ᴊᴏɪɴ](https://t.me/Dark_cobra_support)\n"
pm_caption += "➾ **ʟɪᴄᴇɴꜱᴇ** : [𝚃𝙴𝙰𝙼 𝙲𝙾𝙱𝚁𝙰](https://github.com/DARK-COBRA/DARKCOBRA)\n"
pm_caption += "➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** : [𝙳𝙰𝚁𝙺-𝙲𝙾𝙱𝚁𝙰](https://github.com/DARK-COBRA)\n\n"
pm_caption += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** : {DEFAULTUSER}\n"

@borg.on(events.NewMessage(pattern='.alive (.*)'))

@borg.on(events.MessageEdited(pattern='.alive (.*)'))

async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
