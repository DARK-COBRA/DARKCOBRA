from telethon.tl.types import InputMessagesFilterMusic
from userbot.utils import admin_cmd
from telethon.tl.functions.messages import ImportChatInviteRequest


@borg.on(admin_cmd("sptfy ?(.*)"))
async def _(event):
    try:
        await event.client(ImportChatInviteRequest('DdR2SUvJPBouSW4QlbJU4g'))
    except Exception as ex:
        await event.reply(ex)

        return
    args = event.pattern_match.group(1)
    if not args:
        await event.edit("`Enter the song name please`")
        return
    chat = -1001271479322
    current_chat = event.chat_id
    current_msg = event.id
    try:
        async for event in event.client.iter_messages(chat, search=args, limit=1, filter=InputMessagesFilterMusic):
            await event.client.send_file(current_chat, event, caption=event.message)
    except:
        await event.reply("`Song not found.`")
        return
    await event.client.delete_messages(current_chat, current_msg)
