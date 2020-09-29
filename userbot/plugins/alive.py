import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/76df9853cef5f5a857896.jpg"
pm_caption = "**⚜ɢᴏᴅᴢɪʟʟᴀ ɪs ᴏɴʟɪɴᴇ⚜**\n"
 
pm_caption += f"**M̴y̴ ̴B̴o̴s̴s̴**       : {DEFAULTUSER}\n"


pm_caption += "Mʏ Bᴏᴛ Sᴛᴀᴛᴜꜱ      : Wᴏʀᴋɪɴɢ ᴘᴇʀғᴇᴄᴛʟʏ🔥"


pm_caption += "тєℓєтнσи           : тєℓєтнσи-15.0.0 𖤐⃟🔷"

pm_caption += "ρутнσи             : ρутнσи-3.8.5 𖤐⃟🔷"




pm_caption += "My Master's other acc  : @Godzilla_365 🔱"



pm_caption += "ι'ℓℓ вє ωιтн му мαѕтєя тιℓℓ му ∂уиσ єи∂ѕ!!☠ 𖤐⃟🛰"



pm_caption += " [┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/Mothra365)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
