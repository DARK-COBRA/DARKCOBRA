# Copyright (C) 2020 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Port from UniBorg to Userbot by @danish_00

import math
import asyncio
import os
import time
import zipfile
import re
import hashlib
from datetime import date
from telethon.tl.types import DocumentAttributeFilename

from userbot import CMD_HELP, bot
from userbot.events import register

TEMP_DOWNLOAD_DIRECTORY = './downloads/'
ZIP_DOWNLOAD_DIRECTORY = './downloads/zip'

# ====================
today = date.today()
# ====================


def humanbytes(size: int) -> str:
    if size is None or isinstance(size, str):
        return ""

    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(seconds: int) -> str:
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " day(s), ") if days else "") +
        ((str(hours) + " hour(s), ") if hours else "") +
        ((str(minutes) + " minute(s), ") if minutes else "") +
        ((str(seconds) + " second(s), ") if seconds else "")
    )
    return tmp[:-2]


async def progress(
    current, total, gdrive, start, prog_type,
    file_name=None, is_cancelled=False
):
    now = time.time()
    diff = now - start
    if is_cancelled is True:
        raise CancelProcess

    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff)
        eta = round((total - current) / speed)
        if 'upload' in prog_type.lower():
            status = 'Uploading'
        elif 'download' in prog_type.lower():
            status = 'Downloading'
        else:
            status = 'Unknown'
        progress_str = "`{0}` | [{1}{2}] `{3}%`".format(
            status,
            ''.join(["■" for i in range(
                    math.floor(percentage / 10))]),
            ''.join(["▨" for i in range(
                    10 - math.floor(percentage / 10))]),
            round(percentage, 2))
        tmp = (
            f"{progress_str}\n"
            f"`{humanbytes(current)} of {humanbytes(total)}"
            f" @ {humanbytes(speed)}`\n"
            f"`ETA` -> {time_formatter(eta)}\n"
            f"`Duration` -> {time_formatter(elapsed_time)}"
        )
        await gdrive.edit(f"`{prog_type}`\n\n"
                          f"`Status`\n{tmp}")


@register(outgoing=True, pattern=r"^\.compress(?: |$)(.*)")
async def _(event):
    # Prevent Channel Bug to use update
    if event.is_channel and not event.is_group:
        await event.edit("`Compress Command isn't permitted on channels`")
        return
    if event.fwd_from:
        return
    if not event.is_reply:
        await event.edit("`Reply to a file to compress it.`")
        return
    mone = await event.edit("`Processing...`")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        try:
            c_time = time.time()
            downloaded_file_name = await bot.download_media(
                reply_message,
                TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "[DOWNLOADING]")
                ),
            )
            directory_name = downloaded_file_name
            await event.edit(
                f"Downloaded to `{directory_name}`" "`\ncompressing file...`"
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await mone.edit(str(e))
    zipfile.ZipFile(directory_name + ".zip", "w", zipfile.ZIP_DEFLATED).write(
        directory_name
    )
    c_time = time.time()
    await bot.send_file(
        event.chat_id,
        directory_name + ".zip",
        force_document=True,
        allow_cache=False,
        reply_to=event.message.id,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, mone, c_time, "[UPLOADING]")
        ),
    )
    await event.edit("`Done!!`")
    await asyncio.sleep(7)
    await event.delete()


@register(outgoing=True, pattern=r"^\.addzip(?: |$)(.*)")
async def addzip(add):
    """ Copyright (c) 2020 azrim @github"""
    # Prevent Channel Bug to use update
    if add.is_channel and not add.is_group:
        await add.edit("`Command isn't permitted on channels`")
        return
    if add.fwd_from:
        return
    if not add.is_reply:
        await add.edit("`Reply to a file to compress it.`")
        return
    mone = await add.edit("`Processing...`")
    if not os.path.isdir(ZIP_DOWNLOAD_DIRECTORY):
        os.makedirs(ZIP_DOWNLOAD_DIRECTORY)
    if add.reply_to_msg_id:
        reply_message = await add.get_reply_message()
        try:
            c_time = time.time()
            downloaded_file_name = await bot.download_media(
                reply_message,
                ZIP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "[DOWNLOADING]")
                ),
            )
            success = str(downloaded_file_name).replace("./zips/", "")
            await add.edit(f"`{success} Successfully added to list`")
        except Exception as e:  # pylint:disable=C0103,W0703
            await mone.edit(str(e))
            return


@register(outgoing=True, pattern=r"^\.upzip(?: |$)(.*)")
async def upload_zip(up):
    if not os.path.isdir(ZIP_DOWNLOAD_DIRECTORY):
        await up.edit("`Files not found`")
        return
    mone = await up.edit("`Zipping File...`")
    input_str = up.pattern_match.group(1)
    curdate = today.strftime("%m%d%y")
    title = str(input_str) if input_str else "zipfile" + f"{curdate}"
    zipf = zipfile.ZipFile(title + ".zip", "w", zipfile.ZIP_DEFLATED)
    zipdir(ZIP_DOWNLOAD_DIRECTORY, zipf)
    zipf.close()
    c_time = time.time()
    await bot.send_file(
        up.chat_id,
        title + ".zip",
        force_document=True,
        allow_cache=False,
        reply_to=up.message.id,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, mone, c_time, "[UPLOADING]", input_str)
        ),
    )
    os.rmdir(ZIP_DOWNLOAD_DIRECTORY)
    await up.delete()


@register(outgoing=True, pattern=r"^\.rmzip(?: |$)(.*)")
async def remove_dir(rm):
    if not os.path.isdir(ZIP_DOWNLOAD_DIRECTORY):
        await rm.edit("`Directory not found`")
        return
    os.rmdir(ZIP_DOWNLOAD_DIRECTORY)
    await rm.edit("`Zip list removed`")


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            os.remove(os.path.join(root, file))


CMD_HELP.update(
    {
        "zipfile": ".compress **[optional: <reply to file>]**\
            \nUsage: make files to zip.\
            \n.addzip **<reply to file>**\
            \nUsage: add files to zip list.\
            \n.upzip **[optional: <zip title>]**\
            \nUsage: upload zip list.\
            \n.rmzip **[optional: <zip title>]**\
            \nUsage: clear zip list."
    }
)
