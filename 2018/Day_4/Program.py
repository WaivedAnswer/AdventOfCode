import Common
import datetime
import collections
import operator

def part1(input):
    twoCount = 0
    prev_gid = None
    logs = {}
    for line in input:
        clean = Common.sub(line)
        values = clean.split()
        year = int(values[0])
        month = int(values[1])
        day = int(values[2])
        hour = int(values[3])
        minutes = int(values[4])
        date = datetime.datetime(year, month, day)
        if(hour == 23):
            date = date + datetime.timedelta(days = 1)
        if(date not in logs):
            logs[date] = [None,{}]
        if(len(values) == 6):
            logs[date][0] = int(values[5])
        fullDate = datetime.datetime(year,month,day,hour,minutes)
        if line.count("wakes"):
            print("wakes" + line)
            logs[date][1][fullDate] = False
        elif line.count("falls"):
            print("falls" + line)
            logs[date][1][fullDate] = True
        else: # begins
            print("begins" + line)
            logs[date][1][fullDate] = False
    
    sleepCounts = {}
    sleepers = {}
    sleepMinutes = {}
    for date, guardLog in logs.items():
        gid = guardLog[0]
        #if(gid == None):
        #    gid = logs[date - datetime.timedelta(days = 1)][0]
        minutes = guardLog[1]
        sleepTime = None
        for fullDate, value in collections.OrderedDict(sorted(minutes.items())).items():
            if(value == True):
                sleepTime = fullDate
            elif(not sleepTime == None):
                if(gid not in sleepCounts):
                    sleepCounts[gid] = 0
                sleepCounts[gid] = sleepCounts[gid] + ((fullDate - sleepTime).seconds/60)
                if(gid not in sleepMinutes):
                    sleepMinutes[gid] = {}
                startMinute = sleepTime.minute
                endMinute = fullDate.minute
                minRange = range(startMinute,endMinute)
                if(endMinute < startMinute):
                    minRange = range(endMinute, 60).extend(range(0, startMinute))
                    print(minRange)
                for minute in range(startMinute, endMinute):
                    if(minute not in sleepMinutes[gid]):
                        sleepMinutes[gid][minute] = 0
                    sleepMinutes[gid][minute] = sleepMinutes[gid][minute] + 1
                sleepTime = None
            else:
                sleepTime = None
                continue
                
    maxId = max(sleepCounts.items(), key=operator.itemgetter(1))[0]
    print(maxId) 
    maxMin = max(sleepMinutes[maxId].items(), key=operator.itemgetter(1))[0]
    
    print(maxMin)
    print(maxId * maxMin)
    
    maxGuard = None
    maxCount = 0
    maxMinute = None
    for gid, minutes in sleepMinutes.items():
        print(gid, minutes)
        maxMin = max(minutes.items(), key=operator.itemgetter(1))
        if(maxMin[1] > maxCount):
            maxGuard = gid
            maxCount = maxMin[1]
            maxMinute = maxMin[0]
    print(sleepMinutes[maxGuard])
    print(maxGuard, maxMinute)
    print(maxGuard * maxMinute)
    #guard = 3137
    """if line.count("wakes"):
        if(gid not in sleepCounts):
            sleepCounts[gid] = 0
        if(gid not in sleepers):
            continue
        sleepCounts[gid] = sleepCounts[gid] + minutes - sleepers[gid]
        sleepers.clear()
    elif line.count("falls"):
        sleepers[gid] = [minutes]
    else: # beings
        onDuty = gid"""
    
            
input = Common.inputAsLines()
#input = Common.inputAsString()

part1(input)
#part2(input)




