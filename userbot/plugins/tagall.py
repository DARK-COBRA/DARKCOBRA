# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2



from telethon.tl.types import ChannelParticipantsAdmins
from userbot.utils import admin_cmd
from userbot import CMD_HELP

@borg.on(admin_cmd(pattern=r"tagall", outgoing=True))
@borg.on(admin_cmd(pattern=r"tagall", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "Check that msg 🙂🙂 "
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, 75):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.edit(mentions)
   


"""@borg.on(admin_cmd(pattern=r"admin", outgoing=True))
@borg.on(admin_cmd(pattern=r"admin", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "Admins : "
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.edit(mentions)
    
"""
CMD_HELP.update(
    {
        "tagall": ".tagall\
    \nReplay any msg with .tagall nd u'll tag top 75 active mem of a grp."
    

})
