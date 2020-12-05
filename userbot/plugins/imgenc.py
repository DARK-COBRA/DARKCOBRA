# Made for DARK COBRA
# Thanks to @THE_B_LACK_HAT
# Kang with credits else gay..

from telethon.tl.types import MessageMediaPhoto
import os, urllib, requests, re, asyncio
from userbot.utils import admin_cmd
from userbot import CMD_HELP

DARKCOBRA = Config.DEEP_AI if Config.DEEP_AI else "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"

@bot.on(admin_cmd(pattern="enc (.*)", outgoing=True))
async def _(event):
    
               
    reply = await event.get_reply_message()
    if not reply:

        return await event.edit(
           "Reply to any image or non animated sticker !"
        )

    input_str = input_str = event.pattern_match.group(1)
    hm = input_str
    devent = await event.edit("yo let me downlaoad it....")
    media = await event.client.download_media(reply)
    if not media.endswith(("png", "jpg", "webp")):
        return await event.edit(
             "Reply to any image or non animated sticker !"
        )

    devent = await event.edit("styling the image sar...")
    r = requests.post(
        "https://api.deepai.org/api/neural-style",
        files={
            'style': f"{hm}",
            'content': open(media, "rb"),
            },
        headers={"api-key": DARKCOBRA},
    )

    os.remove(media)
    if "status" in r.json():
        return await devent.edit( r.json()["status"])
    r_json = r.json()['output_url']
    pic_id = r.json()['id']
    
    link = f"https://api.deepai.org/job-view-file/{pic_id}/inputs/image.jpg"
    result = f"{r_json}"
    
    await devent.delete()
    await borg.send_message(
        event.chat_id,
        file=result
    )



CMD_HELP.update(
    {
        "imgenc": "__**PLUGIN NAME :** imgenc__\
    \n\n📌** CMD ★** `.enc`\
    \n**USAGE   ★  **It combines to pics giving them an anime look..by default it doesn't needs the API but if it asks so then kindly restart your bot it will be fine as it is..\
    \n\n📌** How?? ★** [It can be used like this](https://telegra.ph/file/22a74d22cadd1b1c89e49.mp4)\
    \n**NOTE   ★  **Sorry for quality, made it like that so that it doesn't consume much of your data... Enjoy"
    }
)
