#    TeleBot - UserBot
#    Copyright (C) 2020 TeleBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.



import re
import random
from userbot import bot
from userbot.utils import admin_cmd

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


@borg.on(admin_cmd(pattern="tweet(?: |$)(.*)"))

async def tweet(okie):
#"""Creates random anime sticker!"""
    what = okie.pattern_match.group(1)
    if not what:
        if okie.is_reply:
            what = (await okie.get_reply_message()).message
        else:
            await okie.edit("`Tweets must contain some text, pero!`")
            return
    sticcers = await bot.inline_query(
        "TwitterStatusBot", f"{(deEmojify(what))}")
    await sticcers[0].click(okie.chat_id,
                            reply_to=okie.reply_to_msg_id,
                            silent=True if okie.is_reply else False,
                            hide_via=True)
    await okie.delete()
