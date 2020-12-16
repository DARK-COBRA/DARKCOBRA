import asyncio
import os
import time
from datetime import datetime

from userbot.utils import admin_cmd, progress
from userbot import CMD_HELP

thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "thumb_image.jpg"


@borg.on(admin_cmd(pattern="rename (.*)"))
async def _(event):
    if event.fwd_from:
        return
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    dcevent = await event.edit(
        
        "`Rename & Upload in process 🙄🙇‍♂️🙇‍♂️🙇‍♀️ It might take some time if file size is big`",
    )
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        file_name = input_str
        reply_message = await event.get_reply_message()
        c_time = time.time()
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await event.client.download_media(
            reply_message,
            downloaded_file_name,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, dcevent, c_time, "trying to download", file_name)
            ),
        )
        end = datetime.now()
        ms_one = (end - start).seconds
        try:
            thumb = await reply_message.download_media(thumb=-1)
        except Exception:
            thumb = thumb
        if os.path.exists(downloaded_file_name):
            c_time = time.time()
            hmm = await event.client.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
                supports_streaming=True,
                allow_cache=False,
                reply_to=event.message.id,
                thumb=thumb,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(
                        d, t, event, c_time, "trying to upload", downloaded_file_name
                    )
                ),
            )
            end_two = datetime.now()
            os.remove(downloaded_file_name)
            ms_two = (end_two - end).seconds
            await dcevent.edit(
                f"`Downloaded file in {ms_one} seconds.`\n`Uploaded in {ms_two} seconds.`"
            )
            await asyncio.sleep(2)
            await dcevent.delete()
        else:
            await dcevent.edit("File Not Found {}".format(input_str))
    else:
        await dcevent.edit(
           ".rename file.name as reply to a Telegram media/file"
        )


CMD_HELP.update(
    {
        "rename": 
    ".rename filename."
    "\nReply to media with above command to rename and upload the file with given name__"
    
    }
)
