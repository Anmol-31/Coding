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
a =set()
for i in range(0,len(texts)):
    for j in range(0,2):
        a.add(texts[i][j])
for i in range(0,len(calls)):
    for j in range(0,2):
        a.add(calls[i][j])
print(f"There are {len(a)} different telephone number in the records")
