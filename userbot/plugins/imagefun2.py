

     # By @danish_00
     # OpenCV Basics
     # For Dark Cobra
     # Team Dc

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


    
@bot.on(admin_cmd("mirror"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to media")
        return
    await event.edit("```Processing...```")
    reply = await event.get_reply_message()
    pathh = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(pathh)
    iss,dan = img.read()
    ish = cv2.flip(dan, 1)
    misi = cv2.hconcat([dan, ish])
    cv2.imwrite('dark.jpg', misi)
    await event.client.send_file(event.chat_id, "dark.jpg" , reply_to=event.reply_to_msg_id) 
    await event.delete()
    shutil.rmtree(path)
    os.remove("dark.jpg")
    


@bot.on(admin_cmd("quad"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to media")
        return
    await event.edit("```Processing...```")
    reply = await event.get_reply_message()
    pathh = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(pathh)
    ros,dcob = img.read()
    danish = cv2.flip(dcob, 1)
    mici = cv2.hconcat([dcob, danish])
    fr = cv2.flip(mici, 1)
    trn = cv2.rotate(fr, cv2.ROTATE_180)
    fix = cv2.vconcat([mici, trn])
    cv2.imwrite('dark.jpg', fix)
    await event.client.send_file(event.chat_id, "dark.jpg" , reply_to=event.reply_to_msg_id) 
    await event.delete()
    shutil.rmtree(path)
    os.remove("dark.jpg")   
    

@bot.on(admin_cmd("flip"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to media")
        return
    await event.edit("```Processing...```")
    reply = await event.get_reply_message()
    pathh = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(pathh)
    iss,dan = img.read()
    trn = cv2.flip(dan, 1)
    ish = cv2.rotate(trn, cv2.ROTATE_180)
    misi = cv2.vconcat([dan, ish])
    cv2.imwrite('dark.jpg', misi)
    await event.client.send_file(event.chat_id, "dark.jpg" , reply_to=event.reply_to_msg_id) 
    await event.delete()
    shutil.rmtree(path)
    os.remove("dark.jpg")
    


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

    # .ytc by @shivam_patel
    #  kang with credits
@bot.on(admin_cmd(pattern=r"ytc"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    reply = await event.get_reply_message()
    download = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(download)
    ret, frame = img.read()
    cv2.imwrite("danish.png", frame)
    givenvar=event.text
    text = givenvar[5:]
    try:
        global username, comment
        username, comment= text.split(".")
    except:
        await event.edit("`.ytc username.comment reply  to image`")
    url_s = upload_file("danish.png")
    imglink = f"https://telegra.ph{url_s[0]}"
    nikal = f"https://some-random-api.ml/canvas/youtube-comment?avatar={imglink}&comment={comment}&username={username}"
    r = requests.get(nikal)
    open("shivam.png", "wb").write(r.content)
    await event.client.send_file(event.chat_id, "shivam.png", reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("shivam.png")
    os.remove("danish.jpg")
