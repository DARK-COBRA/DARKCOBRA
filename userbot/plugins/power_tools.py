"""Restart or Terminate the bot from any chat
Available Commands:
.restartsys
.shutdown"""
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="restart"))
async def _(event):
    await event.edit("Restarting [██░] ...")
    await asyncio.sleep(2)
    await event.edit("Restarting [███]...")
    await asyncio.sleep(2)
    await event.edit("Restarted boss....✈ `.king` me or type `.help` or type '.awake' or type '.allive' to check if your DC is online/alive ")
    await borg.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@borg.on(admin_cmd(pattern="shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Turning dyno off ...Manually turn me on later")
    await borg.disconnect()
