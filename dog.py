class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("--dog initialized--")

# calling classes
my_dog = Dog("Doge", "Shiba Inu")
print(my_dog)
print(my_dog.name)