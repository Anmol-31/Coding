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
a =set()
c = []
for i in range(0,len(calls)):
    for j in range(0,2):
        a.add(calls[i][j])
b = list(a)
b.sort()
for k in range(len(b)):
    c.append(0)
    for i in range(0,len(calls)):
        for j in range(0,2):
            if b[k] == calls[i][j]:
                c[k] += int(calls[i][3])
d = c.copy()
d.sort(reverse=True)

print(f"{b[c.index(d[0])]} spent the longest time, {d[0]} seconds, on the phone during September 2016.")




'''
3+3+8+8+8=30
'''
