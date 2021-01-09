# Kang with credits..
# Team DC
from PIL import Image
import sys
import os
from userbot.utils import admin_cmd
from userbot import bot 
import moviepy.editor as m

if not os.path.isdir("./dcpath/"):
    os.makedirs("./dcpath/")


@bot.on(admin_cmd(pattern="gif ?(.*)"))
async def gifs(event):
    get = event.pattern_match.group(1)
    if not get:
       await event.edit("`.gif <text>`")
       return
    gifs = await bot.inline_query("gif", f"{get}")
    await gifs[0].click(event.chat.id, reply_to=event.reply_to_msg_id, silent=True ,hide_via=True)
    await event.delete()                         



#made by @THE_B_LACK_HAT #team DC
@bot.on(admin_cmd(pattern=r"vtog"))
async def vtog(event):
    path = "viddck"
    reply = await event.get_reply_message()
    lol = await borg.download_media(reply.media, path)
    file_name = "dc.gif"
    clip = (m.VideoFileClip(lol).subclip((4.3),(5.8)).resize(0.3))
    clip.write_gif(file_name)
    hehe = path + "/" + file_name
    await borg.send_file(event.chat_id, file_name)
    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)        
    hoi = await event.delete()
