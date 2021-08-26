OBSPokemonHUD
------------

![Screenshot of the OBS scripts window showing OBS Pokemon HUD's properties](readme_files/screenshot_obspokemonhud.png?raw=true)

OBSPokemonHUD is a way to have your current Pokemon team showing up in OBS and allow them to be updated by a JSON file. The JSON file can be manually edited or you use accompanying scripts to write them for you.

This project is based on an idea that [ShockSlayer](https://www.youtube.com/c/shockslayer "SS's YouTube Channel") [(his Twitch)](https://twitch.tv/shockslayer "SS's Twitch") came up with. Originally the project was named [SSPokemonHUD](https://github.com/guitaristtom/sspokemonhud), but that was janky mess between HTML, Python, and Javascript all being used in tandem. The idea was that it was a just a web site that you could use as a browser source and add to your scene, that way it didn't matter what broadcasting or recording software you were using.

There is also a [Team Editor](#team-editor) script that you can add to OBS's Scripts as well. That way you can manage your team without editing a JSON file directly, and from right within OBS itself.

## Premise
I have been wanting to redo this project from scratch for a couple years now, but between work and now school I haven't had a whole lot of time to do it.

## Install Instructions

Follow the instructions below if you don't have Python installed already and working with OBS.

If you do, then you may need to install the required [libraries](#libraries).

From there all you need to do is open up the Script dialog within OBS by going to `Tools` -> `Scripts`, and press the `+` button and add in `obspokemonhud.py`.

After you've done that, create six image sources on your scene of choice, just leave them blank for now. In the scripts dialog press `Reload Scripts` (the little spinny arrow icon).

Then in the `Slot X Image Source` dropdowns select the image sources for the six slots for your team. Set the height and width that you wish to have them all be. Set your `Sprite Style` to the one you'd like.

Copy `team.example.json` to a new file (it's a template). Usually you can call it `team.json`, but you can do whatever your heart desires. However in this README file it'll be referenced as `team.json`. Browse to the location of this new file for `Team JSON File`.

From there _you can_ change the `Update Interval` if you want, but there's usually no need.

Once you're done setting that up, check the `Run?` box to start the script. _This is here for if you aren't streaming using this script, as OBS is always running scripts in the background... You might need to save those extra CPU cycles_.

### Windows
You will need to have a version of Python 3.6 installed, as that's what OBS currently supports. Right now that is [Python 3.6.8](https://www.python.org/downloads/release/python-368/). 

**None of the versions on the Microsoft Store will work**. [OBS only supports Python 3.6](https://obsproject.com/docs/scripting.html) on Windows at this point in time, so Python 3.7, Python 3.8, or Python 3.9 on the Store won't work.

Make sure you install the version that matches your OBS install. If you install the 32-bit version of Python and try to use it with a 64-bit version of OBS it won't load up correctly and give an error similar to this in the log:

```
13:54:17.152: LoadLibrary failed for 'C:/Users/Thomas/AppData/Local/Programs/Python/Python36-32/python36.dll': %1 is not a valid Win32 application.
13:54:17.152:  (193)
13:54:17.152: [Python] Could not load library: C:/Users/Thomas/AppData/Local/Programs/Python/Python36-32/python36.dll
```

### Linux
All you should need is the `obs-studio` and `python` packages installed and setup on your distribution. If that isn't working, start up an [issue](issues/) and let me know what you had to do and I'll add notes for it here.

### Mac...
I'm not sure, I don't have a Mac system or VM to test this on. If someone would like to start an [issue](issues/) and give me instructions for how to install and set up OBS and Python, that would be appreciated.

## Libraries
You may need to install the `requests` library if it isn't already installed. You'll know you're missing it if the OBS script log shows an error about missing a library. It'll look like similar to this:

```
[obspokemonhud.py] Traceback (most recent call last):
[obspokemonhud.py]   File "F:/Downloads/obspokemonhud\obspokemonhud.py", line 9, in <module>
[obspokemonhud.py]     import requests
[obspokemonhud.py] ModuleNotFoundError: No module named 'requests'
```

This can be achieved by opening up a terminal or command prompt and running:
```
pip install requests
```

**If you have multiple versions of Python installed** you'll need to run that command under the specific version of Python that you are using with OBS.

Assuming that Python is installed in the default location, this can be achieved (in Windows) by going:
```
cd C:\Users\<username>\AppData\Local\Programs\Python\Python36
python.exe -m pip install requests
```

If Python is not installed in the default folder, you need to figure out where it is and change the `cd` command above to that folder.

Once this is done, restart OBS and the issue should be resolved.

## Team Editor
Within this repository there is a second Python file named `team_editor.py`. This allows for having it all self-contained within OBS, and not needing to open your `team.json` file in a text editor at all. You are still welcome to do it that way and not use this, this is just for people who prefer an "all-in-one" solution.

![Screenshot of the OBS scripts window showing the team editor properties](readme_files/screenshot_team_editor.png?raw=true)

To set it up all you have to do is add it to OBS. You do this by going to `Tools` -> `Scripts`, and press the `+` button and add in `team_editor.py`.

From there you browse for your `Team JSON File` (preferably the same location as the one you're using for `obspokemonhud.py`).

For updating your team just change it and press save. It'll save it to your chosen JSON file. The Team Editor in combination with the OBSPokemonHUD script will update the sources automagically on OBS.

If you are loading up a JSON file that you've used previously, you **have to reload the script** for the information to show properly in the Scripts dialog window. _It technically loads all of the information, but it just doesn't display it unless you either reload the script, close and reopen the window, or choose a different script and then back to this one._

## Notes
* If you're on Linux, you _might_ have to create any additional cache folders that aren't a part of the repository (custom maps, etc.)

## Donating
Someone mentioned that I should put this here in case people feel like donating a little bit to me and my projects


[![shield.io](https://img.shields.io/badge/buymeacoffee-thomashine-yellow)](https://www.buymeacoffee.com/thomashine)
[![shield.io](https://img.shields.io/badge/ko--fi-thomashine-blue)](https://ko-fi.com/thomashine)
