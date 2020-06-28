
import os

import random
from userbot.utils import admin_cmd

from tswift import Song
from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
import time





@borg.on(admin_cmd(outgoing=True, pattern="slyrics (.*)"))
async def _(event):
    await event.edit("wi8..! I am searching your lyrics....`")
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply.text:
        query = reply.message
    else:
    	await event.edit("`What I am Supposed to find `")
    	return
    
    song = ""
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "Couldn't find any lyrics for that song! try with artist name along with song if still doesnt work "
    else:
        reply = "lyrics not found! try with artist name along with song if still doesnt work"
        
    if len(reply) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(reply)) as out_file:
            out_file.name = "lyrics.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=query,
                reply_to=reply_to_id
            )
            await event.delete()
    else:
        await event.edit(reply)       

