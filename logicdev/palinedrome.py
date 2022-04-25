def palinedrome(n):
    y = n
    x = 0
    while(y != 0):
        x *= 10
        x += y%10
        y //= 10
    return x


a = int(input("Enter The Number:- "))
b = palinedrome(a)
if a == b:
    print(f"{a} is Palinedrome Number")
else:
    print(f"{a} is not a Palinedrome Number")            
