def x(s,l,a=1,b=0):
    if b < len(s):
        c = s[b:a+b]
        if len(c) != a:
            return x(s,l,a,b+1)
        else:
            l.append(c)
            return x(s,l,a,b+1)
    elif(a <= len(s)):
        return x(s,l,a+1,b=0)
    else:
        for i in l:
            print (i)
        return l
def count1(x,k,s):
    vowel = ['A','E','I','O','U']
    if len(x) == 0:
        return 1
    elif x[0][0] in vowel:
        k.append(x[0])
    else:
        s.append(x[0])
    x.pop(0)
    return count1(x,k,s)
def minion_game(string):

    k = []
    s = []
    l = []
    count1(x(string,l),k,s)
    if len(k) > len(s):
        print(f'Kevin {len(k)}')
    elif len(k) == len(s):
        print("Draw")
    else:
        print(f'Stuart {len(s)}')


a = input("enter:-")
minion_game(a)
print()
