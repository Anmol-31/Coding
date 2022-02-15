def fun(num):
    if num < 1:
        return 0
    elif num % 2 == 0:
        return fun(num-1)
    else:
        return num+fun(num-2)    
print(fun(8))
