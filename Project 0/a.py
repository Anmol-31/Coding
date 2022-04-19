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


#BinarySearch Code for searching each number under Incoming calls of Calls List
def binarysearch(arr,s):
    start,end,decision=0,len(arr)-1,0
    while start<=end:
        mid=(start+end)//2
        m=arr[mid]
        if s==m:
            decision=1
            break
        elif s<m:
            end=mid-1
        elif s>m:
            start=mid+1
    return decision

unique=set()
call=set()
tele=[]

#Adding first and second column of text file to unique set
for i in texts:
    unique.add(i[0])
    unique.add(i[1])


for i in calls:
    call.add(i[0])#Adding first column of calls file to "CALL" Set
    unique.add(i[1])#Adding second column of calls file

unique=list(unique)
call=list(call)

unique.sort()#Sorting unique list so that binary search can easily be implemented
call.sort()#Sorting call list so it helps to print in lexicographic order

#Checking for telemarketer number
for i in call:
    c=binarysearch(unique,i)
    if c==0:
        tele.append(i)

#Printing telemarketer numbers
print("These numbers could be telemarketers: ")
for i in tele:
    print(i)
