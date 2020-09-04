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
async def SendMusicPleaseBot(gaana):
    if gaana.fwd_from:
        return
    song = netase.pattern_match.group(1)
    chat = "@SendMusicPleaseBot"
    link = f"{song}"
    await netase.edit("```Getting Your Music```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await gaana.edit("`Downloading...Please wait`")
          try:
              msg = await conv.send_message(link)
              response = await conv.get_response()
              respond = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await netase.edit("```Please unblock @SendmusicpleaseBot and try again```")
              return
          await gaana.edit("`Sending Your Music...weit!😎`")
          await asyncio.sleep(3)
          await bot.send_file(gaana.chat_id, respond)
    await netase.client.delete_messages(conv.chat_id,
                                       [msg.id, response.id, respond.id])
    await gaana.delete()
