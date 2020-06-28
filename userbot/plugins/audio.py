
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="ad ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("```reply to media message```")
       return
    chat = "@dwnmp3Bot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=507379365))
              await borg.send_message(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @AudioTubeBot and try again```")
              return
          await event.delete()
          await borg.send_file(event.chat_id, response.message.media)
