import random
from ability import Ability
from armor import Armor

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = []
        self.armors = []

    def add_ability(self, ability):
        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def attack(self):
        # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage

    def add_armor(self, armor):
        # We use the append method to add armor objects to our list.
        self.armors.append(armor)

    def defend(self, damage_amt):
        # start our total out at 0
        total_block = 0
        # loop through all of our hero's abilities
        for armor in self.armors:
            # add the damage of each attack to our running total
            total_block += armor.block()
        # return the total damage
        return total_block

    def take_damage(self, damage):
        # TODO: Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        defense = self.defend(damage)
        damage -= defense
        self.current_health -= damage

    def fight(self, opponent):
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        # 1) randomly choose winner,
        # Hint: Look into random library, more specifically the choice method
        fighters = [self.name, opponent.name]
        print(f"{random.choice(fighters)} won!")

    def is_alive(self):  
        # TODO: Check the current_health of the hero.
        # if it is <= 0, then return False. Otherwise, they still have health
        # and are therefore alive, so return True
        if self.current_health <= 0:
            return False
        else:
            return True


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # armor = Armor("Debugging Shield", 10)
    # another_armor = Armor("Great Firewall", 50)
    my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)
    # my_hero.add_ability(ability)
    # my_hero.add_ability(another_ability)
    # print(my_hero.attack())
    # my_hero.add_armor(armor)
    # my_hero.add_armor(another_armor)
    # my_hero.take_damage(50)
    # print(my_hero.current_health)
    # print(my_hero.defend(10))
    # my_villan = Hero("Firebrand")
    # my_hero.fight(my_villan)
    my_hero.take_damage(150)
    print(my_hero.is_alive())
    my_hero.take_damage(15000)
    print(my_hero.is_alive())