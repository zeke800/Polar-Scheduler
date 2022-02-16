def return_params():
    #########PARAMETERS START#######
    yourLat = 46.444   # Your latitude
    yourLon = 60.444   # Your longitude
    yourAlt = 500           # Your altitude (meters above sea level)
    N2YO_api_key = "YOUR-API-KEY"      # Your N2YO API key
    minElevation = -2      # Minimum elevation of the GAC event (can be negative)
    liveNear = ['SVL'] #SVL = Svaalbard, FBK = Fairbanks, WAL = Wallops (allows multiple definitions like ['FBK','SVL'])
    #########PARAMETERS END#########
    return yourLat,yourLon,yourAlt,N2YO_api_key,liveNear

