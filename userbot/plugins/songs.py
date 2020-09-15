# Ported here by @hellboi_atul
# credit CAT USERBOT
# 🔨🛠DARK COBRA🎼🎧🎧
import requests
from bs4 import BeautifulSoup
from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
from userbot.utils import admin_cmd , sudo_cmd
import glob
import os  
from userbot import CMD_HELP
from userbot.plugins import darkmusic , darkmusicvideo
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeVideo

@borg.on(admin_cmd(pattern="song(?: |$)(.*)"))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("weit, let me search for the song you are looking for....")
    elif reply.message:
        query = reply.message
        await event.edit("weit..searching")
    else:
    	await event.edit("`What am I Supposed to find sir?! `")
    	return
    
    await darkmusic(str(query),"128k")
    l = glob.glob("*.mp3")
    if l:
        await event.edit("Sir, I found something related to your query weit.. Let me send it here..!!")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`😣😣 ")
    loa = l[0]    
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption="`@Dark_cobra_support`",
                reply_to=reply_to_id
            )
    await event.delete()
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3",shell=True)
    
@borg.on(admin_cmd(pattern="songg(?: |$)(.*)"))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("Let me search for yor query..")
    elif reply.message:
        query = reply.message
        await event.edit("Searching...!!!🤖")
    else:
    	await event.edit("`What am I Supposed to find `")
    	return
    
    await darkmusic(str(query),"320k")
    l = glob.glob("*.mp3")
    if l:
        await event.edit("Sir, I found something related to your query..weit let me send it here!!!")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`😣😣")
    loa = l[0]    
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption="Audio File Successfully Uploaded",
                reply_to=reply_to_id
            )
    await event.delete()
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3",shell=True)    
    
@borg.on(admin_cmd(pattern="vs(?: |$)(.*)"))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("Searching🤖🤖..!!")
    elif reply.message:
        query = reply.message
        await event.edit("Searching...🤖....!")
    else:
        await event.edit("What am I Supposed to find")
        return
    await darkmusicvideo(query)
    l = glob.glob(("*.mp4")) + glob.glob(("*.mkv")) + glob.glob(("*.webm")) 
    if l:
        await event.edit("yeah..! i found something wi8..🥰")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`")
    loa = l[0]  
    metadata = extractMetadata(createParser(loa))
    duration = 0
    width = 0
    height = 0
    if metadata.has("duration"):
        duration = metadata.get("duration").seconds
    if metadata.has("width"):
        width = metadata.get("width")
    if metadata.has("height"):
        height = metadata.get("height")
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption="`Video File Successfully Uploaded `",
                supports_streaming=True,
                reply_to=reply_to_id,
                attributes=[DocumentAttributeVideo(
                                duration=duration,
                                w=width,
                                h=height,
                                round_message=False,
                                supports_streaming=True,
                            )],
            )
    await event.delete()
    os.system("rm -rf *.mkv")
    os.system("rm -rf *.mp4")
    os.system("rm -rf *.webm")    
    

CMD_HELP.update({"song":
    "`.song` query or `.song` reply to song name :\
    \nUSAGE:finds the song you entered in query and sends it in medium quality\
    `.songg` query or `.songg` reply to song name :\
     \nUSAGE:finds the song you entered in query and sends it in High Quality\
    `.videosong` query or `.vs` reply to song name :\
    \nUSAGE:finds the Video song you entered in query and sends it As A video File"
})    
