from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
import time
from userbot.utils import admin_cmd
import glob
import os
import spotdl
import subprocess
    

@borg.on(admin_cmd(pattern="song ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = event.pattern_match.group(1)
    cmnd = f"{cmd}"
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    subprocess.run(["spotdl", "-s", cmnd, "-q", "best"])
    subprocess.run(
        'for f in *.opus; do      mv -- "$f" "${f%.opus}.mp3"; done',
        shell=True)
    l = glob.glob("*.mp3")
    loa = l[0]
    await event.edit("`Yes 🌚 I found the song..🎶`")
    await event.client.send_file(
        event.chat_id,
        loa,
        force_document=False,
        allow_cache=False,
        supports_streaming=True,
        caption=cmd,
        reply_to=reply_to_id,
    )
    subprocess.run("rm -rf *.mp3", shell=True)
