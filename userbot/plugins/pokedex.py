from pokedex import pokedex as badhiya
import os
import shutil
from re import findall
from userbot.utils import admin_cmd
import requests
@borg.on(admin_cmd(pattern="pokedex ?(.*)"))
#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG
async def pokedex(event):

    await event.edit("`Booting up the pokedex.......`")
    pokemon = event.pattern_match.group(1)

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
    line='\n'.join(map(str, l))
    gen=a['generation']
    description=a['description']
    typ=', '.join(map(str, typ))
    Stats=a['stats']
    species=','.join(map(str, species))
    abilities=','.join(map(str, abilities))
    poli = badhiya.Pokedex()
    pname = poli.get_pokemon_by_name(pokemon)
    pokemon = pname[0]
    lst=pokemon.get("sprite")
    cap=f'''

**NAME** : `{name}`
**TYPE** : `{typ}`
**SPECIES** : `{species}`
**Evolution Line : `{line}`
**Evolution Stage** : `{esatge}`
**Generation** : `{gen}`
**ABILITIES** : `{abilities}`
**WEAKNESSES** :`{weaknesses}` 
**HEIGHT** : `{height}`
**WEIGHT** : `{weight}`

**Stats**
\n

**Hp** : `{Stats['hp']}`
**Attack** : `{Stats['attack']}`
**Defense** : `{Stats['defense']}`
**Sp_atk** : `{Stats['sp_atk']}`
**Sp_def** : `{Stats['sp_def']}`
**Speed** : `{Stats['speed']}`
**Total** : `{Stats['total']}`

**DESCRIPTION** : `{description}`
  
    '''
    await event.client.send_file(await event.client.get_input_entity(event.chat_id), lst, caption=cap)
    await event.delete()
#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG

@borg.on(admin_cmd(pattern="pokecard ?(.*)"))
async def pokedex(event):
    pokename=event.pattern_match.group(1)
    rw = f"https://api.pokemontcg.io/v1/cards?name={pokename}"
    r = requests.get(rw)
    a=r.json()
    o=a['cards'][0]['imageUrlHiRes']
    await event.client.send_file(await event.client.get_input_entity(event.chat_id), o)
    await event.delete()
#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG#made by @THE_B_LACK_HAT #team dc DONOT KANG