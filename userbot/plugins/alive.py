import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK COBRA"
PM_IMG = "https://telegra.ph/file/63d4609c6ab1feac0cb12.jpg"
pm_caption = "**ᴘɪᴋᴀᴄʜᴜ ɪs ᴏɴʟɪɴᴇ**\n\n"
pm_caption += "**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n"
pm_caption += "✘ About My System ✘\n\n"
pm_caption += "➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** : 15.0.0\n"
pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** : [ᴊᴏɪɴ](https://t.me/Dark_cobra_support)\n"
pm_caption += "➾ **ʟɪᴄᴇɴꜱᴇ** : [ᴛᴇᴀᴍ ᴘɪᴋᴀᴄʜᴜ](https://github.com/DARK-COBRA/DARKCOBRA)\n"
pm_caption += "➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** : [ᴛᴇᴀᴍ ᴘɪᴋᴀᴄʜᴜ](https://github.com/DARK-COBRA)\n\n"
pm_caption += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** : {DEFAULTUSER}\n"
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
