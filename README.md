# Polar Scheduler
![thumbnail](https://github.com/zeke800/Polar-Scheduler/blob/main/promo.png?raw=true)
Polrschd ported (more like rewritten, recycling a few parts) to run on python 3.7 and below. It also has extra features like station alignment, etc. Basically, predicts all the GAC transmissions for POES satellites. Slightly based on https://github.com/sgcderek/polrschd. All times and dates are in UTC! 

## Port status
Everything is ported, except the orbital predictions. I am working on porting that.

# FAQ

## What is GAC?

GAC is a dump-like downlink on NOAA POES satellites. It contains data collected from nearly the entire orbit of a POES satellite.

## What do I need to receive it?

An SDR capable of running at more than 5 MSPS (I was able to get a lock at 4MSPS), as well as a rather large dish. I tried it on my 80cm dish and got a barely-decodable result, however I've seen people receive it (with a little noise) on 70cm dishes. But my setup isn't great, either. 100-260cm dishes work fine.

# Install
## Prerequisites
An N2YO API key. Is currently needed, but isn't really used. Will be needed when I add support in the future.
## Install
``` shell
git clone https://github.com/zeke800/Polar-Scheduler
cd Polar-Scheduler
nano secrets.py
```
Now, update your information in the editor! Then, CTRL+X and ENTER to close. 
``` shell
python main.py
```
