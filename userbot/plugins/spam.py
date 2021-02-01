# By dark cobra for Dark cobra with logger support
# Kang with credits..

import asyncio
from asyncio import wait
from userbot import CMD_HELP


from userbot.events import register

@register(outgoing=True, pattern="^.tspam")
async def tmeme(e):
    tspam = str(e.text[7:])
    message = tspam.replace(" ", "")
    for letter in message:
        await e.respond(letter)
    await e.delete()

@register(outgoing=True, pattern="^.spam")
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
        
                               
@register(outgoing=True, pattern="^.bigspam")
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[9:13])
        spam_message = str(e.text[13:])
        for i in range(1, counter):
            await e.respond(spam_message)
        await e.delete()
        
        
        

@register(outgoing=True, pattern="^.mspam")
async def tiny_pic_spam(e):
    reply = await e.get_reply_message()
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        text = message.split()
        counter = int(text[1])
        media = await e.client.download_media(reply)
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, media)
        await e.delete()
        

@register(outgoing=True, pattern="^.delayspam (.*)")
async def spammer(e):
    spamDelay = float(e.pattern_match.group(1).split(' ', 2)[0])
    counter = int(e.pattern_match.group(1).split(' ', 2)[1])
    spam_message = str(e.pattern_match.group(1).split(' ', 2)[2])
    await e.delete()
    for i in range(1, counter):
        await e.respond(spam_message)
        await asyncio.sleep(spamDelay)
    
CMD_HELP.update(
    {
        "spam": ".spam <no of msgs> <your msg>"
        "\nUsage: spams the current chat, the current limit for this is from 1 to 99.\n\n"
        ".bigspam <no of msgs> <your msg>"
        "\nUsage: Spams the current chat, the current limit is above 100.\n\n"
        ".mspam <no of spam> (with reply to media)"
        "\nUsage: Spams the current chat with number you did put in <no of spam>.\n\n"
        ".delayspam <delay time> <count> <msg>"
        "\nUsage: Spams the current chat with with the input msgs with a delay time that has been given as its input.\n\n"
    }
)
