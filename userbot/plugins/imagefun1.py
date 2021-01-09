

import cv2
import numpy as np
from PIL import Image, ImageDraw
import pygments, os, asyncio, shutil, scapy, sys, requests, re, subprocess
from pygments.lexers import Python3Lexer
from pygments.formatters import ImageFormatter
from userbot import bot, CMD_HELP
from userbot.utils import admin_cmd, sudo_cmd
from telegraph import upload_file
from telethon import events
from telethon.tl.types import MessageMediaPhoto


path = "./dcobra/"
if not os.path.isdir(path):
    os.makedirs(path)

@bot.on(admin_cmd(pattern=r"trig"))
async def dc(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any media.")
        return
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    download = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(download)
    ret, frame = img.read()
    cv2.imwrite("danish.png", frame)
    url = upload_file("danish.png")
    link = f"https://telegra.ph{url[0]}"
    api = f"https://some-random-api.ml/canvas/triggered?avatar={link}"
    r = requests.get(api)
    open("shivam.gif", "wb").write(r.content)
    await event.client.send_file(event.chat_id, "shivam.gif", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.png")
    os.remove("shivam.gif")
    
            
@bot.on(admin_cmd(pattern=r"wst"))
async def dc(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any media.")
        return
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    download = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(download)
    ret, frame = img.read()
    cv2.imwrite("danish.png", frame)
    url = upload_file("danish.png")
    link = f"https://telegra.ph{url[0]}"
    api = f"https://some-random-api.ml/canvas/wasted?avatar={link}"
    r = requests.get(api)
    open("shivam.gif", "wb").write(r.content)
    await event.client.send_file(event.chat_id, "shivam.gif", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.png")
    os.remove("shivam.gif")
            

@bot.on(admin_cmd(pattern="rgif"))
async def _(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any media.")
        return
    reply = await event.get_reply_message()
    download = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(download)
    ret, frame = img.read()
    cv2.imwrite("danish.png", frame)
    danish = PIL.Image.open("danish.png")
    dark,python = danish.size
    cobra = f"""ffmpeg -f lavfi -i color=c=00ff00:s={dark}x{python}:d=10 -loop 1 -i danish.png -filter_complex "[1]rotate=angle=PI*t:fillcolor=none:ow='hypot(iw,ih)':oh=ow[fg];[0][fg]overlay=x=(W-w)/2:y=(H-h)/2:shortest=1:format=auto,format=yuv420p" -movflags +faststart danish.mp4 -y"""                 
    await event.edit("```Processing ...```")
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    process = await asyncio.create_subprocess_shell(
        cobra, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    await event.edit("```Uploading...```")
    await event.client.send_file(event.chat_id, "danish.mp4" , force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.mp4")
    os.remove("danish.png")

            

@bot.on(admin_cmd("grey"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any Media.")
        return
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    cv2.imwrite("danish.jpg", gray)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")

    
   
@bot.on(admin_cmd(pattern="circle", outgoing=True))
async def shiv(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any media.")
        return
    await event.edit("```Processing...```")
    reply = await event.get_reply_message()
    download = await bot.download_media(reply.media, path)
    danish = cv2.VideoCapture(download) 
    ret, frame = danish.read()
    cv2.imwrite("danish.jpg", frame)
    img=Image.open("danish.jpg").convert("RGB")
    npImage=np.array(img)
    h,w=img.size
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,h,w],0,360,fill=255)
    npAlpha=np.array(alpha)
    npImage=np.dstack((npImage,npAlpha))
    Image.fromarray(npImage).save('shivam.webp')
    await event.client.send_file(event.chat_id, "shivam.webp", force_document=False, reply_to=event.reply_to_msg_id)
    shutil.rmtree(path)
    os.remove("shivam.webp")
    os.remove("danish.jpg")




CMD_HELP.update(
    {
        "imagefun": "__**PLUGIN NAME :** Image Fun _\
    \n\n📌** CMD ★** `.trig (reply to image)`\
    \n**USAGE   ★  **Makes a Triggered Gif\
    \n\n📌** CMD ★** `.wst(reply to image)`\
    \n**USAGE   ★  **Makes a Triggered Gif\
    \n\n📌** CMD ★** `.rgif(reply to media)`\
    \n**USAGE   ★  **Show A rotation gif. 😂😂\
    \n\n📌** CMD ★** `.grey(reply to image)`\
    \n**USAGE   ★  **Convert Colour image to Black nd white\
    \n\n📌** CMD ★** `.ytc (Name).(text)(reply to image)`\
    \n**USAGE   ★  **Show A Youtube Comment of ur repled img and typed name. (note :- that dot . in middle is important)\
    \n\n📌** CMD ★** `.invert`\
    \n**USAGE   ★  **Create a Negative image to return it back to normal use .invert again\
    \n\n📌** CMD ★** `.blur /.pencil /.enhance / .smooth / .embross /.bright / .sharp / .` \
    \ncheck them on ur own 😁😁\
    \n(note:- it work only on images, u can use .stoi to convert a sticker info image then u can use😁😁)"
      
    }
)









    
