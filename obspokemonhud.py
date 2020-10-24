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
    return "Pokemon team HUD for OBS.\n\nBy GT"


def script_properties():
    # Declare the properties object for us to mess with
    properties = obs.obs_properties_create()

    obs.obs_properties_add_int(properties, "check_interval", "Update Interval (seconds)", 1, 120, 1)

    # Add in a file path property for the team.json file
    obs.obs_properties_add_path(properties, "team_file", "Team JSON File", obs.OBS_PATH_FILE, "*.json", None)

    # Team image locations
    image_list1 = obs.obs_properties_add_list(properties, "source1", "Team Member 1", obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
    image_list2 = obs.obs_properties_add_list(properties, "source2", "Team Member 2", obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
    image_list3 = obs.obs_properties_add_list(properties, "source3", "Team Member 3", obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
    image_list4 = obs.obs_properties_add_list(properties, "source4", "Team Member 4", obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
    image_list5 = obs.obs_properties_add_list(properties, "source5", "Team Member 5", obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
    image_list6 = obs.obs_properties_add_list(properties, "source6", "Team Member 6", obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
    sources = obs.obs_enum_sources()
    if sources is not None:
        for source in sources:
            source_id = obs.obs_source_get_unversioned_id(source)
            if source_id == "image_source":
                name = obs.obs_source_get_name(source)
                obs.obs_property_list_add_string(image_list1, name, name)
                obs.obs_property_list_add_string(image_list2, name, name)
                obs.obs_property_list_add_string(image_list3, name, name)
                obs.obs_property_list_add_string(image_list4, name, name)
                obs.obs_property_list_add_string(image_list5, name, name)
                obs.obs_property_list_add_string(image_list6, name, name)

    # Finally, return the properties so they show up
    return properties
