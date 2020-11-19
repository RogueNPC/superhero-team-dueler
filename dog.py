class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("--dog initialized--")

    def bark(self):
        print("Woof!")

# calling classes
my_dog = Dog("Doge", "Shiba Inu")
# print(my_dog.name)
# print(my_dog.breed)
my_dog.bark()