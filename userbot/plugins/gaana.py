
# Port to UserBot
#ported and modified to DARK COBRA by @hellboi-atul
#Copyright (C) 2020 azrim.

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
    


@register(outgoing=True, pattern="^.netease(?: |$)(.*)")
async def WooMai(netase):
    if netase.fwd_from:
        return
    song = netase.pattern_match.group(1)
    chat = "@WooMaiBot"
    link = f"/netease {song}"
    await netase.reply("```Let me search for the music you are looking for..```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await netase.reply("`Downloading...it would take a few seconds..stay tuned`")
          try:
              msg = await conv.send_message(link)
              response = await conv.get_response()
              respond = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await netase.reply("```Please unblock @WooMaiBot and try again```")
              return
          await netase.reply("`Sending your music🤗...Thanks for using DARK COBRA song plugin..`")
          await asyncio.sleep(3)
          await bot.send_file(netase.chat_id, respond)
    await netase.client.delete_messages(conv.chat_id,
                                       [msg.id, response.id, respond.id])
    await netase.delete()



    
CMD_HELP.update({
       
       
CMD_HELP.update({

        "music":

        ".spd`<Artist - Song Title>\

            \nUsage:For searching songs from Spotify.\

            \n\n`.netease` <Artist - Song Title>\

            \nUsage:Download music with @WooMaiBot\

            \n\n`.dzd` <Spotify/Deezer Link>\

            \nUsage:Download music from Spotify or Deezer.\

            \n\n`.deezload` <spotify/deezer link> <Format>\

            \nUsage: Download music from deezer.\

            \n\n Well deezer is not available in India so create an deezer account using vpn. Set DEEZER_ARL_TOKEN in vars to make this work.\

            \n\n *Format= `FLAC`, `MP3_320`, `MP3_256`, `MP3_128`.\
            
             \n\n\n Guide:Video guide of arl token: [here](https://www.youtube.com/watch?v=O6PRT47_yds&feature=youtu.be) or Read [This](https://notabug.org/RemixDevs/DeezloaderRemix/wiki/Login+via+userToken)."
        
})


