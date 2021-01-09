


import cv2
import numpy as np
from PIL import Image, ImageDraw
import pygments, os, asyncio, shutil, scapy, sys, requests, re, subprocess
from pygments.lexers import Python3Lexer
from pygments.formatters import ImageFormatter
from userbot import bot, CMD_HELP
from userbot.utils import admin_cmd, sudo_cmd
from telegraph import upload_file, events
from telethon.tl.types import MessageMediaPhoto


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


    
@bot.on(admin_cmd("flip"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to media")
        return
    await event.edit("```Processing...```")
    reply = await event.get_reply_message()
    pathh = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(pathh)
    ret,frame = img.read()
    flip = cv2.flip(frame, 1)
    cv2.imwrite("cobra.jpg", frame)
    cv2.imwrite("danish.jpg", flip) 
    dark = cv2.imread("cobra.jpg")
    cobra = cv2.imread("danish.jpg")
    merge = cv2.hconcat([dark, cobra])
    cv2.imwrite('dark.jpg', merge)
    await event.client.send_file(event.chat_id, "dark.jpg" , reply_to=event.reply_to_msg_id) 
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")
    os.remove("dark.jpg")
    os.remove("cobra.jpg")


@bot.on(admin_cmd("mirror"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to media")
        return
    await event.edit("```Processing...```")
    reply = await event.get_reply_message()
    pathh = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(pathh)
    ret,frame = img.read()
    flip = cv2.flip(frame, 1)
    up = cv2.rotate(flip, cv2.ROTATE_180)
    cv2.imwrite("cobra.jpg", frame)
    cv2.imwrite("danish.jpg", up) 
    dark = cv2.imread("cobra.jpg")
    cobra = cv2.imread("danish.jpg")
    merge = cv2.vconcat([dark, cobra])
    cv2.imwrite('dark.jpg', merge)
    await event.client.send_file(event.chat_id, "dark.jpg" , reply_to=event.reply_to_msg_id) 
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")
    os.remove("dark.jpg")
    os.remove("cobra.jpg")

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
        img = await borg.download_media(dc.media, path)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(dc.media, path)
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

