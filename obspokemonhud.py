"""OBSPokemonHUD

This is the main script for the OBSPokemonHUD project
"""

import json
import obspython as obs
import os.path
import requests
import pathlib

# Interval in seconds for the script to check the team file
check_interval = 5

# Enabled for some extra debug output to the script log
# True or False (they need to be capitals for Python)
debug = False

# The location for the JSON file
json_file = ""
json_file_contents = {}

# Boolean to toggle if to run this or not
run_boolean = False

# The style for the sprites to use
sprite_map = {}

# Possible styles for sprites to use
sprite_types = []

# Dictionary for the team sprite image sources
team_sprite_image_sources = []


def script_description():
    """Sets up the description

    This is a built-in OBS function.

    It outputs the value for the description part of the "Scripts" window for
    this script.
    """
    return "OBSPokemonHUD script for OBS.\nBy Tom."


def script_properties():
    """Sets up the properties section of the "Scripts" window.

    This is a built-in OBS function.

    It sets up the properties part of the "Scripts" screen for this script.

    Returns:
        properties
    """
    # Declare the properties object for us to mess with
    properties = obs.obs_properties_create()

    # Put a boolean checkbox for if this should be running or not
    obs.obs_properties_add_bool(properties, "run_boolean", "Run?")

    # Integer for how often (in seconds) this checks for changes
    obs.obs_properties_add_int(properties, "check_interval_int", "Update Interval (seconds)", 1, 120, 1)

    # Width and height
    obs.obs_properties_add_int(properties, "sprite_height", "Height (pixels)", 1, 1000, 1)
    obs.obs_properties_add_int(properties, "sprite_width", "Width (pixels)", 1, 1000, 1)

    # Add in a file path property for the team.json file
    obs.obs_properties_add_path(properties, "json_file", "Team JSON File", obs.OBS_PATH_FILE, "*.json", None)

    # Set up the sprite style dropdown
    sprite_style = obs.obs_properties_add_list(
        properties,
        "sprite_style",
        "Sprite Style",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING
    )
    # Automatically build sprite maps
    sprite_types = [s for s in os.listdir(script_path()) if '.json' in s]
    for x in sprite_types:
        if 'map' in x and 'example' not in x:
            map = x.replace('map_','').replace('.json','')
            obs.obs_property_list_add_string(sprite_style, map, map)

    # Team image locations.
    # Set up the settings and add in a blank value as the first value
    slot1_sprite_image_source = obs.obs_properties_add_list(
        properties,
        "slot1_sprite_image_source",
        "Slot 1 Image Source",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING
    )
    obs.obs_property_list_add_string(slot1_sprite_image_source, "", "")

    slot2_sprite_image_source = obs.obs_properties_add_list(
        properties,
        "slot2_sprite_image_source",
        "Slot 2 Image Source",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING
    )
    obs.obs_property_list_add_string(slot2_sprite_image_source, "", "")

    slot3_sprite_image_source = obs.obs_properties_add_list(
        properties,
        "slot3_sprite_image_source",
        "Slot 3 Image Source",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING
    )
    obs.obs_property_list_add_string(slot3_sprite_image_source, "", "")

    slot4_sprite_image_source = obs.obs_properties_add_list(
        properties,
        "slot4_sprite_image_source",
        "Slot 4 Image Source",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING
    )
    obs.obs_property_list_add_string(slot4_sprite_image_source, "", "")

    slot5_sprite_image_source = obs.obs_properties_add_list(
        properties,
        "slot5_sprite_image_source",
        "Slot 5 Image Source",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING
    )
    obs.obs_property_list_add_string(slot5_sprite_image_source, "", "")

    slot6_sprite_image_source = obs.obs_properties_add_list(
        properties,
        "slot6_sprite_image_source",
        "Slot 6 Image Source",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING
    )
    obs.obs_property_list_add_string(slot6_sprite_image_source, "", "")

    # Iterate through each source in OBS, grabbing and adding the image ones in
    # to the list for each of the team member sources
    sources = obs.obs_enum_sources()
    if sources is not None:
        for source in sources:
            source_id = obs.obs_source_get_unversioned_id(source)
            if source_id == "image_source":
                name = obs.obs_source_get_name(source)
                obs.obs_property_list_add_string(slot1_sprite_image_source, name, name)
                obs.obs_property_list_add_string(slot2_sprite_image_source, name, name)
                obs.obs_property_list_add_string(slot3_sprite_image_source, name, name)
                obs.obs_property_list_add_string(slot4_sprite_image_source, name, name)
                obs.obs_property_list_add_string(slot5_sprite_image_source, name, name)
                obs.obs_property_list_add_string(slot6_sprite_image_source, name, name)

    # Apparently we have to release the list of sources once we are done with
    # them
    obs.source_list_release(sources)

    # If debug is enabled, print out this bit of text
    if debug:
        print("Function: Properties")

    # Finally, return the properties so they show up
    return properties


def script_defaults(settings):
    """Sets the default values

    This is a built-in OBS function.

    It sets all of the default values when the user presses the "Defaults"
    button on the "Scripts" screen.
    """

    # If debug is enabled, print out this bit of text
    if debug:
        print("Function: Defaults")

    # Set the run boolean as false by default, just in case
    obs.obs_data_set_default_bool(settings, "run_boolean", False)

    # Set the default update interval at 1 second
    obs.obs_data_set_default_int(settings, "check_interval_int", 1)

    obs.obs_data_set_default_int(settings, "sprite_height", 50)
    obs.obs_data_set_default_int(settings, "sprite_width", 50)

    # Set the default sprite style as using the Showdown type
    obs.obs_data_set_default_string(settings, "sprite_style", "Showdown")


def script_update(settings):
    """Updates the settings values

    This is a built-in OBS function.

    This runs whenever a setting is changed or updated for the script. It also
    sets up and removes the timer.
    """

    # If debug is enabled, print out this bit of text
    if debug:
        print("Function: Script Update")

    # Get all of the global variables assigned in here
    global check_interval
    global json_file
    global run_boolean
    global sprite_map
    global sprite_style
    global team_sprite_image_sources

    # Set up the check interval
    check_interval = obs.obs_data_get_int(settings, "check_interval_int")

    sprite_height = obs.obs_data_get_int(settings, "sprite_height")
    sprite_width = obs.obs_data_get_int(settings, "sprite_width")

    # Set up the json file location
    json_file = obs.obs_data_get_string(settings, "json_file")

    # Set up the team sprites
    team_sprite_image_sources = [
        obs.obs_data_get_string(settings, "slot1_sprite_image_source"),
        obs.obs_data_get_string(settings, "slot2_sprite_image_source"),
        obs.obs_data_get_string(settings, "slot3_sprite_image_source"),
        obs.obs_data_get_string(settings, "slot4_sprite_image_source"),
        obs.obs_data_get_string(settings, "slot5_sprite_image_source"),
        obs.obs_data_get_string(settings, "slot6_sprite_image_source")
    ]

    for source in team_sprite_image_sources:
        setup_source(source, sprite_height, sprite_width)

    # Set up the sprite style
    sprite_style = obs.obs_data_get_string(settings, "sprite_style")

    # Set up the run bool
    run_boolean = obs.obs_data_get_bool(settings, "run_boolean")

    # Remove the timer for the update_team function, if it exists
    obs.timer_remove(update_team)

    # If the run boolean is false, return out
    if not run_boolean:
        return

    # If the json file isn't given, return out
    if not json_file:
        return

    # If the sprite style isn't chosen
    if not sprite_style:
        return

    # If not all of the team slots are set, return out
    if not (
        team_sprite_image_sources[0] and
        team_sprite_image_sources[1] and
        team_sprite_image_sources[2] and
        team_sprite_image_sources[3] and
        team_sprite_image_sources[4] and
        team_sprite_image_sources[5]
    ):
        return

    # Load up the sprite map
    with open(f"{script_path()}map_{sprite_style}.json", 'r') as file:
        sprite_map = json.load(file)

    # So now, if everything is set up then set the timer
    obs.timer_add(update_team, check_interval * 1000)


def update_team():
    """Updates the different sources for the team

    This function gets run on a timer, loading up a JSON file and running the
    different update functions
    """
    # If debug is enabled, print out this bit of text
    if debug:
        print("Function: Update team")

    # Set up the required global variables
    global json_file
    global json_file_contents
    global team_sprite_image_sources

    # Load up the JSON file in to a dictionary
    with open(json_file, 'r') as file:
        array = json.load(file)
    if sprite_style is not array['map']:
        array['map'] = sprite_style
        with open(json_file, 'w') as file:
            json.dump(array, file, indent=4)

    # If the JSON file hasn't changed since the last check, just return out
    if json_file_contents == array:
        return
    else:
        json_file_contents = array

    # Update all of the team sprites
    update_sprite_sources(team_sprite_image_sources[0], json_file_contents['slot1'])
    update_sprite_sources(team_sprite_image_sources[1], json_file_contents['slot2'])
    update_sprite_sources(team_sprite_image_sources[2], json_file_contents['slot3'])
    update_sprite_sources(team_sprite_image_sources[3], json_file_contents['slot4'])
    update_sprite_sources(team_sprite_image_sources[4], json_file_contents['slot5'])
    update_sprite_sources(team_sprite_image_sources[5], json_file_contents['slot6'])


def update_sprite_sources(source_name, team_slot):
    """Updates the settings values

    Gets called by update_team.

    Given the source name list, it updates the path for the sprite sources
    """

    # If debug is enabled, print out this bit of text
    if debug:
        print("Function: Update sprite sources")

    # If the dex number is zero or null, then give it the empty GIF file so
    # they can set sizing
    if (not team_slot["dexnumber"]) or (team_slot["dexnumber"] == 0):
        location = f"{script_path()}empty.gif"
    else:
        sprite = get_sprite_location(
            sprite_map['urls'],
            sprite_map['sprites'],
            team_slot['shiny'],
            team_slot["dexnumber"],
            team_slot["variant"]
        )
        location = cache_image(
            sprite,
            team_slot['shiny'],
            sprite_map['cache_location'],
            "sprites"
        )

    source = obs.obs_get_source_by_name(source_name)
    if source is not None:
        # Set the text element as being the local cached version of the file
        settings = obs.obs_data_create()
        obs.obs_data_set_string(settings, "file", location)
        obs.obs_source_update(source, settings)
        obs.obs_data_release(settings)

        # Release the source
        obs.obs_source_release(source)


def get_sprite_location(urls, sprites, shiny, dex_number, variant):
    # If debug is enabled, print out this bit of text
    if debug:
        print("Function: Get Sprite sources")

    link = ""
    if shiny:
        link = urls['shiny']
    else:
        link = urls['normal']

    if str(dex_number) not in sprites.keys():
        print("I don't belong")
        return

    if variant in sprites[str(dex_number)].keys():
        return link + sprites[str(dex_number)][variant]

    # If the given forms, genders, etc aren't available, just give the standard
    # sprite
    return link + sprites[str(dex_number)]['standard']


def cache_image(link, shiny, location, image_type):
    # If debug is enabled, print out this bit of text
    if debug:
        print("Function: Cache image")

    # Set the cache folder
    cache_folder = f"{script_path()}cache/{location}/"

    # If it's a shiny, tack that on to the end
    if shiny:
        cache_folder += "shiny/"

    # Get the file name from the image link
    filename = link.split("/")[-1]

    # Check if doesn't exist. If so, then download it and store it in the cache
    if not os.path.isfile(cache_folder + filename):
        r = requests.get(link)
        with open(cache_folder + filename, "wb") as f:
            f.write(r.content)

    return cache_folder + filename


def setup_source(source_name, height, width):
    # If debug is enabled, print out this bit of text
    if debug:
        print("Function: Setup source")

    # Get the current scene
    current_scene = obs.obs_frontend_get_current_scene()
    scene = obs.obs_scene_from_source(current_scene)
    obs.obs_source_release(current_scene)

    # Grab the source
    source = obs.obs_scene_find_source(scene, source_name)

    # This makes sure that the scaling is done right
    obs.obs_sceneitem_set_bounds_type(source, obs.OBS_BOUNDS_SCALE_INNER)

    # Set the bounding box size
    new_scale = obs.vec2()
    new_scale.x = height
    new_scale.y = width
    obs.obs_sceneitem_set_bounds(source, new_scale)
