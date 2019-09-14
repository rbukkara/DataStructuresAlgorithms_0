"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

phoneTime = dict()

def updateCallInfo(number, calltime):
    if number in phoneTime:
        phoneTime[number] += int(calltime)
    else:
        if number != "":
            phoneTime[number] = int(calltime)

if len(calls) == 0:
    print("no data")

for item in calls:
    if not len(item) == 0:
        updateCallInfo(item[0], item[3])
        updateCallInfo(item[1], item[3])

maxtime = 0
maxnumber = ''

for phone, calltime in phoneTime.items():
    if calltime > maxtime:
        maxnumber, maxtime = phone, calltime

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(maxnumber, maxtime))


