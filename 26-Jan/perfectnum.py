def perfect(n):
    x = 0
    for j in range(1,i):
        if(i % j == 0):
            x = x + j
        else:
            pass
    if(x == i):
        print(x)

for i in range(1,10**3):
    perfect(i)            

'''
A Kaprekar number is a number whose square when divided into two parts and such that sum of parts is equal to the original number and none of the parts has value 0. (Source : Wiki)
Given a number, the task is to check if it is Kaprekar number or not.

Input :  n = 45
Output : Yes
Explanation : 45^2 = 2025 and 20 + 25 is 45

Input : n = 13
Output : No
Explanation : 13^2 = 169. Neither 16 + 9 nor 1 + 69 is equal to 13

Input  : n = 297
Output : Yes
Explanation:  297^2 = 88209 and 88 + 209 is 297

i will be back in 20, do this till then
'''
