from PIL import Image
import sys
import os
from userbot.utils import admin_cmd, sudo_cmd
from userbot import bot, CMD_HELP

if not os.path.isdir("./dcobra/"):
    os.makedirs("./dcobra/")

# made by  @THE_B_LACK_HAT 
# modified nd enhanced by @shivam_patel
# @danish_00 did nothing 🙃🙂




@bot.on(admin_cmd(pattern=r"thug"))
@bot.on(sudo_cmd(pattern=r"thug", outgoing=True))

async def scan(event):
    path = "dcobra"
     
    kk = await event.edit("HeHe Lets give a Mask 🤪")

    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)

    import cv2

    os.system('wget https://datreon.000webhostapp.com/haarcascade_frontalface_default.xml')    
    
    os.system('wget https://telegra.ph/file/8c47ddc5c368a1d4f4ee4.png')

    imagePath = lol
    
    maskPath = "8c47ddc5c368a1d4f4ee4.png"
    
    cascPath = "haarcascade_frontalface_default.xml"
   
    faceCascade = cv2.CascadeClassifier(cascPath)
   
    image = cv2.imread(imagePath)
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open(imagePath)
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "d449274b33387550508c4.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
            
    hoi = await event.delete()

            
            

   

@bot.on(admin_cmd(pattern=r"pru"))
@bot.on(sudo_cmd(pattern=r"pru", outgoing=True))

async def scan(event):
    path = "dcobra"
     
    kk = await event.edit("HeHe Lets give a Mask 🤪")

    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)


    import cv2

    os.system('wget https://datreon.000webhostapp.com/haarcascade_frontalface_default.xml')    
    
    os.system('wget https://telegra.ph/file/f061c861ba85fbb23a51e.png')

    imagePath = lol
    
    maskPath = "f061c861ba85fbb23a51e.png"
    
    cascPath = "haarcascade_frontalface_default.xml"
   
    faceCascade = cv2.CascadeClassifier(cascPath)
   
    image = cv2.imread(imagePath)
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open(imagePath)
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "pro.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
            
            
    hoi = await event.delete()

            



@bot.on(admin_cmd(pattern=r"oxy"))
@bot.on(sudo_cmd(pattern=r"oxy", outgoing=True))

async def scan(event):
    path = "dcobra"
     
    kk = await event.edit("HeHe Lets give a Mask 🤪")


    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)


    import cv2

    os.system('wget https://datreon.000webhostapp.com/haarcascade_frontalface_default.xml')    
    
    os.system('wget https://telegra.ph/file/df2d739544595ae337642.png')

    imagePath = lol
    
    maskPath = "df2d739544595ae337642.png"
    
    cascPath = "haarcascade_frontalface_default.xml"
   
    faceCascade = cv2.CascadeClassifier(cascPath)
   
    image = cv2.imread(imagePath)
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open(imagePath)
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "old.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
            
            
    hoi = await event.delete()



@bot.on(admin_cmd(pattern=r"gold"))
@bot.on(sudo_cmd(pattern=r"gold", outgoing=True))

async def scan(event):
    path = "dcobra"
     
    kk = await event.edit("HeHe Lets give a Mask 🤪")


    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)


    import cv2

    os.system('wget https://datreon.000webhostapp.com/haarcascade_frontalface_default.xml')    
    
    os.system('wget https://telegra.ph/file/4cc40d1e0846667488341.png')

    imagePath = lol
    
    maskPath = "4cc40d1e0846667488341.png"
    
    cascPath = "haarcascade_frontalface_default.xml"
   
    faceCascade = cv2.CascadeClassifier(cascPath)
   
    image = cv2.imread(imagePath)
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open(imagePath)
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "old.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
            
            
    hoi = await event.delete()



@bot.on(admin_cmd(pattern=r"old"))
@bot.on(sudo_cmd(pattern=r"old", outgoing=True))

async def scan(event):
    path = "dcobra"
     
    kk = await event.edit("HeHe Lets give a Mask 🤪")


    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)


    import cv2

    os.system('wget https://datreon.000webhostapp.com/haarcascade_frontalface_default.xml')    
    
    os.system('wget https://telegra.ph/file/55fcb205c6f8f4790585e.png')

    imagePath = lol
    
    maskPath = "55fcb205c6f8f4790585e.png"
    
    cascPath = "haarcascade_frontalface_default.xml"
   
    faceCascade = cv2.CascadeClassifier(cascPath)
   
    image = cv2.imread(imagePath)
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open(imagePath)
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "old.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
            
            
    hoi = await event.delete()



@bot.on(admin_cmd(pattern=r"krish"))
@bot.on(sudo_cmd(pattern=r"krish", outgoing=True))

async def scan(event):
    path = "dcobra"
     
    kk = await event.edit("HeHe Lets give a Mask 🤪")


    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)


    import cv2

    os.system('wget https://datreon.000webhostapp.com/haarcascade_frontalface_default.xml')    
    
    os.system('wget https://telegra.ph/file/54d2a267d411951b41a20.png')

    imagePath = lol
    
    maskPath = "54d2a267d411951b41a20.png"
    
    cascPath = "haarcascade_frontalface_default.xml"
   
    faceCascade = cv2.CascadeClassifier(cascPath)
   
    image = cv2.imread(imagePath)
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open(imagePath)
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "old.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
            
            
    hoi = await event.delete()
    
    
    
@bot.on(admin_cmd(pattern=r"cprotect"))
@bot.on(sudo_cmd(pattern=r"cprotect", outgoing=True))

async def scan(event):
    path = "dcobra"
     
    kk = await event.edit("HeHe Lets give a Mask 🤪")


    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)


    import cv2

    os.system('wget https://datreon.000webhostapp.com/haarcascade_frontalface_default.xml')    
    
    os.system('wget https://telegra.ph/file/b934a713abb321bd1a9fe.png')

    imagePath = lol
    
    maskPath = "b934a713abb321bd1a9fe.png"
    
    cascPath = "haarcascade_frontalface_default.xml"
   
    faceCascade = cv2.CascadeClassifier(cascPath)
   
    image = cv2.imread(imagePath)
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open(imagePath)
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "old.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
            
            
    hoi = await event.delete()
    
    
@bot.on(admin_cmd(pattern=r"cmask"))
@bot.on(sudo_cmd(pattern=r"cmask", outgoing=True))

async def scan(event):
    path = "dcobra"
     
    kk = await event.edit("HeHe Lets give a Mask 🤪")


    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)
    linc= event.text
    link=linc[7:]
    pic=linc[31:]
    import cv2

    os.system('wget https://datreon.000webhostapp.com/haarcascade_frontalface_default.xml')    
    
    os.system(f'wget {link}')
    
    imagePath = lol
      
    maskPath = f"{pic}"
     
    cascPath = "haarcascade_frontalface_default.xml"
   
    faceCascade = cv2.CascadeClassifier(cascPath)
   
    image = cv2.imread(imagePath)
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open(imagePath)
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "old.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
            
            
    hoi = await event.delete()



