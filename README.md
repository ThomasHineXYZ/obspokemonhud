OBSPokemonHUD
------------

OBSPokemonHUD is a way to have your current Pokemon team showing up in OBS and allow them to be updated by a JSON file. The JSON file will let you manually edit it or (eventually) use an accomponying scripts to write them for you.

This project is based on an idea that [ShockSlayer](https://www.youtube.com/c/shockslayer "SS's YouTube Channel") [(his Twitch)](https://twitch.tv/shockslayer "SS's Twitch") came up with. Originally the project was named [SSPokemonHUD](https://github.com/guitaristtom/sspokemonhud), but that was janky mess between HTML, Python, and Javascript all being used in tandem. The idea was that it was a just a web site that you could use as a browser source and add to your scene, that way it didn't matter what broadcasting or recording software you were using.

## Premise
I have been wanting to redo this project from scratch for a couple years now, but between work and now school I haven't had a whole lot of time to do it.

## Install Instructions
### Windows
You will need to have a version of Python 3.6 installed, as that's what OBS currently supports. Right now that is [Python 3.6.12](https://www.python.org/downloads/release/python-3612/). Make sure you install the 64-bit version or it won't load up correctly and give an error similar to this in the log:

```
13:54:17.152: LoadLibrary failed for 'C:/Users/Thomas/AppData/Local/Programs/Python/Python36-32/python36.dll': %1 is not a valid Win32 application.
13:54:17.152:  (193)
13:54:17.152: [Python] Could not load library: C:/Users/Thomas/AppData/Local/Programs/Python/Python36-32/python36.dll
```

### Linux
All you should need is the `obs-studio` and `python` packages installed and setup on your distribution. If that isn't working, start up an [issue](issues/) and let me know what you had to do and I'll add notes for it here.

### Mac...
I'm not sure, I don't have a Mac machine or VM to test this on. If someone would like to start an [issue](issues/) and give me instructions for how to install and set up OBS and Python, that would be appreciated.

## Notes
* If you're on Linux, you'll have to create any additional cache folders that aren't a part of the repository (custom maps, etc.)

## To Do:
* Variants (Alolan, Galarian)
* Nickname
* Ball
* Level
* A lot...?
