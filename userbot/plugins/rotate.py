import os
#MADE BY SHIVAM DONT KANG
import cv2
from userbot import CMD_HELP
#MADE BY SHIVAM DONT KANG
#MADE BY SHIVAM DONT KANG
from telethon.tl.types import MessageMediaPhoto
from userbot.utils import admin_cmd
from userbot import bot 
from userbot import bot as borg
import os , shutil

from PIL import Image
sedpath = "./s_h_1_v_a_m/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)
@borg.on(admin_cmd(pattern=r"rotate"))
async def hmm(event):
    s=event.text
    h=s[8:]
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    window_name = 'Made By Shivam'
    img = Image.open(img)
    rotate_img= img.rotate(int(h))
    rotate_img.save("s_h_1_v_a_m_s.png")
    await event.client.send_file(event.chat_id, "s_h_1_v_a_m_s.png", force_document=False, reply_to=event.reply_to_msg_id)
    shutil.rmtree(sedpath)
    os.remove("s_h_1_v_a_m_s.png")
