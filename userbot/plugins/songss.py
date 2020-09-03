# plugin made by @hellboi_atul
# Copyright (C) DARK COBRA 2020.
# if you change this line you are gay...bc fuck off!

from telethon import events
import asyncio
#from userbot.utils import admin_cmd
from userbot.events import register 
from userbot import bot, CMD_HELP
from telethon.errors.rpcerrorlist import YouBlockedUserError
import os
try:
 import subprocess
except:
 os.system("pip install instantmusic")



os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s "+name)



@register(outgoing=True, pattern="^.gaana(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@FindMusicPleaseBot"
    await event.edit("```Getting Your Music Ser```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await event.edit("`Downloading, Stay Tuned.....`")
          try:
              msg = await conv.send_message(link)
              response = await conv.get_response()
              respond = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
              
         
          except YouBlockedUserError:
              await event.reply("```Please unblock @FindMusicPleaseBot and try again```")
              return
          await gaana.edit("`Sending Your Music...weit!😎`")
          await asyncio.sleep(3)
          await bot.send_file(gaana.chat_id, respond)
    await gaana.client.delete_messages(conv.chat_id,
                                       [msg.id, response.id, respond.id])
    await gaana.delete()

         
