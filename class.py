class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic animal sound"

    def move(self):
        return "Moves in some way"

    def get_name(self):
        return self.name


class Mammal(Animal):
    def __init__(self, name, has_fur=True):
        super().__init__(name)
        self.has_fur = has_fur

    def give_birth(self):
        return "Gives birth to live young"


class Dog(Mammal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Barks"

    def get_breed(self):
        return self.breed


# Kuriame šunų klasės objektą
my_dog = Dog("Buddy", "Golden Retriever")

# Informacijos apie objektą rodymas
print(my_dog.get_name())    # Buddy
print(my_dog.get_breed())   # Golden Retriever
print(my_dog.speak())       # Barks
print(my_dog.give_birth())  # Gives birth to live young
print(my_dog.move())        # Moves in some way