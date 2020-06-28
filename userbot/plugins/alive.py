
# thanks to @WhySooSerious 
# thanks to @Sur_vivor  
# final editing by leobrownlee



"""Check if userbot alive or not . 

"""
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from platform import python_version, uname

ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
if ALIVE_PIC is None:
  MOD_IMG = "https://telegra.ph/file/189e8ac9f26e1fcff7e36.mp4"
else:
  MOD_IMG = ALIVE_PIC


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"



mod_caption = "**MY BOT IS RUNNING SUCCESFULLY\n\n\n**"
mod_caption += "`🔰SYSTEM STATUS\n\n`"
mod_caption += f"`🔰Telethon version: {version.__version__}\n\n`"
mod_caption += "`🔰Database Status: Databases functioning normally!\n\n`"
mod_caption += f"`🔰Python: {python_version()}\n\n`"
mod_caption += "`🔰Always with you, my master!\n\n`"
mod_caption += f"`🔰Owner Name`:   {DEFAULTUSER}\n\n\n"
mod_caption += "`🔰Bot was modified by:` leobrownlee and Sur_vivor\n\n"
mod_caption += "[DEPLOY MODIFIED FRIDAY](https://github.com/leobrownlee/FRIDAY)"



#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete() 
    await borg.send_file(alive.chat_id, MOD_IMG,caption=mod_caption)
