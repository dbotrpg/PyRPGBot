import random

import random

class Weapon:
    ### Requires a Name(str), damage(int), seed(list, which consists of 3 integers.)
    ## To keep it fair, the seed should NEVER contain items highter then 100.
    def __init__(self, name, damage, seed=None):
        self.name = name
        self.damage = damage
        self.seed = seed
        self.level = int
        self.hidden_level = int
        self.usable_at = int
        if self.seed == None:
            self.level = 255
            self.hidden_level = 255
            self.usable_at = 999
        elif not self.seed == None:
 #           print(seed)
            self.level = seed[0]
            self.hidden_level = seed[1]
            self.usable_at = seed[2]
        if self.level >= 10:
            print('Checkpoint 1 hit.')

            print(self.damage)
            if self.hidden_level >=20:
                print('checkpoint 2 hit.')
                dam_buf = self.hidden_level / random.randrange(10, 50)
                actdamage = self.damage * dam_buf
                self.damage = round(actdamage)
                print(self.damage)
            
        elif self.level <=9:
            self.damage = self.damage * 0.2

class class_base:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
    

class Player:
    def __init__(self, name, race, weapon, perks, class_base):
        self.name = name
        self.race = race
        self.perks = perks
        self.profession = class_base
        self.magicka = race.magicka
        self.max_health = race.health
        self.health = self.max_health
        self.base_attack = race.attack
        self.gold = 40
        self.pots = 0
        self.weapons = []
        self.curweapon = weapon
    
    @property
    def attack(self):
        attack = self.base_attack
        if not self.curweapon == None:
            attack += self.curweapon.damage
            return attack

class Enemy:
    def __init__(self, name, race, weapon, loot, is_boss=False):
        self.name = name
        self.race = race
        self.base_attack = race.attack
        self.level = random.randrange(1, 100)
        self.cur_weapon = weapon
        self.is_boss = is_boss
        self.loot = loot

        if self.is_boss == True:
            self.damage = self.damage * 2
            self.level = self.level * 2

    @property
    def attack(self):
        attack = self.base_attack
        if not self.cur_weapon == None:
            attack += self.cur_weapon.damage
            return attack

class Race:
    def __init__(self, name, attack, health, magicka):
        self.name = name
        self.attack = attack
        self.health = health
        self.magicka = magicka


        #Different races get different THINGS.
        if self.name == 'Human':
            self.attack += 10
            self.health += 100
            self.magicka += 10
        elif self.name == 'Dwarf':
            #Dwarfs are Bulky chunky people, so ofc they get a bit more health.
            self.attack += 10
            self.health += 150
            self.magicka += 5
        elif self.name == 'Elf':
            #naturally, elven characters are magically gifted, and less powerful.
            self.attack += 7
            self.health += 100
            self.magicka += 150
        elif self.name == 'Orc':
            #Bigger brutes then dwarves, tho magically weak, their increased health pool & strength make them a great choice.
            self.attack += 15
            self.health += 125
            self.magicka += 2

Annihilator = Weapon('The Annihilator', 100, [9000,9000,9000])
print(Annihilator.damage)
#print(Annihilator.seed[0])
class1 = class_base('Dick', ['Att1', 'att2'])
Main = Player('Glazey', Race('Orc', 100, 1000, 90000), Annihilator, ['aaa'], ['AAA'])
print('Player {0.name}\n of race {0.race.name} with a base attack of {0.base_attack}\n now has an attack of {0.curweapon.damage} because of weapon {0.curweapon.name}'.format(Main))
Woot = class_base('Testing', {'Wtf': 10, 'AAAAAA': 20})
print(Main.curweapon.damage)   