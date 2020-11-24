# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from telethon import events
from telethon.tl.functions.messages import SaveDraftRequest
from userbot.utils import admin_cmd
from userbot import CMD_HELP

@borg.on(admin_cmd(pattern="chain"))
async def _(event):
    await event.edit("Counting...")
    count = -1
    message = event.message
    while message:
        reply = await message.get_reply_message()
        if reply is None:
            await borg(SaveDraftRequest(
                await event.get_input_chat(),
                "",
                reply_to_msg_id=message.id
            ))
        message = reply
        count += 1
    await event.edit(f"Chain length: {count}")


CMD_HELP.update(
    {
        "chain": 
    ".chain <reply to any msg> "
    "\nCount the chain length means the reply-reply how many times 😂😂"
    })
