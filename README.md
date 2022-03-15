# Polar Scheduler
![thumbnail](https://github.com/zeke800/Polar-Scheduler/blob/main/promo.png?raw=true)
Polrschd ported (more like rewritten, recycling a few parts) to run on python 3.7 and below. It also has extra features like station alignment, dump location, etc. Basically, predicts all the GAC transmissions for POES satellites. Original reverse engineering done here: https://github.com/sgcderek/polrschd. **All dates and times are in UTC!**

## Port status
Everything is ported, except the orbital predictions. I am working on porting that. EDIT: Ephem gives some (very) wrong elevation numbers. After fighting with it, I have come to realize that the library Ephem hates me. I will soon post a **semi-working** code. I am not sure why Ephem says that all my pass degrees are negative... the main_BETA.py file also will contain a version that **does not** need an N2YO api key. If you have any idea WHY ephem does not work, please do not hesitate to reach out in the issues section on Github. 

# FAQ

## What is GAC?

GAC is a dump-like downlink on NOAA POES satellites. It contains data collected from nearly the entire orbit of a POES satellite.

## What do I need to receive it?

An SDR capable of running at more than 4 MSPS (I was able to get a lock at 4MSPS), as well as a rather large dish. I tried it on my 80cm dish and got a barely-decodable result, however I've seen people receive it (with a little noise) on 70cm dishes. But my setup isn't great, either. 100-260cm dishes work fine. EDIT: I **was** able to decode it! Turns out, NOAA dumps backwards at my location 🤔. 

# Install
## Prerequisites
An N2YO API key. Is currently needed, but isn't really used. Will be needed when I add support in the future.
## Install
### Linux
``` shell
git clone https://github.com/zeke800/Polar-Scheduler
cd Polar-Scheduler
nano secrets.py
```
Now, update your information in the editor! Then, CTRL+X and ENTER to close. Make sure to update the emojis as shown in the 'Known Errors' section. 
``` shell
python main.py
```
If you are using the main_BETA.py file, install pyephem!
``` shell
pip install pyephem
```
### Windows
Download the repository from github. Open secrets.py in Notepad or Python IDLE. Run the main file through Python IDLE or 
``` shell
python main.py
```
You should not need to change any ASCII characters. If you do, refer to the next section. 
## Known errors
``` python
SyntaxError: Non-ASCII character '\xe2' in file main.py on line 125, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```
### Systems
Raspberry Pi/Linux

### Fix
Change 
``` shell
emoji = "✅"
```
and 
``` shell
emoji = "❎"
```
to any text like 
``` shell
emoji = "Yes"
```
``` shell
emoji = "No"
```
### Potential Fix (coming soon)
Switch to emoji library for Python.
