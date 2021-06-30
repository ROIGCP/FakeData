#!/usr/bin/env python3

from numpy import random
from faker import Faker
import datetime as datetime

fake = Faker()
Faker.seed(random.randint(1000))

def getdatetimestamp(subtract = 0):
    currentdate = datetime.datetime.now()
    returndate = currentdate - datetime.timedelta(days=subtract)
    returnstring = returndate.strftime("%Y%m%d%H%m%S%f")
    return returnstring

def getdatestamp(subtract = 0):
    currentdate = datetime.datetime.now()
    returndate = currentdate - datetime.timedelta(days=subtract)
    returnstring = returndate.strftime("%Y%m%d")
    return returnstring

def gettimestamp():
    currenttime = datetime.datetime.now().strftime("%H%m%S%f")
    return currenttime

def gettimestring(hr, min, sec):
    timestring = str(hr).zfill(2) + str(min).zfill(2) + str(sec).zfill(2) + str(random.randint(0, 999999)).zfill(6)
    return timestring

def getamount(minamount = 0,maxamount = 1000):
    amount = random.randint(minamount,maxamount*100)/100
    return str(amount)

def getacctnum():
    acctnum = fake.iban()
    return str(acctnum)

def getname():
    name = fake.name()
    return name

def getip():
    ip = fake.ipv4_public()
    return ip

def getneptunerow():
    row = getdatetimestamp()
    return row

def createaccounts(totalaccounts = 1000, seed = 99):
    Faker.seed(seed)
    outname = "accounts.json"
    outfile = open(outname,"w") 
    outfile.write("[")
    for account in range(totalaccounts):
        account = {}
        account.update({'name':getname()})
        account.update({'account':getacctnum()})
        account.update({'ip':getip()})
        outfile.write(str(account)+",\n")
    outfile.write("]")
    outfile.close  
    return "Done"

if __name__ == "__main__":
    print(getdatetimestamp())
    print(getdatetimestamp(1))
    print(getdatestamp())
    print(getdatestamp(1))
    print(gettimestamp())
    print(gettimestring(1,1,1))
    print(getamount())
    print(getamount(1,5))
    print(getacctnum())
    print(getname())
    print(getip())
    print(createaccounts(5000))
