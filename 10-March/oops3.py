'''
class car hogi
usmai uake object ke characterstics
color,engine,no. of passangr
baad mai message print krna hai -->
car ka naam krna hai color ka phla letter
engine ka phla letter
last letter is
3 objext
8,4,6
'''
class car:
    def __init__(self,color,engine,passenger):
        self.color = color
        self.engine = engine
        self.passenger = passenger



s1 = car('red','zzz',8)
s2 = car('green','zz',4)
s3 = car('white','zzzz',6)

s1.name = s1.color[0] + s1.engine[0] + str(s1.passenger)
print(s1.name)

s2.name = s2.color[0] + s2.engine[0] + str(s2.passenger)
print(s1.name)

s3.name = s3.color[0] + s3.engine[0] + str(s3.passenger)
print(s3.name)
