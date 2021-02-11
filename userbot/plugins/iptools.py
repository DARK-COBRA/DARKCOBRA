# Advanced Web Tools Plugin Made by @Hackintush..
# All Credits Belong to CɪᴘʜᴇʀX..
# Edited and ported with accordance to the utility by @hellboi_atul...Itz team DC
# Use on your own risk..we aren't responsible for any illegal activities done by you..this module is for educational purposes only..neither the team or the maker of the plugin is responsible..
# If you remove these 5 lines you are the geyest gey in the whole world..
import json
import urllib.request
import requests 
from bs4 import BeautifulSoup

from userbot.utils import admin_cmd 
from userbot.utils import edit_or_reply
from userbot import CMD_HELP
from userbot import bot 


@bot.on(admin_cmd(pattern="nmap (.*)"))
async def _(event):
    if event.fwd_from:
        return      
    try:
        cipher = await edit_or_reply(event, "Fecthing Nmap Ip/Host Info, please wait..")
        input_str = event.pattern_match.group(1) 
        adress = input_str
        api = f"http://api.hackertarget.com/nmap/?q={adress}"
        soup = BeautifulSoup(requests.get(api).content, "html.parser")   
        soup = str(soup) 
        first_line = soup.split("\n")[0]
        other_lines =  soup.split("\n")[1:]
        for line in other_lines:
            await cipher.edit(line) 
            print('\n\n✨ ©DARK COBRA ✨') 
    except:
            await cipher.edit("Not a Valid ip/host or Don't Have Enough Info.")
    
        
        
@bot.on(admin_cmd(pattern="honeypot (.*)"))
async def _(event):
    if event.fwd_from:
        return      
    try:
        cipher = await edit_or_reply(event, "`Fetching Honeypot Ip Info, Please wait..`")
        input_str = event.pattern_match.group(1) 
        adress = input_str
        api = (f"https://api.shodan.io/labs/honeyscore/{adress}?key=C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by") 
        soup = BeautifulSoup(requests.get(api).content, "html.parser")
        for line in soup:
            await cipher.edit('Honeypot Probabilty: ', line, '\n\n✨ ©DARK COBRA ✨')
    except:
            await cipher.edit("Not a Valid ip or Don't Have Enough Info.")
    

@bot.on(admin_cmd(pattern="ipreverse (.*)"))
async def _(event):
    if event.fwd_from:
        return      
    try:
        cipher = await edit_or_reply(event, "Fecthing Reverse Ip Info, Please wait...")
        input_str = event.pattern_match.group(1) 
        adress = input_str
        api = (f'https://api.hackertarget.com/reverseiplookup/?q={adress}') 
        soup = BeautifulSoup(requests.get(api).content, "html.parser")
        for line in other_lines:
            await cipher.edit('Reverse Ip Lookup Result: \n\n', line , '\n\n✨ ©DARK COBRA ✨')
    except:
            await cipher.edit("Not a Valid ip or Don't Have Enough Info.")
    



@bot.on(admin_cmd(pattern="dnslookup (.*)"))
async def _(event):
    if event.fwd_from:
        return      
    try:
        cipher = await edit_or_reply(event, "Fecthing dns Lookup Info, Please wait...")
        input_str = event.pattern_match.group(1) 
        adress = input_str
        api = (f'https://api.hackertarget.com/dnslookup/?q={adress}') 
        soup = BeautifulSoup(requests.get(api).content, "html.parser")
        for line in other_lines:
            await cipher.edit('DNS Lookup Result: \n\n', line , '\n\n✨ ©DARK COBRA ✨')
    except:
            await cipher.edit("Not a Valid ip/host or Don't Have Enough Info.")
    



@bot.on(admin_cmd(pattern="ipwhois (.*)"))
async def _(event):
    if event.fwd_from:
        return      
    try:
        cipher = await edit_or_reply(event, "Fetching Whois Ip Info, Please wait...")
        input_str = event.pattern_match.group(1) 
        adress = input_str
        api = (f'http://api.hackertarget.com/whois/?q={adress}')
        soup = BeautifulSoup(requests.get(api).content, "html.parser")
        for line in other_lines:
            await cipher.edit('Wois Result: \n\n', line , '\n\n✨ ©DARK COBRA ✨')
    except:
            await cipher.edit("Not a Valid ip or Don't Have Enough Info.")
    
@bot.on(admin_cmd(pattern="advanceip (.*)"))
async def _(event):
    if event.fwd_from:
        return      
    try:
        cipher = await edit_or_reply(event, "Fecthing Advanced Ip/Host Info, Please wait...")
        input_str = event.pattern_match.group(1) 
        adress = input_str
        api = 'http://ip-api.com/json/' + adress
        result = urllib.request.urlopen(api).read()
        result = result.decode()
        result = json.loads(result)
        a = result["status"]
        b = result["country"]
        c = result["countryCode"]
        d = result["region"]
        e = result["regionName"]
        f = result["city"]
        g = result["zip"]
        h = result["lat"]
        i = result["lon"]
        j = result["timezone"]
        k = result["isp"]
        l = result["org"]
        m = result["as"]
        n = result["query"]
        output = (f"<b><u>Information Gathered Successfully</b></u>\n\n<b>Ip Adress :- </b><code>{n}</code>\n<b>Status :-</b><code>{a}</code>\n<b>Country:- </b> <code>{b}</code>\n<b>Country Code:-</b><code>{c}</code>\n<b>Region :- </b><code>{d}</code>\n<b>Region Name :-</b><code>{e}</code>\n<b>City:- </b> <code>{f}</code>\n<b>Zip :- </b><code>{g}</code>\n<b>Latitude :- </b><code>{h}</code>\n<b>Longitude :- </b><code>{i}</code>\n<b>Timezone :- </b><code>{j}</code>\n<b>ISP :- </b><code>{k}</code>\n<b>ORG :- </b><code>{l}</code>\n<b>AS :- </b><code>{m}</code>\n\n✨ ©DARK COBRA ✨")  
        await cipher.edit(output, parse_mode="HTML")
    except:
        await cipher.edit("Not a Valid ip/host or Don't Have Enough Info.")
    
    
CMD_HELP.update(
    {
        "iptools": "cipherxiptools\
        \n\nSyntax : .nmap <ip/host>\
        \nUsage : Perform nmap on the defined ip/host address.\
        \n\nSyntax : .honeypot <ip>\
        \nUsage : Find honeypot probability through shodan engine.\
        \n\nSyntax :  .ipreverse <ip>\
        \nUsage : Perform reverse ip search.\
        \n\nSyntax :  .dnslookup <ip/host>\
        \nUsage : Find all dns ips of a ip/host address.\
        \n\nSyntax :  .ipwhois <ip>\
        \nUsage : Find whois information of an ip address.\
        \n\nSyntax :  .advanceip <ip/host>\
        \nUsage : Find the most detailed Geo information of an ip/host."
    }
) 
