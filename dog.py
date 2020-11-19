class Dog:
    def __init__(self, name):
        self.name = name
        print("--dog initialized--")

# calling classes
my_dog = Dog("Doge")
print(my_dog)
print(my_dog.name)