#Note: Polar Scheduler version 0.3.1
import secrets
#########PARAMETERS START#######
yourLat,yourLon,yourAlt,N2YO_api_key,liveNear = secrets.return_params()  # Enter your parameters in secrets.py!
minElevation = -2      # Minimum elevation of the GAC event (can be negative) NOT USED
#########PARAMETERS END#########
import time
from datetime import datetime
import random
import requests
import json
def is_between(time, time_range): #Thanks https://stackoverflow.com/questions/45265044/how-to-check-a-time-is-between-two-times-in-python!
    if time_range[1] < time_range[0]:
        return time >= time_range[0] or time <= time_range[1]
    return time_range[0] <= time <= time_range[1]
def random_wait():
    words = ["Waiting...","Throwing into volcano...","3D printing new feed...","Receiving GOES...","Installing feed mount...","Waiting for AOS...","Starting primary demodulator...","Hanging map...","Bargaining for a new dish with neighbor..."]
    return random.choice(words)

scheduleURL = "https://noaasis.noaa.gov/cemscs/polrschd.txt" #URL for GAC schedule
n2yo_url = "https://api.n2yo.com/rest/v1/satellite/radiopasses/"
#tleURL = "https://celestrak.com/NORAD/elements/noaa.txt" #SOOO much faster than the default TLE server :)
print("Calculating GAC events. Observer parameters: \n")
print(" Location: Lat "+str(yourLat)+", Long "+str(yourLon)+", Alt: "+str(yourAlt))
#print(" Minimum Satellite Elevation is set to "+str(minElevation))
def n2yo_request_url(norad_id,days):
    sep = "/"
    ret_url = n2yo_url+str(norad_id)+sep+str(yourLat)+sep+str(yourLon)+sep+str(yourAlt)+sep+str(days)+sep+str(minElevation)+"&apiKey="+N2YO_api_key
    return ret_url

print("[LOG] Grabbing data from N2YO...")

psnoaa19 = requests.get(n2yo_request_url(33591,7)) #NOAA 19, schedule is for 7 days only
psnoaa18 = requests.get(n2yo_request_url(28654,7)) #NOAA 18
psnoaa15 = requests.get(n2yo_request_url(25338,7)) #NOAA 15


print("[LOG] Communiated with N2YO server, computing orbits...")
noaa19rawpass = json.loads(psnoaa19.text)
noaa19elev = noaa19rawpass['passes'][0]['maxEl']
noaa18rawpass = json.loads(psnoaa18.text)
noaa18elev = noaa18rawpass['passes'][0]['maxEl']
noaa15rawpass = json.loads(psnoaa15.text)
noaa15elev = noaa15rawpass['passes'][0]['maxEl']
print("[LOG] Next passes for NOAA satellites (not necessarily with GAC)")
print("NOAA 19 elevation "+str(noaa19elev))
print("NOAA 18 elevation "+str(noaa18elev))
print("NOAA 15 elevation "+str(noaa15elev))
print("[LOG] Parsing elevations for passes...")
passamountnoaa19 = noaa19rawpass['info']['passescount']
passamountnoaa18 = noaa18rawpass['info']['passescount']
passamountnoaa15 = noaa15rawpass['info']['passescount']
print("[LOG]"+" "+str(passamountnoaa19)+" passes for NOAA 19 within the week.")
print("[LOG]"+" "+str(passamountnoaa18)+" passes for NOAA 18 within the week.")
print("[LOG]"+" "+str(passamountnoaa15)+" passes for NOAA 15 within the week.")

print("Now to the fun stuff! Downloading schedule...")
reqschedule = requests.get(scheduleURL)
schedule = str(reqschedule.text).splitlines()
for i in range(len(schedule)):
    line = schedule[i]
    date = line[0:17] # get date from line
    dateParsed = datetime.strptime(date, '%Y/%j/%H:%M:%S') 
    satID = line[23:25] # get satellite number from line
    station = line[26:29] #The official receiving station
    if (satID == "01"):
        satIDParsed = "MetOp-B"
    elif (satID == "02"):
            satIDParsed = "MetOp-A"
    elif (satID == "03"):
            satIDParsed = "MetOp-C"
    elif (satID == "15"):
            satIDParsed = "NOAA-15"
            #satellite = noaa15
    elif (satID == "18"):
            satIDParsed = "NOAA-18"
            #satellite = noaa18
    elif (satID == "19"):
            satIDParsed = "NOAA-19"
            #satellite = noaa19
    else:
            satIDParsed = satID
            
    if (station == "WAL"): #Handle station information. Currently very WIP. In this case, Wallops Island.
        stationParsed = "Wallops Command and Data Acquisition Station"
    elif (station == "FBK"):
            stationParsed = "Fairbanks Command and Data Acquisition Station"
    elif (station == "SVL"):
            stationParsed = "Svaalbard"
    elif (station == "MON"):
            stationParsed = "Montrey, California"
            
    elif (station == "MIA"):
            stationParsed = "Miami, Florida"
    else:
            stationParsed = "Unknown station"
            
    # Determine frequency from transmitter ID	
    if "LSB" in line:
            txFreq = "1698.0 MHz RHCP"
    elif "MSB" in line:
            txFreq = "1702.5 MHz LHCP"
    elif "HSB" in line:
            txFreq = "1707.0 MHz RHCP"
    elif "ESB" in line:
            txFreq = "2247.5 MHz RHCP"
    else:
            txFreq = "Unknown Frequency"
                            
    # Determine type of event	
    if "PBK,START,GAC" in line:
            eventType = "Start of GAC transmission"
    elif "PBK,END,GAC" in line:
            eventType = "End of GAC transmission  "
    else:
            eventType = "other"
    

    if ((eventType == "Start of GAC transmission") or (eventType == "End of GAC transmission  ")):
        emoji = ""
        trials = 0
        gotit = False
        for i in range(len(liveNear)): #We don't know how many stations the user lives close to!
            trials = trials + 1
            if station == liveNear[i]:
                emoji = "✅"
                gotit = True
            else:
                pass
        if trials == len(liveNear) and gotit == False:
            emoji = "❎"
        print(dateParsed, satIDParsed, eventType, txFreq, stationParsed, emoji)
                        
                    
                                

