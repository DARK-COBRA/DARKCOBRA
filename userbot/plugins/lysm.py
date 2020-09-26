import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="lysm ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Yar")
        await asyncio.sleep(0.7)
        await event.edit("Patta hai")
        await asyncio.sleep(1)
        await event.edit("I")
        await asyncio.sleep(0.8)
        await event.edit("Love")
        await asyncio.sleep(0.9)
        await event.edit("You")
        await asyncio.sleep(1)
        await event.edit("Sooooo")
        await asyncio.sleep(0.8)
        await event.edit("much")
        await asyncio.sleep(0.9)
        await event.edit("❤")
        await asyncio.sleep(1)
        await event.edit("`Yar patta hai I love you so much❤`")

@borg.on(events.NewMessage(pattern=r"\.ilu", outgoing=True))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"
        return
    
        await event.edit("ɪƒ ƴσυ'ʀє αʟσηє")
        await asyncio.sleep(20)
        await event.edit("ɪ'ʟʟ ɓє ƴσυʀ ѕɧα∂σѡ.")
        await asyncio.sleep(20)
        await event.edit(" ɪƒ ƴσυ ѡαηт тσ cʀƴ")
        await asyncio.sleep(20)
        await event.edit("ɪ'ʟʟ ɓє ƴσυʀ ѕɧσυʟ∂єʀ")
        await asyncio.sleep(20)
        await event.edit("ɪƒ ƴσυ ѡαηт α ɧυɢ")
        await asyncio.sleep(20)
        await event.edit("ɪ'ʟʟ ɓє ƴσυʀ ρɪʟʟσѡ")
        await asyncio.sleep(20)
        await event.edit("ɪƒ ƴσυ ηєє∂ тσ ɓє ɧαρρƴ")
        await asyncio.sleep(20)
        await event.edit("ɪ'ʟʟ ɓє ƴσυʀ ѕɱɪʟє")
        await asyncio.sleep(15)
        await event.edit("`ɓυт αηƴтɪɱє ƴσυ ηєє∂ αnчσnє, ɪt'ʟʟ ʝυѕт ɓє ɱє.❤`")
        
       
    
