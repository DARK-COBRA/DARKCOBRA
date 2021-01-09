 
    

     # @THE_B_LACK_HAT with @shivam_patel
     # Modified with OpenCV by @danish_00
     # Team Cobra
     # For Dark Cobra
     # Keep Credits

import cv2
from PIL import Image
import sys
import os
from userbot.utils import admin_cmd
from userbot import bot, CMD_HELP

     # Now Gifs nd Stickers also Support
     # OpenCV Basics

path = "./dcobra/"
if not os.path.isdir(path):
    os.makedirs(path)
    
@bot.on(admin_cmd(pattern=r"thug"))
async def scan(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any Image.")
        return
    await event.edit("HeHe Lets give a Mask 🤪")
    reply = await event.get_reply_message()
    lol = await bot.download_media(reply.media, path)
    os.system('wget https://datreon.000webhostapp.com/haarcascade_frontalface_default.xml')    
    os.system('wget https://telegra.ph/file/8c47ddc5c368a1d4f4ee4.png')
    image = lol
    maskPath = "8c47ddc5c368a1d4f4ee4.png"
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    cv2.imwrite("hehe.png", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.15)
    background = Image.open("hehe.png")
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
    file_name = "danish.png"
    hehe = path + "/" + file_name
    background.save(hehe, "PNG")
    await event.client.send_file(event.chat_id, hehe , force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
            
    
@bot.on(admin_cmd(pattern=r"pru"))
async def scan(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any Image.")
        return
    await event.edit("HeHe Lets give a Mask 🤪")
    reply = await event.get_reply_message()
    lol = await bot.download_media(reply.media, path)
    os.system('wget https://datreon.000webhostapp.com/haarcascade_frontalface_default.xml')    
    os.system('wget https://telegra.ph/file/f061c861ba85fbb23a51e.png')
    image = lol
    maskPath = "f061c861ba85fbb23a51e.png"
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    cv2.imwrite("hehe.png", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.15)
    background = Image.open("hehe.png")
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
    file_name = "danish.png"
    hehe = path + "/" + file_name
    background.save(hehe, "PNG")
    await event.client.send_file(event.chat_id, hehe , force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
            
@bot.on(admin_cmd(pattern=r"old"))
async def scan(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any Image.")
        return
    await event.edit("HeHe Lets give a Mask 🤪")
    reply = await event.get_reply_message()
    lol = await bot.download_media(reply.media, path)
    os.system('wget https://datreon.000webhostapp.com/haarcascade_frontalface_default.xml')    
    os.system('wget https://telegra.ph/file/55fcb205c6f8f4790585e.png')
    image = lol
    maskPath = "55fcb205c6f8f4790585e.png"
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    cv2.imwrite("hehe.png", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.15)
    background = Image.open("hehe.png")
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
    file_name = "danish.png"
    hehe = path + "/" + file_name
    background.save(hehe, "PNG")
    await event.client.send_file(event.chat_id, hehe , force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
            
            
            
@bot.on(admin_cmd(pattern=r"krish"))
async def scan(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any Image.")
        return
    await event.edit("HeHe Lets give a Mask 🤪")
    reply = await event.get_reply_message()
    lol = await bot.download_media(reply.media, path)
    os.system('wget https://datreon.000webhostapp.com/haarcascade_frontalface_default.xml')    
    os.system('wget https://telegra.ph/file/54d2a267d411951b41a20.png')
    image = lol
    maskPath = "54d2a267d411951b41a20.png"
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    cv2.imwrite("hehe.png", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.15)
    background = Image.open("hehe.png")
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
    file_name = "danish.png"
    hehe = path + "/" + file_name
    background.save(hehe, "PNG")
    await event.client.send_file(event.chat_id, hehe , force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
            
            
            
@bot.on(admin_cmd(pattern=r"oxy"))
async def scan(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any Image.")
        return
    await event.edit("HeHe Lets give a Mask 🤪")
    reply = await event.get_reply_message()
    lol = await bot.download_media(reply.media, path)
    os.system('wget https://datreon.000webhostapp.com/haarcascade_frontalface_default.xml')    
    os.system('wget https://telegra.ph/file/df2d739544595ae337642.png')
    image = lol
    maskPath = "df2d739544595ae337642.png" 
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    cv2.imwrite("hehe.png", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.15)
    background = Image.open("hehe.png")
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
    file_name = "danish.png"
    hehe = path + "/" + file_name
    background.save(hehe, "PNG")
    await event.client.send_file(event.chat_id, hehe , force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
            
@bot.on(admin_cmd(pattern=r"gold"))
async def scan(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any Image.")
        return
    await event.edit("HeHe Lets give a Mask 🤪")
    reply = await event.get_reply_message()
    lol = await bot.download_media(reply.media, path)
    os.system('wget https://datreon.000webhostapp.com/haarcascade_frontalface_default.xml')    
    os.system('wget https://telegra.ph/file/4cc40d1e0846667488341.png')
    image = lol
    maskPath = "4cc40d1e0846667488341.png"
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    cv2.imwrite("hehe.png", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.15)
    background = Image.open("hehe.png")
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
    file_name = "danish.png"
    hehe = path + "/" + file_name
    background.save(hehe, "PNG")
    await event.client.send_file(event.chat_id, hehe , force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
            
            
@bot.on(admin_cmd(pattern=r"cmask ?(.*)"))
async def scan(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any Image.")
        return
    if not event.pattern_match.group(1):
        await event.edit("Give a link of a background less mask\nTo put on that image")
        return
    await event.edit("HeHe Lets give a Mask 🤪")
    reply = await event.get_reply_message()
    linc= event.text
    link=linc[7:]
    pic=linc[31:]
    os.system(f'wget {link}')
    lol = await bot.download_media(reply.media, path)
    os.system('wget https://datreon.000webhostapp.com/haarcascade_frontalface_default.xml')    
    image = lol
    maskPath = f"{pic}"
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    cv2.imwrite("hehe.png", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.15)
    background = Image.open("hehe.png")
    await event.edit("The link is not supporting , be sure to send link of a transparent mask.")
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
    await event.delete()
    file_name = "danish.png"
    hehe = path + "/" + file_name
    background.save(hehe, "PNG")
    await event.client.send_file(event.chat_id, hehe , force_document=False, reply_to=event.reply_to_msg_id)
    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
            
