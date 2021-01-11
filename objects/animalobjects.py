# animalobjects.py
# practice object oriented programming
# in the context of animals

class Animal():
    # constructor
    def __init__(self):
        self.name = "Unnamed"
        self.legs = 0
        #print("I'm in the constructor")

    # method
    def talk(self):
        if self.name != "Unnamed":
            print(f"Hello, my name is {self.name}!")
        else:
            print("Hello")

# creating an animal object
some_animal = Animal()
# access properties
print(some_animal.name)
some_animal.name = "Rex"
some_animal.legs = 2
print(some_animal.name)

# TODO: create a new object with a name and 20 legs. Print out its name and legs.

new_animal = Animal()
new_animal.name = "Bud"
new_animal.legs = 4
print(f"{new_animal.name}\n{new_animal.legs}")

print(type(new_animal))
new_animal.talk()