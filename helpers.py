import os
def get_tle_lines(sat):
    tle = ""
    with open("noaa.txt",'r') as t:
        tle = t.read()
    tlelinesunformat = tle.splitlines()
    #tlelines = []
    tlelines = tlelinesunformat
    """
    for i in range(len(tlelinesunformat)):
        tlelines.append(tlelinesunformat[i].replace(" ", ""))
        i = i+3
        """
    print(tlelines)
    
    satindex = tlelines.index(sat)
    line1index = satindex+2
    line2index = satindex+4
    satname = tlelines[satindex]
    line1 = tlelines[line1index]
    line2 = tlelines[line2index]
    return satname,line1,line2
