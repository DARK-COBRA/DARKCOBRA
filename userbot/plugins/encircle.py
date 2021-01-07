import PIL
from userbot.utils import admin_cmd
from userbot import CMD_HELP
import pygments, os, asyncio
from pygments.lexers import Python3Lexer
from pygments.formatters import ImageFormatter
from userbot.utils import admin_cmd
from userbot import bot
from userbot import bot as borg
import numpy as np
from PIL import Image, ImageDraw
@bot.on(admin_cmd(pattern="circle", outgoing=True))
# DONOT KANG by Sh1vam
async def shiv(event):
    
    path = "shivamencircles"
    licence = event.text
    liscence=licence[8:]
    await event.delete()
    reply = await event.get_reply_message()
    
    download = await borg.download_media(reply.media, path)
    #image = PIL.Image.open(download)
    img=Image.open(download).convert("RGB")
    npImage=np.array(img)
    h,w=img.size
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,h,w],0,360,fill=255)
    npAlpha=np.array(alpha)

    # Add alpha layer to RGB
    npImage=np.dstack((npImage,npAlpha))

    # Save with alpha
    Image.fromarray(npImage).save('sirsle.png')
    #await event.edit(f"Dimensions Of Image are {shi} by {vam}")
    #img.save("sh1vam.png", format="PNG", optimize=True)
    await event.client.send_file(event.chat_id, "sirsle.png", force_document=True, reply_to=event.reply_to_msg_id)
    await event.client.send_file(event.chat_id, "sirsle.png", force_document=False, reply_to=event.reply_to_msg_id)
    os.remove(download)
    os.remove("sirsle.png")













    
