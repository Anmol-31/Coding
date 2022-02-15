a=[1,2,3,4,5]
b=a
c=[1,2,3,4,5]



print(f'The id of a is {id(a)}')
print(f'The id of b is {id(b)}')   # here list are mutable and list copied/created with assignment operator are stored at same memory location or both gets the tag on that memory location
print(f'The id of c is {id(c)}')   # but if we initialize the same list like we done with variable 'c' , here 'a' and 'c' will store in differnt memory location. this is because list are mutable

print('****************')
a[2]='anmol'
print(f'The id of a is {id(a)}')


print('--------------------------')
print('--------------------------')
print('--------------------------')
print('--------------------------')
print('--------------------------')

x='Anmol'
y='Anmol'
z=x

print(f'The id of x is {id(x)}') # here in case of string we initialize value of x,y and ceate value of z with assignmet of x with it
print(f'The id of y is {id(y)}') # when we check address of each variable with help of id() , we see x,y,z have same memory location or these variable have same tag of that specific memory location
print(f'The id of z is {id(z)}') # this is because strings are immutable

print('--------------------------')
print('--------------------------')
print('--------------------------')
print('--------------------------')
print('--------------------------')

p = 2   # int data type is mutable or immutable?
q = 2   # we can change value of int variable when we need to in that specific code? so is it mutable?
print(f'The id of p is {id(p)}') # if we go deeper Answer is noo because when we change value of that variable yes value changes but now stored in diff. memory location
print(f'The id of q is {id(q)}') # mutable means changing of value at a specific address
p = 5                            # as we see p,q have same value p when we run or check address we see both are the tag of number 2 or are stored at similar memory location
print(f'The id of p is {id(p)}')
print('--------------------------')
print('--------------------------')
print('--------------------------')
print('--------------------------')
print('--------------------------')
g=2
f=g
h=2
