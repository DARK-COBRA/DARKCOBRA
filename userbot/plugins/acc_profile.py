
import os
from telethon import events
from telethon.tl import functions
from userbot.utils import admin_cmd, sudo_cmd
from telethon.errors import ImageProcessFailedError, PhotoCropSizeSmallError
from telethon.errors.rpcerrorlist import (PhotoExtInvalidError,
                                          UsernameOccupiedError)
from telethon.tl.functions.account import (UpdateProfileRequest,
                                           UpdateUsernameRequest)
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.photos import (DeletePhotosRequest,
                                          GetUserPhotosRequest,
                                          UploadProfilePhotoRequest)
from telethon.tl.types import InputPhoto, MessageMediaPhoto, User, Chat, Channel
from userbot import bot
from userbot import CMD_HELP, CMD_LIST

# ====================== CONSTANT ===============================
INVALID_MEDIA = "```The extension of the media entity is invalid.```"
PP_CHANGED = "```Profile pic Changed Successfully🤤```"
PP_TOO_SMOL = "```This image is too small, use a bigger image.```"
PP_ERROR = "```Failure occured while processing image.```"
BIO_SUCCESS = "```Bio Edited Sucessfully.```"
NAME_OK = "```Your name was succesfully changed.```"
USERNAME_SUCCESS = "```Your username was succesfully changed.```"
USERNAME_TAKEN = "```This username is already taken.```"
# ===============================================================


@borg.on(admin_cmd(pattern="pbio (.*)")) 
@borg.on(sudo_cmd(pattern="pbio (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    bio = event.pattern_match.group(1)
    try:
        await borg(functions.account.UpdateProfileRequest(  
            about=bio
        ))
        await event.edit("Succesfully changed my profile bio")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


@borg.on(admin_cmd(pattern="pname ((.|\n)*)"))
@borg.on(sudo_cmd(pattern="pname ((.|\n)*)",allow_sudo=True))  
async def _(event):
    if event.fwd_from:
        return
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if  "|" in names:
        first_name, last_name = names.split("|", 1)
    try:
        await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
            first_name=first_name,
            last_name=last_name
        ))
        await event.edit("My name was changed successfully")
    except Exception as e:  
        await event.edit(str(e))


@borg.on(admin_cmd(pattern="ppic"))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    await event.edit("Downloading Profile Picture to my local ...")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    photo = None
    try:
        photo = await borg.download_media(  # pylint:disable=E0602
            reply_message,
            Config.TMP_DOWNLOAD_DIRECTORY  # pylint:disable=E0602
        )
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))
    else:
        if photo:
            await event.edit("now, Uploading to Telegram ...⚡")
            file = await borg.upload_file(photo)  # pylint:disable=E0602
            try:
                await borg(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                    file
                ))
            except Exception as e:  # pylint:disable=C0103,W0703
                await event.edit(str(e))
            else:
                await event.edit("My profile picture was succesfully chamged")
    try:
        os.remove(photo)
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))  # pylint:disable=E0602


@borg.on(admin_cmd(outgoing=True, pattern="uname (.*)"))
@borg.on(sudo_cmd(outgoing=True, pattern="uname (.*)", allow_sudo=True))
async def update_username(username):
    """ For .username command, set a new username in Telegram. """
    newusername = username.pattern_match.group(1)
    try:
        await username.client(UpdateUsernameRequest(newusername))
        await username.edit(USERNAME_SUCCESS)
    except UsernameOccupiedError:
        await username.edit(USERNAME_TAKEN)



@borg.on(admin_cmd(outgoing=True, pattern=r"delpfp"))
@borg.on(sudo_cmd(outgoing=True,pattern=r"delpfp", allow_sudo=True))
async def remove_profilepic(delpfp):
    """ For .delpfp command, delete your current profile picture in Telegram. """
    group = delpfp.text[8:]
    if group == 'all':
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1

    pfplist = await delpfp.client(
        GetUserPhotosRequest(user_id=delpfp.from_id,
                             offset=0,
                             max_id=0,
                             limit=lim))
    input_photos = []
    for sep in pfplist.photos:
        input_photos.append(
            InputPhoto(id=sep.id,
                       access_hash=sep.access_hash,
                       file_reference=sep.file_reference))
    await delpfp.client(DeletePhotosRequest(id=input_photos))
    await delpfp.edit(
        f"`Successfully deleted {len(input_photos)} profile picture(s).`")

@borg.on(admin_cmd(pattern="myusernames$"))
@borg.on(sudo_cmd(pattern=r"myusernames$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    result = await bot(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)
    
CMD_HELP.update({
    "acc_profile":
    ".username <new_username>\
\nUsage Changes your Telegram username.\
\n\n.pname <firstname> or .pname <firstname> <lastname>\
\nUsage Changes your Telegram name.(First and last name will get split by the first space)\
\n\n.setpfp or .ppic\
\nUsage Reply with .setpfp or .ppic to an image to change your Telegram profie picture.\
\n\n.pbio <new_bio>\
\nUsage Changes your Telegram bio.\
\n\n.delpfp or .delpfp <number>/<all>\
\nUsage Deletes your Telegram profile picture(s).\
\n\n.myusernames\
\nUsage Shows usernames reserved by you.that is created by you channels or groups"
})
