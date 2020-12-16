import asyncio
import time
import shutil
from pySmartDL import SmartDL
from telethon import events
from telethon.tl import functions
from telethon.errors import FloodWaitError
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, CMD_HELP

BIO_MSG = Config.BIO_MSG
if BIO_MSG is None:
  BIO_MSG = "I am a pro @Dark_cobra_support"

DEL_TIME_OUT = 60


@borg.on(admin_cmd(pattern="autobio"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"{DMY} {BIO_MSG} ⌚️{HM}"
        logger.info(bio)
        try:
            await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                about=bio
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        else:
            logger.info(r.stringify())
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                "Successfully Changed Profile Bio"
            )
        await asyncio.sleep(DEL_TIME_OUT)


TIME_OUT = 60
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "FRIDAY"


@borg.on(admin_cmd(pattern="autoname"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        name = f"⌚{HM} 🔥{DEFAULTUSER}🔥 📅{DMY}"
        logger.info(name)
        try:
            await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                first_name=name
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
    
        else:
            logger.info(r.stringify())
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                "Successfully Changed Profile Name"
            )
        await asyncio.sleep(TIME_OUT)
    await event.edit(f"Auto Name has been started Master") 

FONT_FILE_TO_USE = "Fonts/digital.ttf"

@command(pattern="^.autopic", outgoing=True)
async def autopic(event):
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(Var.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    photo = "userbot/photo_pfp.png"
    while not downloader.isFinished():
        place_holder = None
    counter = -30
    while True:
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        file_test = im.rotate(counter, expand=False).save(photo, "PNG")
        current_time = datetime.now().strftime("                      \n  Time: %H:%M:%S \n  Date: %d.%m.%y \n                    ")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 60)
        drawn_text.text((95, 250), current_time, font=fnt, fill=(0, 255, 0))
        img.save(photo)
        file = await bot.upload_file(photo)  # pylint:disable=E0602
        try:
            await bot(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            counter -= 30
            await asyncio.sleep(60)
        except:
            return

CMD_HELP.update(
    {
        "auto_profile": ".autobio"
        "\nUsage: change ur bio automatically nd to stop use .restart\n\n"
        ".autopic"
        "\nUsage: change ur pic automatically (rotate pic in every 60sec) nd to stop use .restart\n\n"
        ".autoname"
        "\nUsage: Change ur name automatically nd show time ns date there to stop it use .restart"
          })
