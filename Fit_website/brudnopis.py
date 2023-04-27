class NamePet():
    def __init__(self, name):
        self.name = name

    def test(self):
        pass

class Dog(NamePet):
    def get_dog(self):
        return "Hał"
class Cat(NamePet):
    def get_cat(self):
        return "Miał"


class FactoryPet:
    def get_all(self, type_pet, name):
        if type_pet == "dog":
            return Dog(name)
        elif type_pet == "cat":
            return Cat(name)
        else:
            print(":(")


factory = FactoryPet()

dog = factory.get_all("dog", "Lucky")
print(dog.get_dog())

cat = factory.get_all("cat", "Leon")
print(cat.get_cat())