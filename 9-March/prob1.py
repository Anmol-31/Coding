def pow1(a,b):
    while(b != 1):
        return(pow1(a,b-1)*pow1(a,1))
    return a

x = int(input('Enter the Number:-'))
y = int(input('Enter the Power :-' ))
print(pow1(x,y))
