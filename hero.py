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

    def is_alive(self):  
        # TODO: Check the current_health of the hero.
        # if it is <= 0, then return False. Otherwise, they still have health
        # and are therefore alive, so return True
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        # 1) else, start the fighting loop until a hero has won
        # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
        # 3) After each attack, check if either the hero (self) or the opponent is alive
        # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
        if self.abilities == [] or opponent.abilities == []:
            print("Draw, Both heroes have no abilities!")
        else:
            while self.is_alive() and opponent.is_alive():
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
            if not self.is_alive() and not opponent.is_alive():
                print("Draw, Both heroes are knocked out!")
            elif self.is_alive() and not opponent.is_alive():
                print(f"{self.name} won!")
            else:
                print(f"{opponent.name} won!")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 100)
    ability2 = Ability("Super Eyes", 30)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)