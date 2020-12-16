# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.utils import admin_cmd
from userbot import bot as javes

@javes.on(admin_cmd(pattern=r"tagall", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    shiv= event.text
    shivam=shiv[8:]
    mentions = f"{shivam}"
    chat = await event.get_input_chat()
    async for x in javes.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.edit(mentions)


@javes.on(admin_cmd(pattern=r"admin", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    shiv= event.text
    shivam=shiv[7:]
    mentions = f"{shivam}"
    chat = await event.get_input_chat()
    async for x in javes.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.edit(mentions)
    else:
        await event.edit(mentions)
    
