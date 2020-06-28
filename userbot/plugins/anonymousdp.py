
import os

from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

from pySmartDL import SmartDL

from telethon.tl import functions

from userbot.utils import admin_cmd

import asyncio

import shutil 

import random, re



FONT_FILE_TO_USE = "Fonts/1942.ttf"

#Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = [
                         "https://telegra.ph/file/b9654916cb6d1a416417c.jpg",
                         "https://telegra.ph/file/b9654916cb6d1a416417c.jpg",
                        ]
@borg.on(admin_cmd(pattern="anonymousdp ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./FRIDAY/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            place_holder = None
    
    
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        current_time = datetime.now().strftime("\nWE ARE ANONYMOUS\nWE ARE LEGION\nWE DO NOT FORGIVE\nWE DO NOT FORGET\n\nTime: %H:%M:%S \n\nDate: %d/%m/%y")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 40)
        drawn_text.text((150,150), current_time, font=fnt, fill=(255,0,0))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=1)))
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            
            await asyncio.sleep(60)
        except:
            return
