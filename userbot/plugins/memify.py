# base by: @r4v4n4
# created by: @A_Dark_Princ3
# if you change these, you gay

"""Reply to an image/sticker/gif with .mmf` 'text on top' ; 'text on bottom
"""

from telethon.errors.rpcerrorlist import YouBlockedUserError

from io import BytesIO
from PIL import Image
import asyncio
import time
from datetime import datetime
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pySmartDL import SmartDL
from telethon.tl.types import DocumentAttributeVideo
from uniborg.util import progress, humanbytes, time_formatter, admin_cmd
import datetime
from collections import defaultdict

import os


from telethon.errors.rpcerrorlist import StickersetInvalidError
from telethon.errors import MessageNotModifiedError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import (
DocumentAttributeFilename,
DocumentAttributeSticker,
InputMediaUploadedDocument,
InputPeerNotifySettings,
InputStickerSetID,
InputStickerSetShortName,
MessageMediaPhoto
)


thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"


@borg.on(admin_cmd(pattern="mmf ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("`Syntax: reply to an image with .mms` 'text on top' ; 'text on bottom' ")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("```reply to a image/sticker/gif```")
       return
    chat = "@MemeCreatorBot"
    sender = reply_message.sender
    file_ext_ns_ion = "@memetime.png"
    file = await borg.download_file(reply_message.media)
    uploaded_gif = None
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    else:
     await event.edit("```Transfiguration Time! Hahaha Memifying this image! (」ﾟﾛﾟ)｣ ```")
     await asyncio.sleep(5)
    
    async with borg.conversation("@MemeCreatorbot") as bot_conv:
          try:
            memeVar = event.pattern_match.group(1)
            await silently_send_message(bot_conv, "/start")
            await asyncio.sleep(1)
            await silently_send_message(bot_conv, memeVar)
            await borg.send_file(chat, reply_message.media)
            response = await bot_conv.get_response()
          except YouBlockedUserError: 
              await event.reply("```Please unblock @MemeCreatorbot and try again```")
              return
          if response.text.startswith("Forward"):
              await event.edit("```can you kindly disable your forward privacy settings```")
          if "Okay..." in response.text:
            await event.edit("``` This is not an image! This will take some tym to convert to image... UwU 🧐 🛑```")
            thumb = None
            if os.path.exists(thumb_image_path):
                thumb = thumb_image_path
            input_str = event.pattern_match.group(1)
            if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
                os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
            if event.reply_to_msg_id:
                file_name = "meme.png"
                reply_message = await event.get_reply_message()
                to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
                downloaded_file_name = os.path.join(to_download_directory, file_name)
                downloaded_file_name = await borg.download_media(
                    reply_message,
                    downloaded_file_name,
                    )
                if os.path.exists(downloaded_file_name):
                    await borg.send_file(
                        chat,
                        downloaded_file_name,
                        force_document=False,
                        supports_streaming=False,
                        allow_cache=False,
                        thumb=thumb,
                        )
                    os.remove(downloaded_file_name)
                else:
                    await event.edit("File Not Found {}".format(input_str))
            response = await bot_conv.get_response()
            the_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
            files_name = "memes.webp"
            download_file_name = os.path.join(the_download_directory, files_name)
            await borg.download_media(
                response.media,
                download_file_name,
                )
            requires_file_name = Config.TMP_DOWNLOAD_DIRECTORY + "memes.webp"
            await borg.send_file(  # pylint:disable=E0602
                event.chat_id,
                requires_file_name,
                supports_streaming=False,
                caption="@Dark_cobra_support OOF @Dark_cobra_support group",
                # Courtesy: @DARK_COBRA_SUPPORT
            )
            await event.delete()
         #   await borg.send_message(event.chat_id, "`☠️☠️Ah Shit... Here we go Again!🔥🔥`")
          elif not is_message_image(reply_message):
            await event.edit("Invalid message type. Plz choose right message type")
            return
          else: 
               await borg.send_file(event.chat_id, response.media)

def is_message_image(message):
    if message.media:
        if isinstance(message.media, MessageMediaPhoto):
            return True
        if message.media.document:
            if message.media.document.mime_type.split("/")[0] == "image":
                return True
        return False
    return False
    
async def silently_send_message(conv, text):
    await conv.send_message(text)
    response = await conv.get_response()
    await conv.mark_read(message=response)
    return response
    
