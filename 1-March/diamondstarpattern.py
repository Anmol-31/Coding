n = int(input("Enter an integer n :-"))
if(n % 2 == 0):
    for i in range(n//2):
        print((i+1) * "*")
    for i in range(n//2,n):
        print((n-i) * "*")
else:
    for i in range((n+1)//2):
        print((i+1) * "*")
    for i in range((n+1)//2,n):
        print((n-i) * "*")
