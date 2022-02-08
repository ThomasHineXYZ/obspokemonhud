#!/usr/bin/python3
"""OBSPokemonHUD - Pre-Cache and Check Map Files

This pre-caches and tests the given map file by going through every entry and
downloading it locally. If an error shows up in the console, then either the
file in the map is wrong or it's missing from the server. (Like shiny starter
Eevee)
"""

import json
import os
import requests
import sys


# Double check that a map is given. Otherwise exit
if len(sys.argv) != 2:
    print("No map file given. Exitting...")
    sys.exit()

with open(sys.argv[1], 'r') as file:
    sprite_map = json.load(file)

for pokemon in sprite_map['sprites']:
    for form in sprite_map['sprites'][pokemon]:
        normal_link = sprite_map['urls']['normal'] + sprite_map['sprites'][pokemon][form]
        shiny_link = sprite_map['urls']['shiny'] + sprite_map['sprites'][pokemon][form]

        # Standard
        # Get the file name from the image link
        filename = normal_link.split("/")[-1]

        # Check that the file doesn't exist yet
        if not os.path.isfile("cache/" + sprite_map['cache_location'] + "/" + filename):
            # Do a request for the file
            response = requests.get(normal_link)

            # Check the image file's response code to see if it exists on their
            # end
            if response.status_code == 404:
                print("File not found: " + filename)

            elif response.status_code != 200:
                print("(" + str(response.status_code) + ")" + filename)

            # If it does, save it.
            else:
                with open("cache/" + sprite_map['cache_location'] + "/" + filename, "wb") as file:
                    file.write(response.content)

        # Shiny
        # Get the file name from the image link
        filename = shiny_link.split("/")[-1]

        # Check that the file doesn't exist yet
        if not os.path.isfile("cache/" + sprite_map['cache_location'] + "/shiny/" + filename):
            # Do a request for the file
            response = requests.get(shiny_link)

            # Check the image file's response code to see if it exists on their
            # end
            if response.status_code == 404:
                print("File not found: shiny/" + filename)

            elif response.status_code != 200:
                print("(" + str(response.status_code) + ") shiny/" + filename)

            # If it does, save it.
            else:
                with open("cache/" + sprite_map['cache_location'] + "/shiny/" + filename, "wb") as file:
                    file.write(response.content)
