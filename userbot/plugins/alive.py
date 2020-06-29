
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


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

ALIVE_MESSAGE = Config.ALIVE_MSG
if ALIVE_MESSAGE is None:
  ALIVE_MESSAGE = "**🔱ＤａＲｋ　ｐＲｉＮｃＥ IS still Alive🔱\n\n\n**"
  ALIVE_MESSAGE += "`My Bot Status\n\n\n`"
  ALIVE_MESSAGE += f"`Telethon version: Telethon Not Found\n`"
  ALIVE_MESSAGE += f"`Python: PYTHON-3.6.4 \n\n`"
  ALIVE_MESSAGE += "`I'll Be With You Till My Dyno Ends!!\n\n`"
  ALIVE_MESSAGE += f"`Support Channel` : @uSe_DaRk_PrInCe\n\n"
  ALIVE_MESSAGE += f"`Bot Created And Maintained By`:   {DEFAULTUSER}\n\n"
  ALIVE_MESSAGE += "[DEPLOY This Lit Userbot Now](https://github.com/No-OnE-Kn0wS-Me/dArK_pRiNcE)"

buttons=[
                    [custom.Button.url("Repo Link", "https://github.com/No-OnE-Kn0wS-Me/dArK_pRiNcE")],
                ],
                link_preview=True




#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete() 
    await borg.send_file(alive.chat_id, ALIVE_IMG,caption=ALIVE_MESSAGE)
