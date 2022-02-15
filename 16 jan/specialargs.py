'''
This was the new edition in Python 3.8


Syntax :-

def f(pos1,pos2,/,pos or kwd, *, kwd1,kwd2):

    function body


'''

def disp(arg):
    print(arg)

def disp1(arg,/):
    print(arg)

def disp2(*,arg):
    print(arg)

def disp3(arg1,/,arg2,*arg3):
    print(arg1,arg2,arg3)


disp(2) # 2
disp(arg=2) # 2

disp1(3)  # 3
# disp1(arg=3) # error

# disp2(4) # error
disp2(arg=4) # 4

disp3(arg1=2,arg2=3,arg4=5) # error
