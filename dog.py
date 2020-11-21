class Dog:
    # instance properties
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("--dog initialized--")

    # class methods
    def bark(self):
        print("Woof!")

    def sit(self):
        print(f"{self.name} sits")
    
    def roll_over(self):
        print(f"{self.name} rolls over")