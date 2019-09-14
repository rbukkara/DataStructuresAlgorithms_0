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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def addtelephonenumber(chosenlist):
    """
    :type chosenlist: list
    """
    if len(chosenlist) == 0:
        return

    for item in chosenlist:
        if not len(item) == 0:
            addNumber(item[0])
            addNumber(item[1])

def addNumber(number):
    if number != "":
        uniquenumbers.add(number)


uniquenumbers = set()

addtelephonenumber(texts)

addtelephonenumber(calls)

print("There are {0} different telephone numbers in the records.".format(len(uniquenumbers)))

