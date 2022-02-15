def otp(n):
    n1 = ''
    for i in range(len(n)):
        if(int(n[i])%2 == 0):
            pass
        else:
            n1 += str(int(n[i])**2)
    return n1



n = input("enter the number :- ")
print(otp(n))
