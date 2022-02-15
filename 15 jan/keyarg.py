'''keyword(kwarg) arguments'''

# once you define a keyword argument next arg cannot be non keyword args
# order doesnt matter in keyword argument

def display(a,b=4,c='Hello WOrld'):
    print(a,b,c,sep='    ')

display(1000) #1 positional args
display(a=2000) #1 keyword args
display(a=5000,b=9000) #2 keyword args
display(a=6000,c='MDK') #2 keyword args
display(8,11,'mdk')#3 positional args
display(9,b='13')#1 pos 1 keyword
# display()#Nothing

# display(a=2000,5)
# display(8,a=2000)
# display(c=7)
display(c='mdk',b='88',a=8)
