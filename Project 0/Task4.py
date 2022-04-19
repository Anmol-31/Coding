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
b = set()
c = set()
for i in range(len(calls)):
    a = calls[i][0]
    for j in range(len(calls)):
        if a == calls[j][1]:
            break
    else:
        b.add(a)
b = list(b)
for i in range(len(b)):
    a = b[i]
    for j in range(len(texts)):
        if a == texts[j][1] or a == texts[j][0]:
            break
    else:
        c.add(a)
print("These numbers could be telemarketers: ")
c = list(c)
c.sort()
for i in c:
    print(i)
