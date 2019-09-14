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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

bangaloreanNumbers = set()

def getCodeForNumber(number):

    if number.startswith('('):
        closeindex = number.index(')')
        return number[0:closeindex+1]

    if number[0:3] != "140":
        return number[0:4]

    return ""

def testgetCodeForNumber():
    # mobile
    assert getCodeForNumber('90366 69257') == '9036'
    # telemarketing
    assert getCodeForNumber('(080)62164823') == '(080)'
    # area code
    assert getCodeForNumber('1406669257') == ""

testgetCodeForNumber()

def numberIsBangalore(num):
    return num[0:5] == "(080)"

def testnumberIsBangalore():
    # mobile
    assert numberIsBangalore('90366 69257') == False
    # telemarketing
    assert numberIsBangalore('(080)62164823') == True
    # area code
    assert numberIsBangalore('1406669257') == False

    assert numberIsBangalore('08036 69257') == False

    assert numberIsBangalore('0806669257') == False

testnumberIsBangalore()

callstoBangalorecount = 0
callsfromBangalorecount = 0

for item in calls:
    if len(item) > 0 and len(item[0]) > 0:
        if numberIsBangalore(item[0]):
            callsfromBangalorecount += 1
            numCode = getCodeForNumber(item[1])
            if len(numCode) > 0:
                bangaloreanNumbers.add(numCode)
            if numberIsBangalore(item[1]):
                callstoBangalorecount += 1

print("The numbers called by people in Bangalore have codes:")

for num in sorted(bangaloreanNumbers):
    print(num)

callPercent = (callstoBangalorecount / callsfromBangalorecount) * 100

callPercent = callPercent
print("{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(callPercent))
