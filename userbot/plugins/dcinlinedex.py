from pokedex import pokedex as badhiya
import os
import shutil
from re import findall
import requests
from telethon import Button, custom, events
#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC

import requests
@tgbot.on(events.InlineQuery(pattern=r"pokedex (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):

    builder = event.builder
    query = event.text
    
    if event.query.user_id == bot.uid:
        pokemon = event.pattern_match.group(1)
        move = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
        rw = f"https://some-random-api.ml/pokedex?pokemon={pokemon}"
        w=requests.get(f"https://api.pokemontcg.io/v1/cards?name={pokemon}")
        lol=w.json()
        weaknesses=lol['cards'][0]['weaknesses'][0]['type']
        r = requests.get(rw)
        a=r.json()
        name=a['name']
        typ=a['type']
        species=a['species']
        abilities=a['abilities']
        height=a['height']
        weight=a['weight']
        esatge=r.json()['family']['evolutionStage']
        l=r.json()['family']['evolutionLine']
        if not l:
            line = 'None'
        else:
            line=', '.join(map(str, l))
        gen=a['generation']
        try:    move1=move.json()["moves"][0]['move']['name']
        except IndexError: pass
        try:    move2=move.json()["moves"][1]['move']['name']
        except IndexError: move2=None
        try:    move3=move.json()["moves"][2]['move']['name']
        except IndexError: move3=None
        try:    move4=move.json()["moves"][3]['move']['name']
        except IndexError : move4=None
        try:    move5=move.json()["moves"][4]['move']['name']
        except IndexError : move5=None
        try:    move6=move.json()["moves"][5]['move']['name']
        except IndexError : move6=None
        try:    move7=move.json()["moves"][6]['move']['name']
        except IndexError : move7=None
        description=a['description']
        typ=', '.join(map(str, typ))
        Stats=a['stats']
        species=', '.join(map(str, species))
        abilities=', '.join(map(str, abilities))
        poli = badhiya.Pokedex()
        pname = poli.get_pokemon_by_name(pokemon)
        pokemon = pname[0]
        lst=pokemon.get("sprite")

        cap=f'''

**NAME** : `{name}`
**TYPE** : `{typ}`
**SPECIES** : `{species}`
**Evolution Line** : `{line}`
**Evolution Stage** : `{esatge}`
**Generation** : `{gen}`
**ABILITIES** : `{abilities}`
**WEAKNESSES** :`{weaknesses}` 
**HEIGHT** : `{height}`
**WEIGHT** : `{weight}`

	**Stats**                               **Moves**
**Hp**      : `{Stats['hp']}`               `(1){move1}`
**Attack**  : `{Stats['attack']}`           `(2){move2}`   
**Defense** : `{Stats['defense']}`          `(3){move3}`   
**Sp_atk**  : `{Stats['sp_atk']}`           `(4){move4}`
**Sp_def**  : `{Stats['sp_def']}`           `(5){move5}`
**Speed**   : `{Stats['speed']}`            `(6){move6}`
**Total**   : `{Stats['total']}`            `(7){move7}`
**DESCRIPTION** : `{description}`
  '''
        result = builder.photo(lst,text=cap,buttons=[[Button.switch_inline("Search Again", query="pokedex ", same_peer=True)],], )
        await event.answer([result])
    if not event.query.user_id == bot.uid:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/DARK-COBRA/DARKCOBRA  ",buttons=[[Button.switch_inline("Search Again", query="pokedex ", same_peer=True)],], )
        await event.answer([resultm])
        return
#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC
@tgbot.on(events.InlineQuery(pattern=r"pokecard(.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    query = event.text
    
    if event.query.user_id == bot.uid:
        pokename=event.pattern_match.group(1)
        rw = f"https://api.pokemontcg.io/v1/cards?name={pokename}"
        r = requests.get(rw)
        a=r.json()
        o=a['cards'][0]['imageUrlHiRes']
        result = builder.photo(o,buttons=[[Button.switch_inline("Search Again", query="pokecard ", same_peer=True)],], )
        await event.answer([result])
    if not event.query.user_id == bot.uid:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/DARK-COBRA/DARKCOBRA   ",buttons=[[Button.switch_inline("Search Again", query="pokecard ", same_peer=True)],], )
        await event.answer([resultm])
        return
#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC#made by @THE_B_LACK_HAT @ Sh1vam #TEAM DC