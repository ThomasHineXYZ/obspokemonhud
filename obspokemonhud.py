"""OBSPokemonHUD

This is the main script for the OBSPokemonHUD project
"""

import obspython as obs

# Interval in seconds for the script to check the team file
check_interval = 5

# Global storage for the team image sources
team_image_sources = {
    "member1": None,
    "member2": None,
    "member3": None,
    "member4": None,
    "member5": None,
    "member6": None,
}


def script_description():
    """Sets up the description

    This is a built-in OBS function. It outputs the value for the description
    part of the "Scripts" window for this script
    """
    return "Pokemon team HUD for OBS.\n\nBy GT"


def script_properties():
    """Sets up the properties section of the "Scripts" window.

    This is a built-in OBS function. It sets up the properties part of the
    "Scripts" screen for this script

    Returns:
        properties
    """
    # Declare the properties object for us to mess with
    properties = obs.obs_properties_create()

    # Put a boolean checkbox for if this should be running or not
    obs.obs_properties_add_bool(properties, "toggle_start", "Run?")

    # Integer for how often (in seconds) this checks for changes
    obs.obs_properties_add_int(properties, "check_interval", "Update Interval (seconds)", 1, 120, 1)

    # Add in a file path property for the team.json file
    obs.obs_properties_add_path(properties, "team_file", "Team JSON File", obs.OBS_PATH_FILE, "*.json", None)

    # Team image locations.
    # Set up the settings and add in a blank value as the first value
    slot1_image_source = obs.obs_properties_add_list(
        properties,
        "source1",
        "Slot 1 Image Source",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING
    )
    obs.obs_property_list_add_string(slot1_image_source, "", "")

    slot2_image_source = obs.obs_properties_add_list(
        properties,
        "source2",
        "Slot 2 Image Source",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING
    )
    obs.obs_property_list_add_string(slot2_image_source, "", "")

    slot3_image_source = obs.obs_properties_add_list(
        properties,
        "source3",
        "Slot 3 Image Source",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING
    )
    obs.obs_property_list_add_string(slot3_image_source, "", "")

    slot4_image_source = obs.obs_properties_add_list(
        properties,
        "source4",
        "Slot 4 Image Source",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING
    )
    obs.obs_property_list_add_string(slot4_image_source, "", "")

    slot5_image_source = obs.obs_properties_add_list(
        properties,
        "source5",
        "Slot 5 Image Source",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING
    )
    obs.obs_property_list_add_string(slot5_image_source, "", "")

    slot6_image_source = obs.obs_properties_add_list(
        properties,
        "source6",
        "Slot 6 Image Source",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING
    )
    obs.obs_property_list_add_string(slot6_image_source, "", "")
    sources = obs.obs_enum_sources()

    # Iterate through each source in OBS, grabbing and adding the image ones in
    # to the list for each of the team member sources
    if sources is not None:
        for source in sources:
            source_id = obs.obs_source_get_unversioned_id(source)
            if source_id == "image_source":
                name = obs.obs_source_get_name(source)
                obs.obs_property_list_add_string(slot1_image_source, name, name)
                obs.obs_property_list_add_string(slot2_image_source, name, name)
                obs.obs_property_list_add_string(slot3_image_source, name, name)
                obs.obs_property_list_add_string(slot4_image_source, name, name)
                obs.obs_property_list_add_string(slot5_image_source, name, name)
                obs.obs_property_list_add_string(slot6_image_source, name, name)

    # Finally, return the properties so they show up
    return properties


def script_defaults(settings):
    """Sets the default values

    This is a built-in OBS function. It sets all of the default values when the
    user presses the "Defaults" button on the "Scripts" screen
    """
    obs.obs_data_set_default_bool(settings, "toggle_start", False)
    obs.obs_data_set_default_int(settings, "check_interval", 1)
