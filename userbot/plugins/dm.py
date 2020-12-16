# By @HeisenbergTheDanger and @xditya

import os
import re
from telethon import *
from userbot import bot
from userbot.utils import admin_cmd
from userbot import CMD_HELP
#Fixed by @NOOBGeng Second Member
@borg.on(admin_cmd(pattern="dm ?(.*)"))
async def _(dc):
 
    d = dc.pattern_match.group(1)
    
    c = d.split(" ")#hehe

    chat_id = c[0]
    try:  #dc hehe
        chat_id = int(chat_id)
    #hmm 🤔🤔🤔🤔
    except BaseException:#lalalala
        
        pass
  
    msg = ""
    masg = await dc.get_reply_message() #ghanta😒😒
    if dc.reply_to_msg_id:
        await borg.send_message(chat_id, masg)
        await dc.edit("⚜️Message Delivered! Sar⚜️")
    for i in c[1:]:
        msg += i + " "#Fixed by @NOOBGeng Second Member
    if msg == "":#hoho
        return
    try:
        await borg.send_message(chat_id, msg)
        await dc.edit("`⚜️Message Delivered!⚜️`")
    except BaseException:#hmmmmmmmmm🤔🤔
        await dc.edit(".dm (username) (text)")

CMD_HELP.update({"dm": ".dm (username) (text)\n or\n .dm (username)(reply to msg)\n it'll forward the replyed msg"})
