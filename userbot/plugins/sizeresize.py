import PIL
from userbot.utils import admin_cmd
from userbot import CMD_HELP
import pygments, os, asyncio
from pygments.lexers import Python3Lexer
from pygments.formatters import ImageFormatter
from userbot.utils import admin_cmd
from userbot import bot
from userbot import bot as borg
@bot.on(admin_cmd(pattern="size ?(.*)", outgoing=True))
# DONOT KANG by Sh1vam
#Team DC
async def __(event):
    
    path = "shivamdownloadesimg"

    reply = await event.get_reply_message()
        
    download = await borg.download_media(reply.media, path)
    image = PIL.Image.open(download)
    shvm=PIL.Image.open(download)
    shi,vam = image.size
    #img=shvm.resize((int(sh1),int(vam)))
    await event.edit(f"Dimensions Of Image are {shi} by {vam}")
    os.remove(download)
@bot.on(admin_cmd(pattern="resize ?(.*)", outgoing=True))
# DONOT KANG by Sh1vam
async def __(event):
    path = "shivamdownloades"
    licence = event.text
    liscence=licence[8:]
    await event.delete()
    reply = await event.get_reply_message()
    download = await borg.download_media(reply.media, path)
    shvm=PIL.Image.open(download)
    shi,vam = liscence.split(":")
    img=shvm.resize((int(shi),int(vam)))
    img.save("sh1vam.png", format="PNG", optimize=True)
    await event.client.send_file(event.chat_id, "sh1vam.png", force_document=False, reply_to=event.reply_to_msg_id)
    os.remove(download)
    os.remove("sh1vam.png")













    
