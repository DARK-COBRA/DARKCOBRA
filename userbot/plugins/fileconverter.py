"""plugin made for reading nd  exploting message in tg {i}reveal <reply to file>"""
# originally made by @ItzSjDude All Rights reserved!!
#  Added Paste System by @danish_00
# All Credits - @ItzSjDude  #Added Paste System by @danish_00
# @ItzSjDude
# @ItzSjDude
#  Added Paste System by @danish_00

import os, requests, re
from userbot import CMD_HELP, bot
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"open", outgoing=True))
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    c = a.read()
    a.close()
    a = await event.reply("Reading file...")
    if len(c) >= 4096:            
            await event.edit("output file too large lemme paste it 😜😜")
            out = c
            url = "https://del.dog/documents"
            r = requests.post(url, data=out.encode("UTF-8")).json()
            url = f"https://del.dog/{r['key']}"
            await event.edit(
                f"Pasted to {url}", link_preview=False)            
            await a.delete()
    else:
        await event.client.send_message(event.chat_id, f"{c}")
        await a.delete()
    os.remove(b)


@borg.on(admin_cmd(pattern="doc ?(.*)"))
async def get(event):
    name = event.text[5:]
    if name is None:
        await event.edit("reply to text message as .ttf <file name>")
        return
    m = await event.get_reply_message()
    if m.text:
        with open(name, "w") as f:
            f.write(m.message)
        await event.delete()
        await event.client.send_file(event.chat_id, name, force_document=True)
        os.remove(name)
    else:
        await event.edit("reply to text message as .doc <file name.extension>")


CMD_HELP.update(
    {
        "fileconverter": "PLUGIN NAME : fileconverter\
    \n\n📌 CMD ★ .open\
    \nUSAGE   ★  open files as text (id the amount of words r resonable)\
    \n\n📌 CMD ★ .doc <file name.extension> <reply to any text/media>\
    \nUSAGE   ★  Create a document of anything (example:- .doc dc.mp4, .doc dc.txt, .doc dc.webp)"
    }
)
