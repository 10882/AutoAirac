import os
import datetime
#crosspatform

def check(MainFolder : str): 
    #takes path to main X-Plane folder
    #check if it exist
    os.chdir(MainFolder)
    try:
        os.chdir('Custom Data')
    except:
        return None
    main, expireDate = CheckMain()
    if expireDate < datetime.datetime.now():
        return False
    else:
        fmc = checkFmc()
        navdata = checkNavdata()
        if fmc == main and navdata == main:
            return True
        else:
            return False

def checkFmc() -> str:
    try:
        os.chdir('x-fmc navdata')
        fle = open('cycle_info.txt', 'r')
    except:
        return 0000
    cycle = fle.readline()
    fle.close()
    os.chdir('..')
    
    cycle = cycle[-5:-1]
    return cycle

def checkNavdata() -> str:
    try:
        os.chdir('navdata')
        fle = open('cycle_info.txt', 'r')
    except:
        return 0000
    cycle = fle.readline()
    fle.close()
    os.chdir('..')

    cycle = cycle[-5:-1]
    return cycle

def CheckMain():
    #get cycle number and expire date from main file
    #read
    try:
        fle = open('cycle_info.txt', 'r')
    except:
        return 0000, datetime.datetime.strptime('01/May/1900', '%d/%b/%Y')
    cycle = fle.readline()
    eversion = fle.readline()
    expire = fle.readline()
    fle.close()
    #take things that we need
    cycle = cycle[-5:-1]
    expire = expire[-12:-1]
    #make date date
    expireDate = datetime.datetime.strptime(expire, '%d/%b/%Y')

    return cycle, expireDate