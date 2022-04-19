'''
Tuple Packing

'''

a=1
b=2
c=3


x=1,2,3
print(x,len(x),type(x))

'''
sequence unpacking
'''
p,q,r=x
print(p,q,r)


w=[5,6,7]
l,m,n=w
print(l,m,n,w)

'''
combination of tuple packing and sequence unpacking
'''
# d = 1,2,3
# e,f,g = d
e,f,g=1,2,3
print(e,f,g)


'''starred expression'''
j = [1,2,3,4,5,6,7,8]
*start,rest=j
print(start,rest)

h,*i,k,o =j
print(h,i,k,o,sep="\n")



'''Underscore(_)'''


u = ['anmol','mdk','sdk','vishu']
v,y,_,t = u
print(v,y,_,t,type(v))
