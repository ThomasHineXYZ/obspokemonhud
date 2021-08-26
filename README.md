OBSPokemonHUD
------------

![Screenshot of the OBS scripts window showing OBS Pokemon HUD's properties](readme_files/screenshot_obspokemonhud.png?raw=true)

OBSPokemonHUD is a way to have your current Pokemon team showing up in OBS and allow them to be updated by a JSON file. The JSON file will let you manually edit it or (eventually) use an accomponying scripts to write them for you.

This project is based on an idea that [ShockSlayer](https://www.youtube.com/c/shockslayer "SS's YouTube Channel") [(his Twitch)](https://twitch.tv/shockslayer "SS's Twitch") came up with. Originally the project was named [SSPokemonHUD](https://github.com/guitaristtom/sspokemonhud), but that was janky mess between HTML, Python, and Javascript all being used in tandem. The idea was that it was a just a web site that you could use as a browser source and add to your scene, that way it didn't matter what broadcasting or recording software you were using.

There is also a [Team Editor](#team-editor) script that you can add to OBS's Scripts as well. That way you can manage your team without editing a JSON file directly, and from right within OBS itself.

## Premise
I have been wanting to redo this project from scratch for a couple years now, but between work and now school I haven't had a whole lot of time to do it.

## Install Instructions

### All
Follow the instructions below if you don't have Python installed already and working with OBS.

If you do, then all you should need to do is install the required [libraries](#libraries).

From there all you need to do is open up the Script dialog within OBS by going to `Tools` -> `Scripts`, and press the `+` button and add in `obspokemonhud.py` and (if you want) `team_editor.py`.

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
Within this repository there is a second Python file named `team_editor.py`. Add that in to your OBS's Scripts window. From there you can browse to your team.json file and edit it that way. Having it all self-contained within OBS.

![Screenshot of the OBS scripts window showing the team editor properties](readme_files/screenshot_team_editor.png?raw=true)

## Notes
* If you're on Linux, you'll have to create any additional cache folders that aren't a part of the repository (custom maps, etc.)

## Donating
Someone mentioned that I should put this here in case people feel like donating a little bit to me and my projects


[![shield.io](https://img.shields.io/badge/buymeacoffee-thomashine-yellow)](https://www.buymeacoffee.com/thomashine)
[![shield.io](https://img.shields.io/badge/ko--fi-thomashine-blue)](https://ko-fi.com/thomashine)
