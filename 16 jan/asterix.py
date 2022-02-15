'''
Single Asterix Double Asterix

** - is used in formal parameters for receiving dictionaries only
* - is used to take multiple arguments

Single asterix ALWAYS come before Double Asterix

There can't be a positional argument after single double asterix

they come after all the args'\

'''

def disp(a,*b,**c):
    print(a,b)

    print(c)
    


disp(2,43,2,222,333,44,eng=80,math=80,chem=80)
