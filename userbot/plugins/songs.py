# plugin made by @hellboi_atul bug fixes by @Mrconfused 
# Copyright (C) DARK COBRA 2020.
# if you change these lines you are gay...bc fuck off!
# leechers stay away😑...if you use this code without credit...u gay bitch fuck off...!



import re
import random
from userbot import bot, CMD_HELP
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import admin_cmd
import asyncio
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError


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


@borg.on(admin_cmd(pattern="songs ?(.*)"))

async def FindMusicPleaseBot(gaana):

    song = gaana.pattern_match.group(1)

    chat = "@FindMusicPleaseBot"

    if not song:

        return await gaana.edit("```what should i search```")

    await gaana.edit("```Getting Your Music```")

    await asyncio.sleep(2)

    async with bot.conversation(chat) as conv:

        await gaana.edit("`Downloading...Please wait`")

        try:

            msg = await conv.send_message(song)

            response = await conv.get_response()

            if response.text.startswith("Sorry"):

                await bot.send_read_acknowledge(conv.chat_id)

                return await gaana.edit(f"Sorry, can't find {song}")

            respond = await conv.get_response()

            cobra = await conv.get_response()

        except YouBlockedUserError:

            await gaana.edit("```Please unblock``` @FindmusicpleaseBot``` and try again```")

            return

        await gaana.edit("`Sending Your Music...weit!Ã°ÂÂÂ`")

        await bot.send_file(gaana.chat_id, cobra)

        await bot.send_read_acknowledge(conv.chat_id)

    await gaana.delete()


@borg.on(admin_cmd(pattern="deezer(?: |$)(.*)"))

async def nope(doit):
    ok = doit.pattern_match.group(1)
    if not ok:
        if doit.is_reply:
            what = (await doit.get_reply_message()).message
        else:
            await doit.edit("`Sir please give some query to search and download it for you..!`")
            return
    sticcers = await bot.inline_query(
        "DeezerMusicBot", f"{(deEmojify(ok))}")
    await sticcers[0].click(doit.chat_id,
                            reply_to=doit.reply_to_msg_id,
                            silent=True if doit.is_reply else False,
                            hide_via=True)
    await doit.delete()


@borg.on(admin_cmd("sptfy ?(.*)"))
async def _(event):
    try:
       await event.client(ImportChatInviteRequest('DdR2SUvJPBouSW4QlbJU4g'))
    except UserAlreadyParticipantError:
        pass
    except:
        await event.reply("You need to join [this](https://t.me/joinchat/DdR2SUvJPBouSW4QlbJU4g) group for this module to work.", link_preview=False)
        return
    args = event.pattern_match.group(1)
    if not args:
        await event.edit("`Enter song name`")
        return
    chat = -1001271479322
    current_chat = event.chat_id
    current_msg = event.id
    try:
       async for event in event.client.iter_messages(chat, search=args, limit=1, filter=InputMessagesFilterMusic):
                    await event.client.send_file(current_chat, event, caption=event.message)
    except:
             await event.reply("`Song not found.`")
             return
    await event.client.delete_messages(current_chat, current_msg)


CMD_HELP.update(
    {
        "songs": "__**PLUGIN NAME :** All Songs __\
    \n\n📌** CMD ★** `.songs (name)`\
    \n**USAGE   ★  **Send u song\
    \n\n📌** CMD ★** `.deezer (name)`\
    \n**USAGE   ★  **Send u song\
    \n\n📌** CMD ★** `.sptfy (name)`\
    \n**USAGE   ★  **Send u song (note:- u can use .vsong/.uta/.utv (name) too for songs 😁😁"
    }
)
