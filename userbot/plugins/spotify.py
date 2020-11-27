# Plugin made by @okay_retard && @hellboi_atul...
# If Gonna kang then keep credits..don't edit/remove these lines... Else gay
# Utilities fixes by @xditya..
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import InputMessagesFilterMusic
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK COBRA"

@borg.on(admin_cmd("sptfy ?(.*)"))
async def _(event):
    try:
        await event.client(ImportChatInviteRequest("DdR2SUvJPBouSW4QlbJU4g"))
    except UserAlreadyParticipantError:
        pass
    except Exception as e:
        await event.edit(
            f"`Some unknown error occured!\nAborting...\nError - {str(e)}`"
        )
        return
    name = event.pattern_match.group(1)
    if not name:
        await event.edit(
            "Song donwloader.\nSyntax - `.song name`\nFor better results, use Song Name- Artist name."
        )
        return
    chat = -1001271479322
    current_chat = event.chat_id
    ok = bot.uid
    current_msg = event.id
    cap = """
==> **Song name** - `{}`
==> **Uploaded by** [{DEFAULTUSER}](tg://user?id={ghanta})
"""
    try:
        async for event in event.client.iter_messages(
            chat, search=name, limit=1, filter=InputMessagesFilterMusic
        ):
            ok = cap.format(event.message, DEFAULTUSER)
            await event.client.delete_messages(current_chat, current_msg)
            await event.client.send_file(current_chat, event, caption=ok)
    except BaseException:
        await event.reply(
            f"`Song, {name}, not found. For better results, use Song name- Artist Name.`"
        )
        return
