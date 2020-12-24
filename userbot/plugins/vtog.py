from PIL import Image
import sys
import os
from userbot.utils import admin_cmd
from userbot import bot 
import moviepy.editor as m
if not os.path.isdir("./dco/"):
    os.makedirs("./dco/")


#made by @THE_B_LACK_HAT #team DC
@bot.on(admin_cmd(pattern=r"vtog"))
async def vtog(event):
    path = "viddck"


    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)
    
    file_name = "gif.gif"

    clip = (m.VideoFileClip(lol).subclip((4.3),(5.8)).resize(0.3))
    clip.write_gif(file_name) 

    
   
    hehe = path + "/" + file_name
   
    await borg.send_file(event.chat_id, file_name)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
            
            
    hoi = await event.delete()