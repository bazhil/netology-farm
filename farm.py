class Farm:
    eyes = 2
    meat = True


class Animal(Farm):
    legs = 4
    minweight = 30
    maxweight = 600


class Bird(Farm):
    legs = 2
    minweight = 1
    maxweight = 20


class Cow(Animal):
    minweight = 300
    maxweight = 600
    milk = True


class Got(Animal):
    minweight = 30
    maxweight = 60
    milk = True


class Sheep(Animal):
    minweight = 30
    maxweight = 60
    wool = True


class Pig(Animal):
    minweight = 50
    maxweight = 100


class Duck(Bird):
    minweight = 1
    maxweight = 10


class Chiken(Bird):
    minweight = 1
    maxweight = 7

def __init__(self, weight):
    self.weight=mimweight

Chiken_1=Chiken()
Chiken_2=Chiken()
Chiken_3=Chiken()

print(type(Chiken_1))
print(Chiken_2)
print(Chiken_3)

class Goose(Bird):
    minweight = 50
    maxweight = 20


Goose_1=Goose()
Goose_2=Goose()
Goose_3=Goose()

print(type(Goose_1))
print(Goose_2)
print(Goose_3)