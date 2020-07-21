"""Corona: Avaible commands: .ripper <cname>
"""
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="ripper ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    chat = "@mrhacker_genuine_bot"
    await event.edit("```Thankyou User Reported @sensible_userbot Ripper Team Will Check This And If user Found So That User Will Be Globally Banned...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1254445279))
              await event.client.send_message(chat, "{}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Abey (@mrhacker_genuine_bot) Ko Unblock Kar```")
              return
          if response.text.startswith("Ripper"):
             await event.edit("😐**Abe Lode Code Churane Aya Hei kya 😎Bhak bhosdike")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)