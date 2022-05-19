"""OBSPokemonHUD - Team Editor

This is the team editor script for OBS, so you can do it all self-contained
"""

import json
import obspython as obs

# Enabled for some extra debug output to the script log
# True or False (they need to be capitals for Python)
debug = False

# The location for the JSON file
json_file = ""

# Team information
team = {
    "slot1": {
        "dexnumber": 0,
        "shiny": False,
    },
    "slot2": {
        "dexnumber": 0,
        "shiny": False,
    },
    "slot3": {
        "dexnumber": 0,
        "shiny": False,
    },
    "slot4": {
        "dexnumber": 0,
        "shiny": False,
    },
    "slot5": {
        "dexnumber": 0,
        "shiny": False,
    },
    "slot6": {
        "dexnumber": 0,
        "shiny": False,
    },
}


def script_description():
    """Sets up the description

    This is a built-in OBS function.

    It outputs the value for the description part of the "Scripts" window for
    this script.
    """
    return "OBSPokemonHUD - Team Editor.\nAlso by Tom."


def script_properties():
    """Sets up the properties section of the "Scripts" window.

    This is a built-in OBS function.

    It sets up the properties part of the "Scripts" screen for this script.

    Returns:
        properties
    """

    # Declare the properties object for us to mess with
    properties = obs.obs_properties_create()

    # Add in a file path property for the team.json file
    obs.obs_properties_add_path(properties, "json_file", "Team JSON File", obs.OBS_PATH_FILE, "*.json", None)

    # Set up the sprite style dropdown
    display_type = obs.obs_properties_add_list(
        properties,  # The properties variable
        "display_type",  # Setting identifier string
        "Display Type",  # Localized name shown to user
        obs.OBS_COMBO_TYPE_LIST,  # Whether it's editable or not
        obs.OBS_COMBO_FORMAT_STRING,  # The type of format to display
    )
    obs.obs_property_list_add_string(
        display_type,
        "Dex",
        "dex"
    )

    # ------------------------------------------------------

    obs.obs_properties_add_int(
        properties,  # The properties variable
        "team_member_dex_1",  # Setting identifier string
        "Member 1 (Dex No.)",  # display name
        0,  # Starting number
        898,  # Ending number
        1,  # Increment by
    )
    variant_1 = obs.obs_properties_add_list(
        properties,
        "variant_1",
        "Variant",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING,
    )
    obs.obs_properties_add_bool(
        properties,  # The properties variable
        "team_member_shiny_1",  # Setting identifier string
        "Member 1 Shiny?",  # display name
    )

    obs.obs_properties_add_int(
        properties,  # The properties variable
        "team_member_dex_2",  # Setting identifier string
        "Member 2 (Dex No.)",  # display name
        0,  # Starting number
        898,  # Ending number
        1,  # Increment by
    )
    variant_2 = obs.obs_properties_add_list(
        properties,
        "variant_2",
        "Variant",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING,
    )
    obs.obs_properties_add_bool(
        properties,  # The properties variable
        "team_member_shiny_2",  # Setting identifier string
        "Member 2 Shiny?",  # display name
    )

    obs.obs_properties_add_int(
        properties,  # The properties variable
        "team_member_dex_3",  # Setting identifier string
        "Member 3 (Dex No.)",  # display name
        0,  # Starting number
        898,  # Ending number
        1,  # Increment by
    )
    variant_3 = obs.obs_properties_add_list(
        properties,
        "variant_3",
        "Variant",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING,
    )
    obs.obs_properties_add_bool(
        properties,  # The properties variable
        "team_member_shiny_3",  # Setting identifier string
        "Member 3 Shiny?",  # display name
    )

    obs.obs_properties_add_int(
        properties,  # The properties variable
        "team_member_dex_4",  # Setting identifier string
        "Member 4 (Dex No.)",  # display name
        0,  # Starting number
        898,  # Ending number
        1,  # Increment by
    )
    variant_4 = obs.obs_properties_add_list(
        properties,
        "variant_4",
        "Variant",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING,
    )
    obs.obs_properties_add_bool(
        properties,  # The properties variable
        "team_member_shiny_4",  # Setting identifier string
        "Member 4 Shiny?",  # display name
    )

    obs.obs_properties_add_int(
        properties,  # The properties variable
        "team_member_dex_5",  # Setting identifier string
        "Member 5 (Dex No.)",  # display name
        0,  # Starting number
        898,  # Ending number
        1,  # Increment by
    )
    variant_5 = obs.obs_properties_add_list(
        properties,
        "variant_5",
        "Variant",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING,
    )
    obs.obs_properties_add_bool(
        properties,  # The properties variable
        "team_member_shiny_5",  # Setting identifier string
        "Member 5 Shiny?",  # display name
    )

    obs.obs_properties_add_int(
        properties,  # The properties variable
        "team_member_dex_6",  # Setting identifier string
        "Member 6 (Dex No.)",  # display name
        0,  # Starting number
        898,  # Ending number
        1,  # Increment by
    )
    variant_6 = obs.obs_properties_add_list(
        properties,
        "variant_6",
        "Variant",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING,
    )
    obs.obs_properties_add_bool(
        properties,  # The properties variable
        "team_member_shiny_6",  # Setting identifier string
        "Member 6 Shiny?",  # display name
    )

    obs.obs_properties_add_button(
        properties,  # The properties variable
        "save_button",  # Setting identifier string
        "Save",
        save_button_clicked
    )

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

    # Team member dex no.
    obs.obs_data_set_default_int(settings, "team_member_dex_1", 0)
    obs.obs_data_set_default_int(settings, "team_member_dex_2", 0)
    obs.obs_data_set_default_int(settings, "team_member_dex_3", 0)
    obs.obs_data_set_default_int(settings, "team_member_dex_4", 0)
    obs.obs_data_set_default_int(settings, "team_member_dex_5", 0)
    obs.obs_data_set_default_int(settings, "team_member_dex_6", 0)

    # Team member shiny state
    obs.obs_data_set_default_bool(settings, "team_member_shiny_1", False)
    obs.obs_data_set_default_bool(settings, "team_member_shiny_2", False)
    obs.obs_data_set_default_bool(settings, "team_member_shiny_3", False)
    obs.obs_data_set_default_bool(settings, "team_member_shiny_4", False)
    obs.obs_data_set_default_bool(settings, "team_member_shiny_5", False)
    obs.obs_data_set_default_bool(settings, "team_member_shiny_6", False)

    # If debug is enabled, print out this bit of text
    if debug:
        print("Function: Defaults")


def script_update(settings):
    """Updates the settings values

    This is a built-in OBS function.

    This runs whenever a setting is changed or updated for the script. It also
    sets up and removes the timer.
    """

    global json_file
    global team

    # If the team json file isn't given, return out so nothing happens
    if not obs.obs_data_get_string(settings, "json_file"):
        if debug:
            print("Conditional: Returning because no JSON file is given")
        return

    if json_file != obs.obs_data_get_string(settings, "json_file"):
        # If debug is enabled, print out this bit of text
        if debug:
            print("Conditional: New JSON File")

        json_file = obs.obs_data_get_string(settings, "json_file")

        with open(obs.obs_data_get_string(settings, "json_file"), 'r') as file:
            new_team_data = json.load(file)

        obs.obs_data_set_int(settings, "team_member_dex_1", new_team_data['slot1']['dexnumber'])
        obs.obs_data_set_int(settings, "team_member_dex_2", new_team_data['slot2']['dexnumber'])
        obs.obs_data_set_int(settings, "team_member_dex_3", new_team_data['slot3']['dexnumber'])
        obs.obs_data_set_int(settings, "team_member_dex_4", new_team_data['slot4']['dexnumber'])
        obs.obs_data_set_int(settings, "team_member_dex_5", new_team_data['slot5']['dexnumber'])
        obs.obs_data_set_int(settings, "team_member_dex_6", new_team_data['slot6']['dexnumber'])

        obs.obs_data_set_bool(settings, "team_member_shiny_1", new_team_data['slot1']['shiny'])
        obs.obs_data_set_bool(settings, "team_member_shiny_2", new_team_data['slot2']['shiny'])
        obs.obs_data_set_bool(settings, "team_member_shiny_3", new_team_data['slot3']['shiny'])
        obs.obs_data_set_bool(settings, "team_member_shiny_4", new_team_data['slot4']['shiny'])
        obs.obs_data_set_bool(settings, "team_member_shiny_5", new_team_data['slot5']['shiny'])
        obs.obs_data_set_bool(settings, "team_member_shiny_6", new_team_data['slot6']['shiny'])

    # Update the dex numbers
    team['slot1']['dexnumber'] = obs.obs_data_get_int(settings, "team_member_dex_1")
    team['slot2']['dexnumber'] = obs.obs_data_get_int(settings, "team_member_dex_2")
    team['slot3']['dexnumber'] = obs.obs_data_get_int(settings, "team_member_dex_3")
    team['slot4']['dexnumber'] = obs.obs_data_get_int(settings, "team_member_dex_4")
    team['slot5']['dexnumber'] = obs.obs_data_get_int(settings, "team_member_dex_5")
    team['slot6']['dexnumber'] = obs.obs_data_get_int(settings, "team_member_dex_6")

    # Update their shiny-ness
    team['slot1']['shiny'] = obs.obs_data_get_bool(settings, "team_member_shiny_1")
    team['slot2']['shiny'] = obs.obs_data_get_bool(settings, "team_member_shiny_2")
    team['slot3']['shiny'] = obs.obs_data_get_bool(settings, "team_member_shiny_3")
    team['slot4']['shiny'] = obs.obs_data_get_bool(settings, "team_member_shiny_4")
    team['slot5']['shiny'] = obs.obs_data_get_bool(settings, "team_member_shiny_5")
    team['slot6']['shiny'] = obs.obs_data_get_bool(settings, "team_member_shiny_6")

    # If debug is enabled, print out this bit of text
    if debug:
        print("Function: Script Update")


def save_button_clicked(properties, p):
    """Activates when the save button is pressed

    Args:
        properties (SwigPyObject): ¯\\_(ツ)_/¯
        p (SwigPyObject): ¯\\_(ツ)_/¯
    """

    save_team()


def save_team():
    """Saves the team information in to the team.json file that has been given

    Returns:
        None: Returns / exits the function if no JSON file is set
    """

    global json_file
    global team

    if not json_file:
        return

    with open(json_file, 'w') as file:
        json.dump(team, file, indent=4)

    if debug:
        print("Function: save_team")
        print(f"JSON file: {json_file}")
        print(f"Team data: {json.dumps(team)}")
