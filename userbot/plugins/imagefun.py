#Made By Sh1vam  Donot KANG
# ME MADE MORE THAN ONE AND MORE COMPLEX ONE WAS YT COMMENT 
#I REMOVED COLOUR CAUSE ALL NEED TO REMEMBER HEX COLOUR CODES # replaced by %23
# DARKCOBRA ORIGINAL 
# by @shivam_patel , fix nd edited by @danish_00
# by #team dc

# Kangers Keep Credits

# Kepp Credits



import cv2
# by @danish_00
import os, scipy, sys, shutil
import numpy as np
import requests, re
from PIL import Image
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto
from userbot import bot, CMD_HELP
from userbot.utils import admin_cmd, sudo_cmd

pathdc = "./shivam/"
if not os.path.isdir(pathdc):
    os.makedirs(pathdc)

#keep CREDIT LINES ELSE GET LOST

path = "./cv2/"
if not os.path.isdir(path):
    os.makedirs(path)



@bot.on(admin_cmd(pattern=r"trig"))
@bot.on(sudo_cmd(pattern=r"trig", allow_sudo=True))
async def dc(event):
    await event.edit("Making this image 😡triggered😈")    
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await borg.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await borg.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hmm = f"https://some-random-api.ml/canvas/triggered?avatar={link}"
    r = requests.get(hmm)
    open("shivam.gif", "wb").write(r.content)
    hehe = "shivam.gif"
    await borg.send_file(
        event.chat_id, hehe, caption="Got Triggered 😈😂", reply_to=dc
     )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()
            
        #Made By Sh1vam  Donot KANG
# ME MADE MORE THAN ONE AND MORE COMPLEX ONE WAS YT COMMENT 
#I REMOVED COLOUR CAUSE ALL NEED TO REMEMBER HEX COLOUR CODES # replaced by %23
# DARKCOBRA ORIGINAL 
# by @shivam_patel , fix nd edited by @danish_00
# by #team dc

# Kangers Keep Credits

# Kepp Credits
@bot.on(admin_cmd(pattern=r"wst"))
@bot.on(sudo_cmd(pattern=r"wst", allow_sudo=True))
async def dc(event):
    await event.edit("What a waste 😒😒")    
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await borg.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await borg.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hmm = f"https://some-random-api.ml/canvas/wasted?avatar={link}"
    r = requests.get(hmm)
    open("shivam.png", "wb").write(r.content)
    hehe = "shivam.png"
    await borg.send_file(
        event.chat_id, hehe, caption="Totally wasted⚰️ 😒", reply_to=dc
     )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()
            
          #Made By Sh1vam  Donot KANG
# ME MADE MORE THAN ONE AND MORE COMPLEX ONE WAS YT COMMENT 
#I REMOVED COLOUR CAUSE ALL NEED TO REMEMBER HEX COLOUR CODES # replaced by %23
# DARKCOBRA ORIGINAL 
# by @shivam_patel , fix nd edited by @danish_00
# by #team dc

# Kangers Keep Credits

# Kepp Credits
            

            
            

@bot.on(admin_cmd("grey"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
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

    ##Made By Sh1vam  Donot KANG
# ME MADE MORE THAN ONE AND MORE COMPLEX ONE WAS YT COMMENT 
#I REMOVED COLOUR CAUSE ALL NEED TO REMEMBER HEX COLOUR CODES # replaced by %23
# DARKCOBRA ORIGINAL 
# by @shivam_patel , fix nd edited by @danish_00
# by #team dc

# Kangers Keep Credits

# Kepp Credits
    
@bot.on(admin_cmd("blur"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
   
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read() 
    blur = cv2.GaussianBlur(frame, (35, 35), 0)
    cv2.imwrite("danish.jpg", blur)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")

@bot.on(admin_cmd("invert"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    invert = cv2.bitwise_not(frame)
    cv2.imwrite("danish.jpg", invert)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")


@bot.on(admin_cmd("enhance"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return   
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    dtl = cv2.detailEnhance(frame, sigma_s=10, sigma_r=0.15)
    cv2.imwrite("danish.jpg", dtl)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")

@bot.on(admin_cmd("smooth"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return   
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read() 
    smooth = cv2.edgePreservingFilter(frame, flags=1, sigma_s=60, sigma_r=0.4)
    cv2.imwrite("danish.jpg", smooth)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")

@bot.on(admin_cmd("pencil"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return 
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read() 
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3,3), 0)
    output = cv2.Laplacian(blur, -1, ksize=5)
    output = 255 - output
    ret, output = cv2.threshold(output, 150, 255, cv2.THRESH_BINARY)
    cv2.imwrite("danish.jpg", output)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")
    
@bot.on(admin_cmd("igrey"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return    
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    invert = cv2.bitwise_not(frame)
    gray = cv2.cvtColor(invert, cv2.COLOR_BGR2GRAY) 
    cv2.imwrite("danish.jpg", gray)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")          
    
    

            

          #Made By Sh1vam  Donot KANG
# ME MADE MORE THAN ONE AND MORE COMPLEX ONE WAS YT COMMENT 
#I REMOVED COLOUR CAUSE ALL NEED TO REMEMBER HEX COLOUR CODES # replaced by %23
# DARKCOBRA ORIGINAL 
# by @shivam_patel , fix nd edited by @danish_00
# by #team dc

# Kangers Keep Credits

# Kepp Credits
@bot.on(admin_cmd(pattern=r"ytc"))
@bot.on(sudo_cmd(pattern=r"ytc", allow_sudo=True))
async def hehe(event):
    await event.edit("Lets make a utube comment 😁😁")
    givenvar=event.text
    text = givenvar[5:]
    try:
        global username, comment
        username, comment= text.split(".")
    except:
        await event.edit("`.ytc username.comment reply  to image`")
    await event.delete()
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await borg.download_media(dc.media, pathdc)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(dc.media, pathd )
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    nikal = f"https://some-random-api.ml/canvas/youtube-comment?avatar={imglink}&comment={comment}&username={username}"
    r = requests.get(nikal)
    open("shivam.png", "wb").write(r.content)
    chutiya = "shivam.png"
    await borg.send_file(
        event.chat_id, chutiya, reply_to=dc
    )
    for files in (chutiya, img):
        if files and os.path.exists(files):
            os.remove(files)
            
    await event.delete()

       #Made By Sh1vam  Donot KANG
# ME MADE MORE THAN ONE AND MORE COMPLEX ONE WAS YT COMMENT 
#I REMOVED COLOUR CAUSE ALL NEED TO REMEMBER HEX COLOUR CODES # replaced by %23
# DARKCOBRA ORIGINAL 
# by @shivam_patel , fix nd edited by @danish_00
# by #team dc

# Kangers Keep Credits


        


CMD_HELP.update(
    {
        "imagefun": "__**PLUGIN NAME :** Image Fun _\
    \n\n📌** CMD ★** `.trig (reply to image)`\
    \n**USAGE   ★  **Makes a Triggered Gif\
    \n\n📌** CMD ★** `.wst(reply to image)`\
    \n**USAGE   ★  **Show A Wasted Image 😂😂\
    \n\n📌** CMD ★** `.grey(reply to image)`\
    \n**USAGE   ★  **Convert Colour image to Black nd white\
    \n\n📌** CMD ★** `.ytc (Name).(text)(reply to image)`\
    \n**USAGE   ★  **Show A Youtube Comment of ur repled img and typed name. (note :- that dot . in middle is important)\
    \n\n📌** CMD ★** `.invert`\
    \n**USAGE   ★  **Create a Negative image to return it back to normal use .invert again\
    \n\n📌** CMD ★** `.blur /.pencil /.enhance / .smooth / .igrey /.bright / .glass / .blrpl` \
    \ncheck them on ur own 😁😁\
    \n(note:- it work only on images, u can use .stoi to convert a sticker info image then u can use😁😁)"
      
    }
)




#gtfo
#nikal mc
