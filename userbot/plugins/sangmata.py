# -0,0 +1,96 @@
# Made For DARK COBRA and TELEBOT...
# Made by team cobra with @xditya
# Retrieves the name history and the username history of the replied user..
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd
from userbot import bot, CMD_HELP

@borg.on(admin_cmd(pattern="sg ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("Reply to any user message.")
       return
    reply_message = await event.get_reply_message() 
    chat = "Sangmatainfo_bot"
    sender = reply_message.sender.id
    if reply_message.sender.bot:
       await event.edit("Reply to actual users message.")
       return
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              #await conv.send_message("/search_id {}".format(sender))
              response1 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response3 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await conv.send_message("/search_id {}".format(sender))
              response1 = await response1 
              response2 = await response2 
              response3= await response3 
          except YouBlockedUserError: 
              await event.reply("Please unblock ( @Sangmatainfo_bot ) ")
              return
          if response1.text.startswith("No records found"):
             await event.edit("User never changed his Username...")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response2.message)
             
             await event.client.send_message(event.chat_id, response3.message)


CMD_HELP.update(
    {
        "sangmata": "__**PLUGIN NAME :** sangmata__\
    \n\n📌** CMD ★** `.sg`\
    \n**USAGE   ★  **Retrieves the name and username history of the replied user even if he has forwarded message privacy..! This may not always work as perfect it should be..if doesn't then try once again.."
    }
)
