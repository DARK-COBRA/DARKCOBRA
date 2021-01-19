# Plugin made by @hellboi_atul for DARK COBRA..
# You can use this..but don't edit/remove these comment lines..
# This module fetches the link from YouTube for the given query..
# merged .uta
# So wahi...Enjoy


import re
import random
from userbot import bot, CMD_HELP
import asyncio
import os
import json
from pathlib import Path
from youtube_search import YoutubeSearch
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import admin_cmd, edit_or_reply


IF_EMOJI = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats 
    "]+")

def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(IF_EMOJI, '', inputString)


@borg.on(admin_cmd(pattern="ulinks ?(.*)"))
async def yt_search(video_q):
    """For .yt command, do a YouTube search from Telegram."""
    query = video_q.pattern_match.group(1)
    if not query:
        await video_q.edit("`Enter query to search`")
    await video_q.edit("`Processing...`")
    try:
        results = json.loads(YoutubeSearch(query, max_results=7).to_json())
    except KeyError:
        return await video_q.edit("`Sorry master i couldn't find something related to this query!`")
    output = f"**Search Query:**\n`{query}`\n\n**Results:**\n\n"
    for i in results["videos"]:
        output += (f"--> `{i['title']}`\nhttps://www.youtube.com{i['url_suffix']}\n\n")
    await video_q.edit(output, link_preview=False)
 
 



# Social Distancing..







@borg.on(admin_cmd(pattern="uta ?(.*)"))

async def nope(doit):
    ok = doit.pattern_match.group(1)
    if not ok:
        if doit.is_reply:
            what = (await doit.get_reply_message()).message
        else:
            await doit.edit("`Sir please give some query to search and download it for you..!`")
            return
    sticcers = await bot.inline_query(
        "Lybot", f"{(deEmojify(ok))}")
    await sticcers[0].click(doit.chat_id,
                            reply_to=doit.reply_to_msg_id,
                            silent=True if doit.is_reply else False,
                            hide_via=True)
    await doit.delete()



SEARCH_STRING = "<code>Ok weit, searching....</code>"
NOT_FOUND_STRING = "<code>Sorry !I am unable to find any results to your query</code>"
SENDING_STRING = "<code>Ok I found something related to that.....</code>"
BOT_BLOCKED_STRING = "<code>Please unblock @utubebot and try again</code>"

@bot.on(admin_cmd(pattern="ut ?(.*)"))
async def fetcher(event):
    if event.fwd_from:
        return
    song = event.pattern_match.group(1)
    chat = "@utubebot"
    event = await edit_or_reply(event, SEARCH_STRING, parse_mode="html")
    async with event.client.conversation(chat) as conv:
        try:
            purgeflag = await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(song)
            ok = await conv.get_response()
            while ok.edit_hide != True:
                await asyncio.sleep(0.1)
                ok = await event.client.get_messages(chat, ids=ok.id)
            baka = await event.client.get_messages(chat)
            if baka[0].message.startswith(
                ("Sorry I found nothing..")
            ):
                await delete_messages(event, chat, purgeflag)
                return await edit_delete(
                    event, NOT_FOUND_STRING, parse_mode="html", time=5
                )
            await event.edit(SENDING_STRING, parse_mode="html")
            await baka[0].click(0)
            music = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(BOT_BLOCKED_STRING, parse_mode="html")
            return
        await event.client.send_file(
            event.chat_id,
            music,
            caption=f"<b>==> <code>{song}</code></b>",
            parse_mode="html",
        )
        await event.delete()
        await delete_messages(event, chat, purgeflag)


CMD_HELP.update(
    {
        "utube": "__**PLUGIN NAME :** All YouTube__\
    \n\n📌** CMD ★** `.uta (song name)`\
    \n**USAGE   ★  **Send sudio song via Lybot\
    \n\n📌** CMD ★** `.utv (song name)`\
    \n**USAGE   ★  **Send video song via vidbot \
    \n\n📌** CMD ★** `.ut (utube video link)`\
    \n**USAGE   ★  **not fixed yet, we'll try to fix later 😅😅"
    }
)
