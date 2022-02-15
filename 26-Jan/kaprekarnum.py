'''''
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
def digit(n):
    x = 0
    y =n
    while(y != 0):
        x += 1
        y //= 10
    return x
def kaprekar(n):
    y = n*n
    b = digit(y)
    if(b%2 == 0):
        a = y//10**(b/2) + y%10**(b/2)
        if(n == a):
            return True
        else:
            return False
    else:
        for i in range (1,b+1):
            x = y//10**i + y%10**(b-i)
            if(n == x):
                return True
    return False
n =  int(input("Enter Number :- "))
a = kaprekar(n)
print(a)
