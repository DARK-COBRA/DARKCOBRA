from telethon import events
import random, re
from uniborg.util import admin_cmd

RUNSREACTS = [
    "`Tufaano Mein Chhatri Nahi Kholi Jaati; Bra Se Pehle Panty Nahi Kholi Jaati; ‘Viagra’ Khana Shuru Kar, Mere Dost; Kyunki Zubaan Aur Ungli Se Aurat Nahi Chodi Jaati!`",
        "`Ranger tumara baap tha hai aur rahega smje`",
    "`Yaad Mein Unki Kiya Loota Diya..Itni Mari Muthh Ke Topa Sujaa Diya..Hume Kamzor Hota Dekh Jab Muskurayi Woh…….Unki Khushi Dekh Kar Ek Baar Fhir Hila Diya..`",
    "` Lund Toh Choot Ki Baddi Shaan Hoti Hai; Lund Bina Choot Bhi Shamshaan Hoti Hai; Yeh Zindgi Ke Saare Khel Toh Lund Ke Hein; Warna Choot Aur Gaand Ek Samaan Hoti Hai!`",
]

@borg.on(admin_cmd(pattern="bc"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(RUNSREACTS) - 1)    
    reply_text = RUNSREACTS[bro]
    await event.edit(reply_text)