

   
   # import cv2
   # By @danish_00
   # with @shivam_patel
   # @THE_B_LACK_HAT
   # Team Dc
   # For Cobra

import cv2
import numpy as np
import PIL
from PIL import Image, ImageDraw
import pygments, os, asyncio, shutil, scapy, sys, requests, re, subprocess, urllib
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
    

    # New .wst By @Shivam_Patel with @danish_00

@borg.on(admin_cmd(pattern=r"wst"))
async def hmm(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any media.")
        return
    reply = await event.get_reply_message()
    await event.edit("```Processing```")
    os.system(f'wget https://telegra.ph/file/b3a6038bc825cc4edc4f0.png')
    img = await bot.download_media(reply.media, path)
    mon = "b3a6038bc825cc4edc4f0.png"
    foreground = Image.open(mon).convert("RGBA")
    img = cv2.VideoCapture(img) 
    tales, miraculous = img.read()
    cv2.imwrite("MiraculousLadybug.png",miraculous)
    shvm=PIL.Image.open("MiraculousLadybug.png")
    shi,vam = shvm.size
    img=shvm.resize((512,512))
    img.save("shivamgta.png", format="PNG", optimize=True)
    img = cv2.VideoCapture("shivamgta.png") 
    tales, miraculousladybug = img.read()
    dan = cv2.cvtColor(miraculousladybug, cv2.COLOR_BGR2GRAY) 
    bug = cv2.imwrite("shivamgtas.jpg", dan)
    image = cv2.imread("shivamgtas.jpg")
    overlay = image.copy()
    overlay =cv2.rectangle(overlay, (0, 210), (800, 310), (0,0,0), -1) 
    image_new = cv2.addWeighted(overlay, 0.5 , image, 0.5 , 0)
    cv2.imwrite("shivamgta.jpg", image_new)
    background = Image.open("shivamgta.jpg").convert("RGB")
    with Image.open("shivamgta.jpg") as imge:
        width, height = imge.size
    fg_resized = foreground.resize((width, int(height/5)))
    background.paste(fg_resized, box=(0,int(height/2)-50), mask=fg_resized)
    background.save("shivamwasted.png")
    miraculous=PIL.Image.open("shivamwasted.png")
    img=miraculous.resize((int(shi),int(vam)))
    img.save("shivamwastedgta.png", format="PNG", optimize=True)
    await event.client.send_file(event.chat_id, "shivamwastedgta.png", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    os.remove("shivamwasted.png")
    os.remove("shivamwastedgta.png")
    os.remove("MiraculousLadybug.png")
    os.remove("shivamgta.png")
            

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
    danish = Image.open("danish.png")
    dark,python = danish.size
    cobra = f"""ffmpeg -f lavfi -i color=c=ffffff00:s={dark}x{python}:d=10 -loop 1 -i danish.png -filter_complex "[1]rotate=angle=PI*t:fillcolor=none:ow='hypot(iw,ih)':oh=ow[fg];[0][fg]overlay=x=(W-w)/2:y=(H-h)/2:shortest=1:format=auto,format=yuv420p" -movflags +faststart danish.mp4 -y"""                 
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

    # api for adding color only....  
DARKCOBRA = Config.DEEP_AI if Config.DEEP_AI else "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"
@borg.on(admin_cmd(pattern="color$", outgoing=True))
async def _(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any Media.")
        return
    reply = await event.get_reply_message()
    await event.edit("`Coloring image 🎨🖌️...`")
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    cv2.imwrite("danish.jpg", frame)
    r = requests.post(
        "https://api.deepai.org/api/colorizer",
        files={"image": open("danish.jpg", "rb")},
        headers={"api-key": f"{DARKCOBRA}"})
    os.remove("danish.jpg")
    if "status" in r.json():
        return await event.edit( r.json()["status"])
    r_json = r.json()["output_url"]
    pic_id = r.json()["id"]
    link = f"https://api.deepai.org/job-view-file/{pic_id}/inputs/image.jpg"
    result = f"{r_json}"
    await bot.send_message(event.chat_id, file = result, reply_to=event.reply_to_msg_id)
    await event.delete()
    
   
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
    await event.delete()
    shutil.rmtree(path)
    os.remove("shivam.webp")
    os.remove("danish.jpg")


@borg.on(admin_cmd(pattern="ftoon$"))
async def _(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any Media.")
        return
    reply = await event.get_reply_message()
    await event.edit("```Toonifing face😜😝...```")
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    cv2.imwrite("danish.jpg", frame)
    r = requests.post(
        "https://api.deepai.org/api/toonify",
        files={"image": open("danish.jpg", "rb")},
        headers={"api-key": f"{DARKCOBRA}"})
    os.remove("danish.jpg")
    if "status" in r.json():
        return await event.edit( r.json()["status"])
    await event.edit("```Be sure to reply a image in which face is visible```")
    r_json = r.json()["output_url"]
    pic_id = r.json()["id"]
    link = f"https://api.deepai.org/job-view-file/{pic_id}/inputs/image.jpg"
    result = f"{r_json}"
    await bot.send_message(event.chat_id, file = result, reply_to=event.reply_to_msg_id)
    await event.delete()

CMD_HELP.update(
    {
        "imagefun1": "__**PLUGIN NAME :** Image Fun _\
    \n\n📌** CMD ★** `.trig (reply to media)`\
    \n**USAGE   ★  **Makes a Triggered Gif\
    \n\n📌** CMD ★** `.wst(reply to media)`\
    \n**USAGE   ★  **Makes a Triggered Gif\
    \n\n📌** CMD ★** `.rgif(reply to media)`\
    \n**USAGE   ★  **Show A rotation gif. 😂😂\
    \n\n📌** CMD ★** `.grey(reply to media)`\
    \n**USAGE   ★  **Convert Colour image to Black nd white\
    \n\n📌** CMD ★** `.color(reply to media)`\
    \n**USAGE   ★  **Convert Black-White media to Colorfull.\
    \n\n📌** CMD ★** `.circle(reply to media)`\
    \n**USAGE   ★  **Make A circle sticker of that media.\
    \n\n📌** CMD ★** `.ftoon(reply to media)`\
    \n**USAGE   ★  **Makes faces look like 💩Toon💩."
    
      
    }


    )#  Thanks for Coming 🤗🤗

    
