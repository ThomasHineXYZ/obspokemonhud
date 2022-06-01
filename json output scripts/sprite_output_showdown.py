
import json
import re

import requests
from bs4 import BeautifulSoup

# do this because showdown is dumb and makes the pokemon alphabetical
pkmnFile = open("pkmn_list.csv", 'r')
csvList = pkmnFile.read()
pkmnList = csvList.split(',')
pkmnFile.close()

dex = 0

# set the json header
pkmnDict = {"cache_location": "Showdown", "urls": {
        "normal": "https://play.pokemonshowdown.com/sprites/ani/",
        "shiny": "https://play.pokemonshowdown.com/sprites/ani-shiny/"
    }, "sprites": {}}

# initialize the dictionary
pkmnDict["sprites"]["0"] = {"i": 1}

# get the sprites main page
page = requests.get("https://play.pokemonshowdown.com/sprites/ani")
data = page.text
soup = BeautifulSoup(data)
webList = []


response = requests.get('https://play.pokemonshowdown.com/sprites/ani/')
page = BeautifulSoup(response.content)

# iterate through all sprites for the current pokemon
for item in page.find_all('a'):
    if 'gif' in str(item['href']):
        webList.append(str(item['href']))

# iterate through the pokemon names
for pkmn in pkmnList:
    dex = dex + 1
    # initialize the current dex number
    pkmnDict["sprites"][str(dex-1)].pop("i")
    pkmnDict["sprites"][str(dex)] = {"i": 1}
    print(str(dex-1) + '. ' +
          str(pkmnDict["sprites"][str(dex-1)]).replace('{', '').replace('}', ''))

    # pull list of all url variants to make the list be in proper dex order
    pkmnVariants = [name for name in webList if pkmn in name]

    # iterate through all files found
    for pkmnName in pkmnVariants:
        # check for variants
        if '-' not in pkmnName and 'female' not in pkmnDict['sprites'][str(dex)]:
            pkmnDict["sprites"][str(dex)]["standard"] = pkmnName
        else:
            variant = pkmnName.replace(pkmn + '-', '').replace('.gif', '')
            if '-' not in pkmnName:
                variant = 'male'
            elif '-f' in variant:
                variant = 'female'
            elif 'megax' in variant:
                variant = 'mega x'
            elif 'megay' in variant:
                variant = 'mega y'
            pkmnDict["sprites"][str(dex)][variant.replace(
                '-', ' ')] = pkmnName

# remove the current initialization key
pkmnDict["sprites"][str(dex)].pop("i")
pkmnDict["sprites"].pop("0")

# export to json
with open('map_Showdown_new.json', 'w', encoding='utf8') as json_file:
    json.dump(pkmnDict, json_file, indent=4, ensure_ascii=False)
