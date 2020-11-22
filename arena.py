from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        team_one = []
        team_two = []

    def create_ability(self):
        name = input("What is the ability name?  ")
        max_damage = input("What is the max damage of the ability?  ")

        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the weapon name?  ")
        max_damage = input("What is the max damage of the weapon?  ")

        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What is the armor name?  ")
        max_block = input("What is the max block of the armor?  ")

        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               #TODO add an ability to the hero
               #HINT: First create the ability, then add it to the hero
               hero.add_ability(self.create_ability())
           elif add_item == "2":
               #TODO add a weapon to the hero
               #HINT: First create the weapon, then add it to the hero
               hero.add_ability(self.create_weapon())
           elif add_item == "3":
               #TODO add an armor to the hero
               #HINT: First create the armor, then add it to the hero
               hero.add_armor(self.create_armor())
        return hero