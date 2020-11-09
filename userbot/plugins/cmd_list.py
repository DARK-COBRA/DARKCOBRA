from telethon import events
import subprocess
import asyncio
import time
from userbot.utils import admin_cmd
from userbot import CMD_HELP

#@command(pattern="^.cmds", outgoing=True)
@borg.on(admin_cmd(pattern=r"cmds"))
async def install(event):
    if event.fwd_from:
        return
    cmd = "ls userbot/plugins"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = (
        OUTPUT
    ) = f"**List of Plugins:**\n{o}\n\n**HELP:** __If you want to know the commands for a plugin, do:-__ \n `.help <plugin name>` **without the < > brackets.**\n__All plugins might not work directly. Visit__ @Dark_cobra_support_group__for assistance.__"
    await event.edit("`Plugins extracted, pasting it weit a second...`")
    message = OUTPUT
    url = "https://nekobin.com/documents"
    r = requests.post(url, data=message.encode("UTF-8")).json()
    url = f"https://nekobin.com/{r['key']}"
    await event.edit(
        f"`All plugins have been successfully extracted and can be found [here]({url})!!"
    )

CMD_HELP.update(
    {"command_list": ".cmds\nUsage - Extracts all the plugins of this userbot in a link.."}
)
