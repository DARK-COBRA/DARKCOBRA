""" Weebify a text,
Ported from Saitama Bot. 
By :- @PhycoNinja13b
Modified by :- @kirito6969
.weeb <text> """

from telethon import events
from uniborg.util import admin_cmd

normiefont = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
weebyfont = ['a', 'ɮ', 'ᴄ', 'd', 'ɛ', 'ʄ', 'ɢ', 'ɦ', 'ɨ', 'ʝ', 'ҡ', 'ʟ', 'ʍ', 'ռ', 'օ', 'p', 'զ', 'ʀ', 's', 't', 'ʊ',
             'ʋ', 'ա', 'x', 'ʏ', 'ʐ']

@borg.on(admin_cmd(pattern="weeb ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text   
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)
