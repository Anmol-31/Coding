n = int(input("Enter The Number --> "))
new_n=0
while (n != 0):
    new_n = new_n*10 + n%10
    n //= 10
print(new_n)
print(float('inf'))
