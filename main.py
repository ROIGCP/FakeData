#!/usr/bin/env python3
from numpy import random
from datetime import datetime
import math
import fakes


def getNULL():
    row = "NULL,NULL,NULL,0,NULL"
    return row

def getNOOP():
    row = "NOOP,NOOP,NOOP,0,NOOP"
    return row

def getBALANCE():
    row = "BALANCE," + fakes.getacctnum() + ",NULL,0," + fakes.getname()
    return row

def getDEPOSIT():
    row = "DEPOSIT," + fakes.getacctnum() + ",NULL," + fakes.getamount() + "," + fakes.getname()
    return row

def getWITHDRAWAL():
    row = "WITHDRAWAL," + fakes.getacctnum() + ",NULL,-" + fakes.getamount() + "," + fakes.getname()
    return row

def getSCHEDULE():
    row = "SCHEDULE," + fakes.getacctnum() + "," + fakes.getacctnum() + "," + fakes.getamount() + "," + fakes.getname()
    return row

def getTRANSFER():
    row = "TRANSFER," + fakes.getacctnum() + "," + fakes.getacctnum() + "," + fakes.getamount() + "," + fakes.getname()
    return row

def getactivity():
    activities = {
    0: getNULL,
    1: getNOOP,
    2: getBALANCE,
    3: getDEPOSIT,
    4: getWITHDRAWAL,
    5: getSCHEDULE,
    6: getTRANSFER
    }
    activity = activities.get(random.randint(len(activities)))
    row = activity()
    return row

def getrow():
    row = fakes.getdatetimestamp() + "," + fakes.getip() + "," + getactivity()
    return row

def getrownotimestamp():
    row = fakes.getip() + "," + getactivity()
    return row

def createfile(outname,filedate,maxentries):
    outfile = open(outname,"w") 
    gap = math.ceil(60*60*24*3 / maxentries )
    entry = 0
    ms = 0
    second = 0
    minute = 0
    hour = 0
    while entry < maxentries: 
        entry += 1 
        second = second + random.randint(0,gap)
        if second > 59:
                second = random.randint(0,gap)
                minute += 1
        if minute > 59:
                minute = 0
                hour +=1
        if hour > 23:
            break
        messagedata = filedate + fakes.gettimestring(hour,minute,second) + "," + getrownotimestamp() + "\n"
        outfile.write(messagedata)
        outfile.close  
    return (outname + " Entries: " + str(entry))

def removefile(fullfilename):
    import os
    if os.path.exists(fullfilename):
        os.remove(fullfilename)
        returnvalue = "File removed: " + fullfilename
    else:
        returnvalue = "File not found:" + fullfilename
    return returnvalue

def createsamples(days = 1, maxentries = 50000):
    results = ""
    path = ""
    basefile = "sample"
    for day in range(1,days+1):
        datename = fakes.getdatestamp(day)
        filename = basefile + datename + ".csv"
        fullfilename = path + filename
        print(createfile(fullfilename,datename,maxentries))
        print(removefile(fullfilename))
    return results
        
def createproduction(days = 1, maxentries = 250000):
    results = ""
    path = ""
    basefile = "production"
    for day in range(1,days+1):
        datename = fakes.getdatestamp(day)
        filename = basefile + datename + ".csv"
        fullfilename = path + filename
        print(createfile(fullfilename,datename,maxentries))
        print(removefile(fullfilename))
    return results

if __name__ == "__main__":
    print(getNULL())
    print(getNOOP())
    print(getBALANCE())
    print(getDEPOSIT())
    print(getWITHDRAWAL())
    print(getSCHEDULE())
    print(getTRANSFER())
    print(getrow())
    sample = int(input("Enter Number of Sample Files (-1 for none):"))
    print(createsamples(sample,50000))
    production = int(input("Enter Number of Production Files (-1 for none):"))
    print(createproduction(production,250000))

