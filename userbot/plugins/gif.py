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
async def gifs(search):
    get = search.pattern_match.group(1)
    if not get:
       if search.is_reply:
           what = (await search.get_reply_message()).message
       else:
           await search.edit("`Sir please give some query to search and download it for you..!`")
           return
    gifs = await bot.inline_query("gif", f"{get}")
    await gifs[0].click(search.chat.id,
                            reply_to=search.reply_to_msg_id,
                            silent=True if search.is_reply else False,
                            hide_via=True)
    await search.delete()






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
