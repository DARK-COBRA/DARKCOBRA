from userbot import bot
import asyncio
from userbot.utils import admin_cmd
import random
from telethon import Button, custom, events
from userbot.helpers.styles.fun import DC_FONT_STYLE, DCFONTS, SIMPLEDC

#originally by Userge X
#ported to telethon by @ProgrammingError
#Kangers Kang with FUll credits else u are gey u lesbian will be globally banned from telethon with unlimited reports
async def dc_font_maker(dc_type_choice, dc_input):
    if dc_type_choice not in DCFONTS:
        return False
    font_type = list(DCFONTS[dc_type_choice])
    for i in dc_input:
        if i in list(SIMPLEDC):
            new_char = font_type[list(SIMPLEDC).index(i)]
            dc_input = dc_input.replace(i, new_char)
    return dc_input
    #originally by Userge X
#ported to telethon by @ProgrammingError
#Kangers Kang with FUll credits else u are gey u lesbian will be globally banned from telethon with unlimited reports
@borg.on(admin_cmd(pattern="sfonts"))
async def teamdc(event):
    await event.edit("serif\nsans\nsans_i\nserif_i\nmedi_b\nmedi\ndouble\ncursive_b\ncursive\nbigsmall\nreverse\ncircle\ncircle_b\nmono\nsquare_b\nsquare\nsmoth\ngoth\nwide\nweb\nweeb\nweeeb\ntwist\ntwist_b\ntwist_c\n")
    
#originally by Userge X
#ported to telethon by @ProgrammingError
#Kangers Kang with FUll credits else u are gey u lesbian will be globally banned from telethon with unlimited reports    
@borg.on(admin_cmd(pattern="fstyle (.*)"))
async def teamdc(event):
    reply = await event.get_reply_message()
    sh1vam = event.pattern_match.group(1)
    if ";" in sh1vam:
        rabbit, atul = sh1vam.split(";")
    else:
        rabbit = sh1vam
        atul = ""
    shivam = rabbit or reply.text
    if not shivam:
        await event.edit("Please give some words to Style.")
        return
    await event.edit("Doing some Black Magic")#originally by Userge X
#ported to telethon by @ProgrammingError
#Kangers Kang with FUll credits else u are gey u lesbian will be globally banned from telethon with unlimited reports
    if atul:
        font_choice = atul
        dctxt = shivam
        if atul not in DC_FONT_STYLE:
            await event.edit("Please select a valid Font Style!")
            return
    else:
        font_choice = random.choice(DC_FONT_STYLE)
        dctxt = shivam
    dcfontchoice = font_choice.replace(";", "")
    danish = await dc_font_maker(dcfontchoice, dctxt)
    await event.edit(danish)
    
@tgbot.on(events.InlineQuery(pattern=r"fstyle (.*)"))
async def teamdc(event: events.InlineQuery.Event):
    builder = event.builder
    
    if event.query.user_id == bot.uid:
        sh1vam = event.pattern_match.group(1)
        if ";" in sh1vam:
            rabbit, atul = sh1vam.split(";")
        else:
            rabbit = sh1vam
            atul = ""
        shivam = rabbit
        if not shivam:
            resultm = builder.article(title="Please add some text.",description="Give some Correct input",text="Type some words or text to style.",buttons=[[Button.switch_inline("Search Again", query="fstyle ", same_peer=True)],],)
            await event.answer([resultm])
            return
        #await event.edit("Doing some Black Magic")#originally by Userge X
#ported to telethon by @ProgrammingError
#Kangers Kang with FUll credits else u are gey u lesbian will be globally banned from telethon with unlimited reports
        if atul:
            font_choice = atul
            dctxt = shivam
            if atul not in DC_FONT_STYLE:
                resultm = builder.article(title="Invalid Font Choosen",description="Give Some Correct input",text="Send .sfonts to see the available fonts.",buttons=[[Button.switch_inline("Search Again", query="fstyle ", same_peer=True)],],)
                await event.answer([resultm])
                return
        else:
            font_choice = random.choice(DC_FONT_STYLE)
            dctxt = shivam
        dcfontchoice = font_choice.replace(";", "")
        danish = await dc_font_maker(dcfontchoice, dctxt)
        result = builder.article(title=shivam,description=dcfontchoice,text=f"{danish}",buttons=[[Button.switch_inline("Search Again", query="fstyle ", same_peer=True)],],)
        await event.answer([result])

#originally by Userge X
#ported to telethon by @ProgrammingError
#Kangers Kang with FUll credits else u are gey u lesbian will be globally banned from telethon with unlimited reports
