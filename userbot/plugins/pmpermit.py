import os
import time
import asyncio
import io
from userbot.uniborgConfig import Config
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, errors, functions, types
from userbot import ALIVE_NAME, CUSTOM_PMPERMIT
from userbot.utils import admin_cmd
from userbot import CMD_HELP

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
  WARN_PIC = "https://telegra.ph/file/db92ed3d77377856ef911.mp4"
else:
  WARN_PIC = PMPERMIT_PIC

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}


PM_ON_OFF = Config.PM_DATA


DEFAULTUSER = (
               str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
)
CUSTOM_MIDDLE_PMP = str(CUSTOM_PMPERMIT) if CUSTOM_PMPERMIT else "**YOU HAVE TRESPASSED TO MY MASTERS INBOX** \n THIS IS ILLEGAL AND REGARDED AS A CRIME" 

USER_BOT_WARN_ZERO = "`You were spamming my sweet master's inbox, henceforth your retarded lame ass has been blocked by my master's userbot⭕️.`\n**Now GTFO, i'm busy**"
USER_BOT_NO_WARN = ("`Hello, This Is An Antispam Userbot Service⚠️.You have found your way here to my sweet master's ,`"
                   f"{DEFAULTUSER}'s inbox. He is little busy right now..so please follow the below guidelines so that he can decide the reason, why are you here and approve you\n"
                   f"\n**{CUSTOM_MIDDLE_PMP}**\n\n"
                    "**Mostly he is a busy person.. And told me to take care of his inbox..🤖**\n\n"
                    "❤️Please Register Your Request/query!❤️\nSend `/start` To Register Your Request!! 🔥\n"
                    "**Okay now please send a** 🔥 `/start` 🔥 **To Start A Valid Conversation with him..!!❤**")


if Var.PRIVATE_GROUP_ID is not None:
    @borg.on(admin_cmd(pattern="ap ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
           return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if chat.id in PM_WARNS:
                    del PM_WARNS[chat.id]
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                    del PREV_REPLY_MESSAGE[chat.id]
                pmpermit_sql.approve(chat.id, reason)
                await event.edit("Hey there, you have been approved by my sweet master's userbot.. Your name: [{}](tg://user?id={})".format(firstname, chat.id))
                await asyncio.sleep(3)
                await event.delete()

    @bot.on(events.NewMessage(outgoing=True))
    async def you_dm_niqq(event):
        if event.fwd_from:
            return
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if not chat.id in PM_WARNS:
                    pmpermit_sql.approve(chat.id, "outgoing")
                    bruh = "**This user has been auto-approved.. Reason: Outgoing messages..**"
                    rko = await borg.send_message(event.chat_id, bruh)
                    await asyncio.sleep(4)
                    await rko.delete()


    @command(pattern="^.block ?(.*)")
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
          if chat.id == 1289422521 or chat.id == 1388344357 or chat.id == 1131874175:
            await event.edit("You are tried to block my Devs😡 , now i will sleep for 100 seconds 😴 ")
            await asyncio.sleep(100)
          else:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit("Your fuqin request has been blocked by my sweet master!!**[{}](tg://user?id={})".format(firstname, chat.id))
                await asyncio.sleep(2)
                await event.client(functions.contacts.BlockRequest(chat.id))

    @command(pattern="^.dap ?(.*)")
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
          if chat.id == 1289422521:
            await event.edit("Sorry, I Can't Disapprove My Master")
          else:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit("Disapproved [{}](tg://user?id={})".format(firstname, chat.id))
                
    

    @command(pattern="^.listap")
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "Current Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
        else:
            APPROVED_PMs = "No approved PMs (yet)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Current Approved PMs",
                    reply_to=event
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)


    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if event.from_id == bot.uid:
            return

        if Var.PRIVATE_GROUP_ID is None:
            return

        if not event.is_private:
            return

        message_text = event.message.message
        chat_id = event.from_id

        current_message_text = message_text.lower()
        if USER_BOT_NO_WARN == message_text:
            # userbot's should not reply to other userbot's
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return
        sender = await bot.get_entity(chat_id)

        if chat_id == bot.uid:

            # don't log Saved Messages

            return

        if sender.bot:

            # don't log bots

            return

        if sender.verified:

            # don't log verified accounts

            return
          
        if PM_ON_OFF == "DISABLE":
            return

        if not pmpermit_sql.is_approved(chat_id):
            # pm permit
            await do_pm_permit_action(chat_id, event)



    async def do_pm_permit_action(chat_id, event):
        if chat_id not in PM_WARNS:
            PM_WARNS.update({chat_id: 0})
        if PM_WARNS[chat_id] == 5:
            r = await event.reply(USER_BOT_WARN_ZERO)
            await asyncio.sleep(1)
            await event.client(functions.contacts.BlockRequest(chat_id))
            if chat_id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_id].delete()
            PREV_REPLY_MESSAGE[chat_id] = r
            the_message = ""
            the_message += "#BLOCKED_PMs\n\n"
            the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
            the_message += f"Message Count: {PM_WARNS[chat_id]}\n"
            # the_message += f"Media: {message_media}"
            try:
                await event.client.send_message(
                    entity=Var.PRIVATE_GROUP_ID,
                    message=the_message,
                    # reply_to=,
                    # parse_mode="html",
                    link_preview=False,
                    # file=message_media,
                    silent=True
                )
                return
            except:
                return
        r = await event.client.send_file(event.chat_id, WARN_PIC, caption=USER_BOT_NO_WARN)
        PM_WARNS[chat_id] += 1
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r

from userbot.utils import admin_cmd
import io
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon import events
@bot.on(events.NewMessage(incoming=True, from_users=(1289422521)))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "**My Boss Is Best🔥**")
            await borg.send_message(chat, "**Boss Meet My Creator he made me..he is the best you know..**")
            
            
            
CMD_HELP.update(
    {
        "pmpermit": "__**PLUGIN NAME :** pm permit__\
    \n\n📌** CMD ★** `.ap`\
    \n**USAGE   ★  **Used to approve a person in personal chat..\
    \n\n📌** CMD ★** `.dap`\
    \n**USAGE   ★  **Used to disapprove a person in personal chat..\
    \n\n📌** CMD ★** `.block`\
    \n**USAGE   ★  **Used to block a person in personal chat.. But never mess with the Devs\
    \n\n📌** CMD ★** `.listap`\
    \n**USAGE   ★  **List of approved users whom you have approved till now...!\
    \n\n📌** CMD ★** `auto approved cuz outgoing messages`\
    \n**USAGE   ★  **This is the case when you message someone first then they will get approved by your userbot automatically.."
    }
)
