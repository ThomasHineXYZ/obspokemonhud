
import json
import re

import requests
from bs4 import BeautifulSoup

dex = 0
pkmnList = []

# set the json header
pkmnDict = {"cache_location": "HOME", "urls": {
        "normal": "https://img.pokemondb.net/sprites/home/normal/",
        "shiny": "https://img.pokemondb.net/sprites/home/shiny/"}, "sprites": {}}

# initialize the dictionary
pkmnDict["sprites"]["0"] = {"i": 1}

# get the sprites main page
page = requests.get("https://pokemondb.net/sprites")
data = page.text
soup = BeautifulSoup(data)

# get all the pokemon names
for link in soup.find_all('a'):
    if "/sprites/" in link['href']:
        pkmnName = str(link['href']).replace('/sprites/', '')
        pkmnList.append(pkmnName)

# iterate through the pokemon names
for pkmn in pkmnList:
    dex = dex + 1
    # initialize the current dex number
    pkmnDict["sprites"][str(dex-1)].pop("i")
    pkmnDict["sprites"][str(dex)] = {"i": 1}
    print(str(dex-1) + '. ' +
          str(pkmnDict["sprites"][str(dex-1)]).replace('{', '').replace('}', ''))
    # get the current pokemon's web page
    url = 'https://pokemondb.net/sprites/' + pkmn
    response = requests.get(url)
    page = BeautifulSoup(response.content)
    # iterate through all sprites for the current pokemon
    for item in page.find_all(href=re.compile("home/normal")):
        pkmnName = str(item['href']).replace(
            'https://img.pokemondb.net/sprites/home/normal/', '')
        # check for variants
        if '-' not in pkmnName and 'female' not in pkmnDict['sprites'][str(dex)]:
            pkmnDict["sprites"][str(dex)]["standard"] = pkmnName
        else:
            variant = pkmnName.replace(pkmn + '-', '').replace('.png', '')
            if '-' not in pkmnName:
                variant = 'male'
            elif 'f' in variant:
                variant = 'female'
            elif 'mega-x' in variant:
                variant = 'mega x'
            elif 'mega-y' in variant:
                variant = 'mega y'
            pkmnDict["sprites"][str(dex)][variant.replace('-', ' ')] = pkmnName

# remove the current initialization key
pkmnDict["sprites"][str(dex)].pop("i")

# export to json
with open('map_HOME_new.json', 'w', encoding='utf8') as json_file:
    json.dump(pkmnDict, json_file, indent=4, ensure_ascii=False)
