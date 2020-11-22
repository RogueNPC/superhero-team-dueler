class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def drink(self):
        print(f"{self.name} is drinking")

class Frog(Animal):
    def jump(self):
        print(f"{self.name} is jumping")


# class calls
if __name__ == "__main__":
    dog = Animal("Doge")
    dog.eat()
    dog.drink()
    frog = Frog("Kermit")
    frog.jump()
    frog.eat()
    frog.drink()