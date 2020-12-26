
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
    #await event.edit(mentions)
    #await event.delete()
    if event.reply_to_msg_id:
        await javes.send_message(event.chat_id,mentions,reply_to=event.reply_to_msg_id)
    else:
        await javes.send_message(event.chat_id,mentions)
    await event.delete()
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
    #await event.edit(mentions)
    #await event.delete()
    if event.reply_to_msg_id:
        await javes.send_message(event.chat_id,mentions,reply_to=event.reply_to_msg_id)
    else:
        await javes.send_message(event.chat_id,mentions)
    await event.delete()
