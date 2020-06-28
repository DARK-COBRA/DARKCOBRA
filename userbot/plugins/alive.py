
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

ALIVE_IMG = Config.ALIVE_PHOTTO
if ALIVE_IMG is None:
  ALIVE_IMG = "https://telegra.ph/file/3952f58c07382778cab87.jpg"
else:
  ALIVE_PHOTTO = ALIVE_IMG


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

  ALIVE_MESSAGE = Config.ALIVE_MSG
else:
  ALIVE_MESSAGE = alive_caption

alive_caption = "**ＤａＲｋ　ｐＲｉＮｃＥ IS Still Running\n\n**"
alive_caption += "`BOT STATUS\n\n`"
alive_caption += f"`Telethon version: {version.__version__}\n`"
alive_caption += "`Database Status: ERROR! DATABASE NOT FOUND!\n`"
alive_caption += f"`Python: PYTHON-3.6.4 \n`"
alive_caption += "`I'll Be With You Till My Dynos Ends!!\n`"
alive_caption += f"`Bot Created And Maintained By`:   {DEFAULTUSER}\n\n"
alive_caption += "[DEPLOY This Lit Userbot Now](https://github.com/No-OnE-Kn0wS-Me/dArK_pRiNcE)"



#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete() 
    await borg.send_file(alive.chat_id, ALIVE_IMG,caption=ALIVE_MESSAGE)
