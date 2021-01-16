# Credits to Friday 
# by @krish1303y

import os
from shutil import rmtree
import re
import cv2
import numpy as np

from PIL import Image

from validators.url import url
from telethon.tl.types import MessageMediaPhoto



from userbot.utils import admin_cmd, sudo_cmd

path = os.path.join("./temp/", "temp.mp4")

import math
def humanbytes(size):
    """Input size in bytes,
    outputs in a human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    gokueson = 2 ** 30
    songoku = 0
    yes = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > gokueson:
        size /= gokueson
        songoku += 1
    return str(round(size, 2)) + " " + yes[songoku] + "B"


def time_formatter(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " day(s), ") if days else "")
        + ((str(hours) + " hour(s), ") if hours else "")
        + ((str(minutes) + " minute(s), ") if minutes else "")
        + ((str(seconds) + " second(s), ") if seconds else "")
        + ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    )
    return tmp[:-2]




import asyncio
import time
# Thanks To Userge-X
async def progress(current, total, event, start, type_of_ps, file_name=None):
    """Generic progress_callback for uploads and downloads."""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current != total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "[{0}{1}] {2}%\n".format(
            "".join(["▰" for i in range(math.floor(percentage / 10))]),
            "".join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            await event.edit(
                "{}\nFile Name: `{}`\n{}".format(type_of_ps, file_name, tmp)
            )
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


async def spinn_converter(event, borg):
    spinner = await event.get_reply_message()
    if not (
        spinner.gif
        or spinner.audio
        or spinner.voice
        or spinner.video
        or spinner.video_note
        or spinner.photo
        or spinner.sticker
    ):
        await event.edit("`Format Not Supported.`")
        return
    else:
        try:
            c_time = time.time()
            downloaded_file_name = await borg.download_media(
                spinner.media,
                path,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, event, c_time, "Hehe")
                ),
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
        else:
            await event.edit(
                "Yeah `{}`.".format(downloaded_file_name)
            )
    if not os.path.exists(downloaded_file_name):
        await event.edit("Download Unsucessfull :(")
        return
    if spinner and spinner.photo:
        spinner_final = downloaded_file_name
    elif spinner.sticker and spinner.sticker.mime_type == "application/x-tgsticker":
        rpath = downloaded_file_name
        image_name20 = os.path.join(path, "SED.png")
        cmd = f"lottie_convert.py --frame 0 -if lottie -of png {downloaded_file_name} {image_name20}"
        stdout, stderr = (await spinner(cmd))[:2]
        os.remove(rpath)
        spinner_final = image_name20
    elif spinner.sticker and spinner.sticker.mime_type == "image/webp":
        pathofsticker2 = downloaded_file_name
        image_new_path = path + "image.png"
        os.rename(pathofsticker2, image_new_path)
        if not os.path.exists(image_new_path):
            await event.edit("`Wasn't Able To Fetch Shot.`")
            return
        spinner_final = image_new_path
    elif spinner.audio:
        ig = downloaded_file_name
        cool = path + "stark.mp3"
        imgpath = path + "starky.jpg"
        os.rename(ig, cool)
        await spinner(f"ffmpeg -i {cool} -filter:v scale=500:500 -an {imgpath}")
        os.remove(ig)
        if not os.path.exists(imgpath):
            await event.edit("`Wasn't Able To Fetch Shot.`")
            return
        spinner_final = imgpath
    elif spinner.gif or spinner.video or spinner.video_note:
        ig2 = downloaded_file_name
        jpg_file = os.path.join(path, "image.jpg")
        await take_screen_shot(ig2, 0, jpg_file)
        os.remove(ig2)
        if not os.path.exists(jpg_file):
            await event.edit("`Couldn't Fetch. SS`")
            return
        spinner_final = jpg_file
    await event.edit("`Almost Completed.`")
    return spinner_final


import os
import re
import shlex

from os.path import basename
from typing import Tuple
from userbot import bot as borg

from telethon.tl.functions.messages import ImportChatInviteRequest as Get
lovepath = "./keinshin/"
if not os.path.isdir(lovepath):
    os.makedirs(lovepath)

# Thanks To Userge X
async def spinner(spin: str) -> Tuple[str, str, int, int]:
    """ run command in terminal """
    args = shlex.split(spin)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


from pymediainfo import MediaInfo

async def cropper(cropper: str, path: str):
    media_info = MediaInfo.parse(cropper)
    for track in media_info.tracks:
        if track.track_type == "Video":
            aspect_ratio = track.display_aspect_ratio
            height = track.height
            width = track.width
    if aspect_ratio != 1:
        crop_by = width if (height > width) else height
        os.system(f'ffmpeg -i {cropper} -vf "crop={crop_by}:{crop_by}" {path}')
        os.remove(cropper)
    else:
        os.rename(cropper, path)    

@borg.on(admin_cmd(pattern=r"turn ?(.*)"))
@borg.on(sudo_cmd(pattern=r"turn ?(.*)", allow_sudo=True))
async def _(message):
    reply = await message.get_reply_message()
    i_can = {"1": 1, "2": 3, "3": 6, "4": 12, "5": 24, "6": 60, '7': 70, "8": 36, "9": 300, "10":33000, "11": 10000, "12":555555, "13": 5566556656565, "14": 4455454545445454545, "15":4444444444}
    me = message.pattern_match.group(1)
    spi_this = f"{me}"
    if not reply:
        await message.edit("`Are You Retard Is This Image?.`")
        return
    else:
        if me:
            lol = i_can[spi_this]
        else:
            lol = 1
    pic_loc = await spinn_converter(message, borg)
    if not pic_loc:
        await message.edit("`Are You Retard Is This Image?.`")
        return
    await message.edit("`Hehehe`")
    how_time = 1
    # Thanks To Friday
    path = "resources/disc/"
    if os.path.exists(path):
        rmtree(path, ignore_errors=True)
    os.mkdir(path)
    im = Image.open(pic_loc)
    if im.mode != "RGB":
        im = im.convert("RGB")
    # Rotating pic by given angle and saving
    for yeah, nums in enumerate(range(1, 360, lol), start=0):
        really = im.rotate(nums * how_time)
        really.save(os.path.join(path, "spinx%s.jpg" % yeah))
    thats_like_a_vid = os.path.join(path, "out.mp4")
    # ;__; Maths lol, y = mx + c
    fram_rate = int(((90 / 59) * lol) + (1680 / 59))
    # https://stackoverflow.com/questions/20847674/ffmpeg-libx264-height-not-divisible-by-2
    await spinner(
        f'ffmpeg -framerate {fram_rate} -i {path}spinx%d.jpg -c:v libx264 -preset ultrafast -vf "crop=trunc(iw/2)*2:trunc(ih/2)*2" -pix_fmt yuv420p {thats_like_a_vid}'
    )
    if os.path.exists(thats_like_a_vid):
        round_vid = os.path.join(path, "lol.mp4")
        await cropper(thats_like_a_vid, round_vid)
        await borg.send_file(
            message.chat_id, round_vid, video_note=True, reply_to=reply.id
        )
        await message.delete()
    os.remove(pic_loc)
    rmtree(path, ignore_errors=True)
