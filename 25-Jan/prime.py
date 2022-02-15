for i in range(1,10**2 +1):
    if i == 1:
        pass
    elif(i == 2):
        print(i)
    else:
        for j in range(2,i):
            if(i % j == 0):#checking prime or not
                break
                
            if(i == j+1):
                print(i)
