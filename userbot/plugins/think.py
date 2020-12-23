"""Emoji

Available Commands:

.think"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("think"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.4
    animation_ttl = range(0, 288)
    
    #await event.edit(input_str)
    await event.edit("thinking")
    animation_chars = [
            "THINKING",
            "THI&K#N₹",
            "ERroR",
            "ErrOr",
            "eRrOr",
            "404",
            "BRAIn Missing🤤",
            "BRAIn Missing🤤",
            "BRAIn Missing🤤",
            "BRAIn Missing🤤",
            "DrOp BRAIn In Ib",
            "Else Gey",
            "NGITHKIN",
            "Kuch V Nahi Mila Bisi... 🤔"
        ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 72])
