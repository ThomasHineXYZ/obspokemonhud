"""OBSPokemonHUD

This is the main script for the OBSPokemonHUD project
"""

import obspython as obs

# Interval in seconds for the script to check the team file
check_interval = 5

# The location for the JSON file
json_file = ""

# Boolean to toggle if to run this or not
run_boolean = False

# Dictionary for the team sprite image sources
team_sprite_image_sources = {}


def script_description():
    """Sets up the description

    This is a built-in OBS function.

    It outputs the value for the description part of the "Scripts" window for
    this script.
    """
    return "Pokemon team HUD for OBS.\n\nBy GT"


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

    # Add in a file path property for the team.json file
    obs.obs_properties_add_path(properties, "json_file", "Team JSON File", obs.OBS_PATH_FILE, "*.json", None)

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

    # Finally, return the properties so they show up
    return properties


def script_defaults(settings):
    """Sets the default values

    This is a built-in OBS function.

    It sets all of the default values when the user presses the "Defaults"
    button on the "Scripts" screen.
    """
    obs.obs_data_set_default_bool(settings, "run_boolean", False)
    obs.obs_data_set_default_int(settings, "check_interval_int", 1)


def script_update(settings):
    """Updates the settings values

    This is a built-in OBS function.

    This runs whenever a setting is changed or updated for the script. It also
    sets up and removes the timer.
    """
    # Get all of the global variables assigned in here
    global check_interval
    global json_file
    global run_boolean
    global team_sprite_image_sources

    # Set up the check interval
    check_interval = obs.obs_data_get_int(settings, "check_interval_int")

    # Set up the json file location
    json_file = obs.obs_data_get_string(settings, "json_file")

    # Set up the team sprites
    team_sprite_image_sources["slot1"] = obs.obs_data_get_string(settings, "slot1_sprite_image_source")
    team_sprite_image_sources["slot2"] = obs.obs_data_get_string(settings, "slot2_sprite_image_source")
    team_sprite_image_sources["slot3"] = obs.obs_data_get_string(settings, "slot3_sprite_image_source")
    team_sprite_image_sources["slot4"] = obs.obs_data_get_string(settings, "slot4_sprite_image_source")
    team_sprite_image_sources["slot5"] = obs.obs_data_get_string(settings, "slot5_sprite_image_source")
    team_sprite_image_sources["slot6"] = obs.obs_data_get_string(settings, "slot6_sprite_image_source")

    # Set up the run bool
    run_boolean = obs.obs_data_get_bool(settings, "run_boolean")

    # NOTE Debug output for now
    print(check_interval)
    print(json_file)
    print(run_boolean)
    print(team_sprite_image_sources)

    # Remove the timer for the update_team function, if it exists
    obs.timer_remove(update_team)

    # If the run boolean is false, return out
    if not run_boolean:
        return

    # If the json file isn't given, return out
    if not json_file:
        return

    # If not all of the team slots are set, return out
    if not (
        team_sprite_image_sources["slot1"] and
        team_sprite_image_sources["slot2"] and
        team_sprite_image_sources["slot3"] and
        team_sprite_image_sources["slot4"] and
        team_sprite_image_sources["slot5"] and
        team_sprite_image_sources["slot6"]
    ):
        return

    # So now, if everything is set up then set the timer
    obs.timer_add(update_team, check_interval * 1000)


def update_team():
    print("update test")
