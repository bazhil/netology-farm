class Animal():
    minweight = 1
    maxweight = 600
    food = 2
    product = []

    def __init__(self):
        self.minweight=minweight
        self.maxweight=maxweight
        self.food=food
        self.product=product

    def eat(self):
        return self.food

    def get_product(self):
        return self.product

    def get_name(self):
        pass

    def say(self):
        pass

class Cow(Animal):

    def __init__(self, name):
        self.name = name
        self.minweight=50
        self.maxweight=600
        self.product=['milk', 'meat']
        self.scream='Mooo'

    def eat(self):
        return food*20

    def say(self):
        return scream*3

Cow_1 = Cow('Vera')
Cow_2 = Cow('Lena')
Cow_3 = Cow('Vova')

class Goat(Animal):

    def __init__(self, name):
        self.name = name
        self.minweight=10
        self.maxweight=50
        self.product=['milk', 'meat', 'leather']
        self.scream='Beeeee'

    def eat(self):
        return food*2

    def say(self):
        return scream

    def leather_count(self):
        return (maxweigth-minweight)/4

Goat_1 = Goat('Vasya')
Goat_2 = Goat('Zorya')
Goat_3 = Goat('Mila')

class Sheep(Animal):

    def __init__(self, name):
        self.name = name
        self.minweight=10
        self.maxweight=50
        self.product=['meat', 'leather', 'wool']
        self.scream='Meeeee'

    def eat(self):
        return food * 2

    def say(self):
        return scream

Sheep_1 = Sheep('Fedya')

class Pig(Animal):

    def __init__(self, name):
        self.name = name
        self.minweight=30
        self.maxweight=150
        self.product=['meat', 'leather']
        self.scream='Hryu'

    def eat(self):
        return food * 10

    def say(self):
        return scream

    def leather_count(self):
        return (maxweigth - minweight) / 4

Pig_1 = Pig('Hryak')

class Chiken(Animal):

    def __init__(self):
        self.minweight=1
        self.maxweight=5
        self.product=['meat', 'eggs']
        self.scream='ko'

    def eat(self):
        return food/8

    def get_eggs(self):
        return 1

    def say(self):
        return scream*3

Chiken_1 = Chiken()

class Goose(Animal):


    def __init__(self):
        self.minweight=50
        self.maxweight=600
        self.product=['meat', 'eggs']
        self.scream='ga'

    def eat(self):
        return food / 5

    def get_eggs(self):
        return 1

    def say(self):
        return scream * 3

Goose_1 = Goose()

class Duck(Animal):
    minweight = 1
    maxweight = 10
    product = ['meat', 'eggs']
    scream = 'ga'

    def eat(self):
        return food / 5

    def get_eggs(self):
        return 1

    def say(self):
        return scream * 3

Duck_1 = Duck()

