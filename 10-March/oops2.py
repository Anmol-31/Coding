class student:
    def __init__(self,name,rn,email):#dunder/magic method
        self.name = name
        self.rn = rn
        self.email = email


s1 = student('anmol',8,'anmol@gmail.com')
s2 = student('vishu',89,'vishu@gmail.com')

print(s1.name)
print(s2.name)
