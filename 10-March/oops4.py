class car:
    def __init__(self,color,engine,passenger):
        self.color = color
        self.engine = engine
        self.passenger = passenger

    def name(self):
        carname = self.color[0] + self.engine[0] + str(self.passenger)
        print(carname)




s1 = car('red','zzz',8)
s2 = car('green','zz',4)
s3 = car('white','zzzz',6)

s1.name()
s2.name()
s3.name()


def x():
    pass
print(type(x))
