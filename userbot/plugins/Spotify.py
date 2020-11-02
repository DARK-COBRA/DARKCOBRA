from telethon.tl.types import InputMessagesFilterMusic
from userbot.events import register

@register(outgoing=True, pattern="^.sptfy(?: |$)(.*)")

id = event.chat_id
chat = -1001271479322
song = f"{song}"
async for event in event.client.iter_messages(chat, search=song, limit=1, filter=InputMessagesFilterMusic):
    lol = event
    await event.client.send_file(id, lol, caption=event.message)
