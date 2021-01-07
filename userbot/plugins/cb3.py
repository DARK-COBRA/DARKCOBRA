import os
#MADE BY SHIVAM DONT KANG
import cv2
from userbot import CMD_HELP
#MADE BY SHIVAM DONT KANG
#MADE BY SHIVAM DONT KANG
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto
from userbot.utils import admin_cmd
from userbot import bot 
from userbot import bot as borg
import os , shutil
sedpath = "./s_h_i_v_a_m_Javes/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)
@borg.on(admin_cmd(pattern=r"cblur"))
async def hom(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    await event.delete()
    sed = await event.get_reply_message()
    linc = event.text
    links=linc[7:]
    kaboom,kabum=links.split(",")

    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    sh_1_vam=(int(kaboom),int(kabum))
    #image=cv2.imshow(window_name, image)
    spath = img
    image = cv2.imread(spath)
    image = cv2.blur(image, sh_1_vam)
    cv2.imwrite("s_h_i_v_a_m_s.jpg", image)
    #await borg.send_file(event.chat_id,"s_h_i_v_a_m.png")
    #await event.client.send_file(event.chat_id, "s_h_i_v_a_m.png", force_document=True, reply_to=event.reply_to_msg_id)
    await event.client.send_file(event.chat_id, "s_h_i_v_a_m_s.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    shutil.rmtree(sedpath)
    os.remove("s_h_i_v_a_m_s.jpg")
