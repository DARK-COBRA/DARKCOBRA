#Made By Sh1vam  Donot KANG
# ME MADE MORE THAN ONE AND MORE COMPLEX ONE WAS YT COMMENT 
#I REMOVED COLOUR CAUSE ALL NEED TO REMEMBER HEX COLOUR CODES # replaced by %23
# DARKCOBRA ORIGINAL 
# by @shivam_patel , fix nd edited by @danish_00
# by #team dc

# Kangers Keep Credits

# Kepp Credits

import os
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
    #Made By Sh1vam  Donot KANG
# ME MADE MORE THAN ONE AND MORE COMPLEX ONE WAS YT COMMENT 
#I REMOVED COLOUR CAUSE ALL NEED TO REMEMBER HEX COLOUR CODES # replaced by %23
# DARKCOBRA ORIGINAL 
# by @shivam_patel , fix nd edited by @danish_00
# by #team dc

# Kangers Keep Credits

# Kepp Credits
@bot.on(admin_cmd(pattern=r"rmbw"))
@bot.on(sudo_cmd(pattern=r"rmbw", allow_sudo=True))
async def dc(event):
    await event.edit("Filling This img with Colors 😊")    
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
    hehe = f"https://some-random-api.ml/canvas/gay?avatar={link}"
    r = requests.get(hehe)
    open("shivam.png", "wb").write(r.content)
    hehe = "shivam.png"
    await borg.send_file(
        event.chat_id, hehe, caption="Wow Its a Ranbow🌈 😂", reply_to=dc
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
@bot.on(admin_cmd(pattern=r"bow"))
@bot.on(sudo_cmd(pattern=r"bow", allow_sudo=True))
async def dc(event):
    await event.edit("Adding Filter 😎")    
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
    hehe = f"https://some-random-api.ml/canvas/threshold?avatar={link}"
    r = requests.get(hehe)
    open("shivam.png", "wb").write(r.content)
    hehe = "shivam.png"
    await borg.send_file(
        event.chat_id, hehe, reply_to=dc
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
            
@bot.on(admin_cmd(pattern=r"sepia"))
@bot.on(sudo_cmd(pattern="sepia", allow_sudo=True))
async def dc(event):
    await event.edit("Adding Filter 😎")    
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
    hehe = f"https://some-random-api.ml/canvas/sepia?avatar={link}"
    r = requests.get(hehe)
    open("shivam.png", "wb").write(r.content)
    hehe = "shivam.png"
    await borg.send_file(
        event.chat_id, hehe, reply_to=dc
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
           
@bot.on(admin_cmd(pattern=r"red"))
@bot.on(sudo_cmd(pattern=r"red", allow_sudo=True))
async def dc(event):
    await event.edit("Adding Filter 😎")    
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
    hehe = f"https://some-random-api.ml/canvas/red?avatar={link}"
    r = requests.get(hehe)
    open("shivam.png", "wb").write(r.content)
    hehe = "shivam.png"
    await borg.send_file(
        event.chat_id, hehe, reply_to=dc
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
            
@bot.on(admin_cmd(pattern=r"green"))
@bot.on(sudo_cmd(pattern=r"green", allow_sudo=True))
async def dc(event):
    await event.edit("Adding Filter 😎")    
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
    hehe = f"https://some-random-api.ml/canvas/green?avatar={link}"
    r = requests.get(hehe)
    open("shivam.png", "wb").write(r.content)
    hehe = "shivam.png"
    await borg.send_file(
        event.chat_id, hehe, reply_to=dc
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
@bot.on(admin_cmd(pattern=r"blue"))
@bot.on(sudo_cmd(pattern=r"blue", allow_sudo=True))
async def dc(event):
    await event.edit("Adding Filter 😎")    
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
    hehe = f"https://some-random-api.ml/canvas/blue?avatar={link}"
    r = requests.get(hehe)
    open("shivam.png", "wb").write(r.content)
    hehe = "shivam.png"
    await borg.send_file(
        event.chat_id, hehe, reply_to=dc
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






CMD_HELP.update(
    {
        "imagefilter": "__**PLUGIN NAME :** Image filter _\
    \n\n📌** CMD ★** `.rmbw (reply to image)`\
    \n**USAGE   ★  **Add Rainbow 🌈 Filter\
    \n\n📌** CMD ★** `.bow(reply to image)`\
    \n**USAGE   ★  **Add (Don't know) Filter😂\
    \n\n📌** CMD ★** `.sepia(reply to image)`\
    \n**USAGE   ★  **Add cool Sepia filter \
    \n\n📌** CMD ★** `.red / .blue /.green`\
    \ncheck them on ur own 😁😁\
    \n(Note:- it work only on images, u can use .stoi to convert a sticker info image then u can use😁😁) "
      
    }
)


#gtfo

#nikal mc
