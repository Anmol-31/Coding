n = int(input("Enter half height greater than egual to 3:- "))
for i in range(n):
    print("*" + " "*i + "*")

for i in range(n,0,-1):
    print("*" + " "*(i-1) + "*")
