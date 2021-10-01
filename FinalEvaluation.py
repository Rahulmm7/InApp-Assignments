class Pet():


    def _init_(self,species, name):
        self.name = name
        self.species = species


    def named(self,name):
        return bool(name)

    def _str_(self):
        if self.named() :
            print(f'Species of: {self.species}, named {self.name} ')
        else :
            print(f'Species of: {self.species}, unnamed ')


class Dog(Pet):
    def _init_(self, name,chases):
        super()._init_(name=name, species=Dog)

        self.chases = chases

    def named(self,name):
        return bool(name)

    def _str_(self):
        if self.named() :
            print(f'Species of: {self.species}, named {self.name}, chases {self.chases} ')
        else :
            print(f'Species of: {self.species}, unnamed, chases{self.chases} ')



class Cat(Pet):
    def _init_(self,name,hates):
        super()._init_(name=name, species=Cat)
        self.hates = hates

    def named(self,name):
        return bool(name)

    def _str_(self):
        if self.named() :
            print(f'Species of: {self.species}, named {self.name}, hates {self.hates} ')
        else :
            print(f'Species of: {self.species}, unnamed, hates{self.hates} ')




dict = {'dog': [],'Cat':[]}


def createDog():
    DogName = input("Enter Dog Name")
    DogSpecies = input("Enter the species")
    d = Dog(DogName, DogSpecies)
    dict[0] = d

def createCat():
    CatName = input("Enter Cat Name")
    CatSpecies = input("Enter the species")
    dict[1] = Cat(CatName, CatSpecies)



for i in range(5):
    createDog()

for i in range(3):
    createCat()
