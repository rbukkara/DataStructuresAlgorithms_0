"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telemarketers = set()
nonteles = set()

def addNumberToTeleMarketers(number):
    if len(item) > 0 and len(item[0]) > 0:
        if len(telemarketers) == 0:
            telemarketers.add(number)
        elif number not in telemarketers:
            telemarketers.add(number)

def addNumberToNonTeles(number):
    if len(nonteles) == 0:
        nonteles.add(number)
    elif number not in nonteles:
        nonteles.add(number)

for item in calls:
    addNumberToTeleMarketers(item[0])
    addNumberToNonTeles(item[1])

for item in texts:
    addNumberToNonTeles(item[0])
    addNumberToNonTeles(item[1])

possibletelemarketers = telemarketers.difference(nonteles)

print("These numbers could be telemarketers: ")
for num in sorted(possibletelemarketers):
    print(num)


