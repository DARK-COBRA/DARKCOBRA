"""Emoji

Available Commands:

.wtf"""

from telethon import events

import asyncio
from userbot import CMD_HELP
from userbot.utils import admin_cmd

@borg.on(admin_cmd("wtf"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    await event.edit("wtf")
    animation_chars = [
            "What",
            "What The",
            "What The F",
            "What The F Brah",
            "[What The F Brah](https://telegra.ph//file/f3b760e4a99340d331f9b.jpg)"
        ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i %5 ])

CMD_HELP.update(
    {
        "wtf": ".wtf"
        "\nUsage: Just a Animation of WTF\n\n"
    }
)
