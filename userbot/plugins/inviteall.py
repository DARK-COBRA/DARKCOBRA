from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"inviteall ?(.*)"))

async def get_users(event):   
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
    else:
    	rkp = await event.edit("`processing...`")
    rk1 = await get_chatinfo(event) ; chat = await event.get_chat()
    if event.is_private:
              return await rkp.edit("`Sorry, Can add users here`")    
    s = 0 ; f = 0 ; error = 'None'   
  
    await rkp.edit("**TerminalStatus**\n\n`Collecting Users.......`")
    async for user in event.client.iter_participants(rk1.full_chat.id):
                try:
                    if error.startswith("Too"):
                        return await rkp.edit(f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people")
                    await event.client(functions.channels.InviteToChannelRequest(channel=chat,users=[user.id]))
                    s = s + 1                                                    
                    await rkp.edit(f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`")                
                except Exception as e:
                    error = str(e) ; f = f + 1             
    return await rkp.edit(f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people")
    



@borg.on(admin_cmd(pattern=r"inviteall2 ?(.*)"))
async def get_users(event):   
    rk1 = await get_chatinfo(event) ; chat = await event.get_chat()
    if event.is_private:
              return await event.edit("`Sorry, Can add users here`")
    if not BOTLOG_CHATID:
	         return await event.edit (f"`Failed to Channed Bot log Chat \nPlease add bot log chat to use this`")
    s = 0 ; f = 0 ; error = 'None'   
    await event.delete()    
    test = "**TerminalStatus**\n\n`Collecting Users.......`"
    rkp = await client.send_message(BOTLOG_CHATID, test)
    async for user in event.client.iter_participants(rk1.full_chat.id):
                try:
                    if error.startswith("Too"):
                        return await rkp.edit(f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people")
                    await event.client(functions.channels.InviteToChannelRequest(channel=chat,users=[user.id]))
                    s = s + 1                                                    
                    await rkp.edit(f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`")                
                except Exception as e:
                    error = str(e) ; f = f + 1             
    return await rkp.edit(f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people")
