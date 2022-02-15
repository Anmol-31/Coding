'''
* _ _ _ _ _ _ _ *
* * _ _ _ _ _ * *
* * * _ _ _ * * *
* * * * _ * * * *
* * * * * * * * *

mcall uthaa
'''
n = int(input("Enter Height :- "))
for i in range (1,n+1):
#     for j in range (1,n+1):
#         if(i >= j):
#             print(end="*")
#     for k in range (2*n-i-1,0,-1):
#         if(i >= k):
#             print(end="*")
#         else:
#             print(end=" ")
#     print("")
    if(i == n):
        print("*"*(2*n-1))
    else:
        print("*"*i + " "*((2*n)-1-(2*i)) + "*"*i)
