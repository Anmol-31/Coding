class student:
    pass

#s1,s2 are instance of a class i.e. object...
s1 = student()
s2 = student()

print(s1)
print(s2)

#name,rn,email are instance variable...
s1.name = 'Anmol'
s1.rn = 9
s1.email = 'anmolupadyay@gmail.com'
s1.age = 20

s2.name = 'Vishu'
s2.rn = 89
s2.email = 'vishu@gmail.com'

print(s1.name,s1.rn,s1.email,s1.age,sep = '\n')
print(s2.name,s2.rn,s2.email,s2.age,sep = '\n')
