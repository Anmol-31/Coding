# a = 'anmolupadhyay'
# print(a[1:8])
# #nmolupa
# print(a[1:])
# #nmolupadhyay
# print(a[:7])
# #anmolup
# print(a[:-1])
# #anmolupadhya
# print(a[-1])
# #y
# print(a[-1:])
# #y
# print(a[-12:])
# #nmolupadyay
# print(a[1:12:-1])
# #empty string
# print(a[1:12:1])
# #nmolupadhya
# print(a[12:1:-1])
# #yayhdapulom
#
# '''
# If start index < stop index
#     then check if step is negative:
#                 answer :- Empty String
#     else check if step is positive:
#                 answer :- Usual
#
# '''
# print(a[:])
# #anmolupadhyay
# print(a[::])
# #anmolupadhyay
# print(a[::1])
# #anmolupadhyay
# print(a[::2])
# #amlpdyy
# print(a[::-1])
# #yayhdapulomna
#
# b =[1,2,3,4,5]
# print(b[0:3:0.5])
# # Error step can't be negative

x=[6,2,3,4,5,6,7,8]
print(x[100:-1:-1]) #-1 represents end element therefore there won't be anything between end element and end element hence its an empty list
print(x[8:1:-1])   #all eleme
print(x[7:1:-1])   #8 7 6 5 4 3
print(x[7:0:-1])   #8 7 6 5 4 3 2
