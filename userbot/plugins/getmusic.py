#Thanks to catuserbot for this plugin 
# modified by @No_OnE_Kn0wS_Me 
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
from userbot.plugins import catmusic , catmusicvideo
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
        await event.edit("wi8..! I am finding your song....")
    elif reply.message:
        query = reply.message
        await event.edit("wi8..! I am finding your song....")
    else:
    	await event.edit("`What I am Supposed to find `")
    	return
    
    await catmusic(str(query),"128k")
    l = glob.glob("*.mp3")
    if l:
        await event.edit("yeah..! i found something wi8..🥰")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`")
    loa = l[0]    
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption="`Audio File Medium Quality Successfully Uploaded By:`@uSe_DaRk_PrInCe",
                reply_to=reply_to_id
            )
    await event.delete()
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3",shell=True)
    
@borg.on(admin_cmd(pattern="song320(?: |$)(.*)"))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("wi8..! I am finding your song....")
    elif reply.message:
        query = reply.message
        await event.edit("wi8..! I am finding your song....")
    else:
    	await event.edit("`What I am Supposed to find `")
    	return
    
    await catmusic(str(query),"320k")
    l = glob.glob("*.mp3")
    if l:
        await event.edit("yeah..! i found something wi8..🥰")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`")
    loa = l[0]    
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption="Audio File HQ Successfully Uploaded By:`@uSe_DaRk_PrInCe",
                reply_to=reply_to_id
            )
    await event.delete()
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3",shell=True)    
    
@borg.on(admin_cmd(pattern="videosong(?: |$)(.*)"))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("wi8..! I am finding your videosong....")
    elif reply.message:
        query = reply.message
        await event.edit("wi8..! I am finding your videosong....")
    else:
        await event.edit("What I am Supposed to find")
        return
    await catmusicvideo(query)
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
                caption="`Video File Successfully Uploaded By:` @uSe_DaRk_PrInCe",
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
    

CMD_HELP.update({"getmusic":
    "`.song` query or `.song` reply to song name :\
    \nUSAGE:finds the song you entered in query and sends it in medium quality\
    `.song320` query or `.song320` reply to song name :\
     \nUSAGE:finds the song you entered in query and sends it in High Quality\
    `.videosong` query or `.videosong` reply to song name :\
    \nUSAGE:finds the Video song you entered in query and sends it As A video File"
})    
