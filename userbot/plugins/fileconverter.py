import os

from userbot import CMD_HELP
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern=r"open", outgoing=True))

async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    c = a.read()
    a.close()
    a = await event.reply("Reading file...")
    if len(c) > 4095:
        await a.edit("The Total words in this file is more than telegram limits.")
    else:
        await event.client.send_message(event.chat_id, f"{c}")
        await a.delete()
    os.remove(b)


@borg.on(admin_cmd(pattern="doc ?(.*)"))
async def get(event):
    name = event.text[5:]
    if name is None:
        await event.edit("reply to text message as `.ttf <file name>`")
        return
    m = await event.get_reply_message()
    if m.text:
        with open(name, "w") as f:
            f.write(m.message)
        await event.delete()
        await event.client.send_file(event.chat_id, name, force_document=True)
        os.remove(name)
    else:
        await event.edit("reply to text message as `.doc <file name.extension>`")


CMD_HELP.update(
    {
        "fileconverter": "__**PLUGIN NAME :** fileconverter__\
    \n\n📌** CMD ★** `.open`\
    \n**USAGE   ★  **open files as text (id the amount of words r resonable)\
    \n\n📌** CMD ★** `.doc <file name.extension> <reply to any text/media>`\
    \n**USAGE   ★  **Create a document of anything (example:- .doc dc.mp4, .doc dc.txt, .doc dc.webp)"
    }
)
