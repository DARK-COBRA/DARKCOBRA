
 
"""
designed By @Krishna_Singhal in userge
ported to telethon by @mrconfused and @sandy1709
"""

import os

from glitch_this import ImageGlitcher
from PIL import Image
from telethon import functions, types

from .. import CMD_HELP, LOGS
from ..utils import admin_cmd, edit_or_reply
from . import runcmd, take_screen_shot


@borg.on(admin_cmd(outgoing=True, pattern="(glitch|glitchs)(?: |$)(.*)"))
async def glitch(dark):
    cmd = dark.pattern_match.group(1)
    darkinput = dark.pattern_match.group(2)
    reply = await dark.get_reply_message()
    darkid = dark.reply_to_msg_id
    dark = await edit_or_reply(dark, "```Weit..let me glitch this```")
    if not (reply and (reply.media)):
        await dark.edit("`Media not found...`")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    darksticker = await reply.download_media(file="./temp/")
    if not darksticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg")):
        os.remove(darksticker)
        await dark.edit("`Media not found...`")
        return
    os.path.join("./temp/", "glitch.png")
    if darkinput:
        if not darkinput.isdigit():
            await dark.edit("`You input is invalid, check help`")
            return
        darkinput = int(darkinput)
        if not 0 < darkinput < 9:
            await dark.edit("`Invalid Range...`")
            return
    else:
        darkinput = 2
    if darksticker.endswith(".tgs"):
        darkfile = os.path.join("./temp/", "glitch.png")
        darkcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(darkcmd))[:2]
        if not os.path.lexists(darkfile):
            await dark.edit("`darksticker not found...`")
            LOGS.info(stdout + stderr)
        glitch_file = darkfile
    elif darksticker.endswith(".webp"):
        darkfile = os.path.join("./temp/", "glitch.png")
        os.rename(darksticker, darkfile)
        if not os.path.lexists(darkfile):
            await dark.edit("`darksticker not found... `")
            return
        glitch_file = darkfile
    elif darksticker.endswith(".mp4"):
        darkfile = os.path.join("./temp/", "glitch.png")
        await take_screen_shot(darksticker, 0, darkfile)
        if not os.path.lexists(darkfile):
            await cat.edit("```darksticker not found...```")
            return
        glitch_file = darkfile
    else:
        glitch_file = darksticker
    glitcher = ImageGlitcher()
    img = Image.open(glitch_file)
    if cmd == "glitchs":
        glitched = "./temp/" + "glitched.webp"
        glitch_img = glitcher.glitch_image(img, darkinput, color_offset=True)
        glitch_img.save(glitched)
        await borg.send_file(dark.chat_id, glitched, reply_to=catid)
        os.remove(glitched)
        await dark.delete()
    elif cmd == "glitch":
        Glitched = "./temp/" + "glitch.gif"
        glitch_img = glitcher.glitch_image(img, darkinput, color_offset=True, gif=True)
        DURATION = 200
        LOOP = 0
        glitch_img[0].save(
            Glitched,
            format="GIF",
            append_images=glitch_img[1:],
            save_all=True,
            duration=DURATION,
            loop=LOOP,
        )
        dark = await borg.send_file(dark.chat_id, Glitched, reply_to=darkid)
        await borg(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=dark.media.document.id,
                    access_hash=sandy.media.document.access_hash,
                    file_reference=sandy.media.document.file_reference,
                ),
                unsave=True,
            )
        )
        os.remove(Glitched)
        await dark.delete()
    for files in (darksticker, glitch_file):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "glitch": "**Plugin : **`glitch`\
    \n\n**Syntax : **`.glitch` reply to media file\
    \n**Usage :** glitches the given mediafile(gif , stickers , image, videos) to a gif and glitch range is from 1 to 8.\
    If nothing is mentioned then by default it is 2\
    \n\n**Syntax : **`.glitchs` reply to media file\
    \n**Usage :** glitches the given mediafile(gif , stickers , image, videos) to a sticker and glitch range is from 1 to 8.\
    If nothing is mentioned then by default it is 2\
    "
    }
)
