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
            print(seed)
            self.level = seed[0]
            self.hidden_level = seed[1]
            self.usable_at = seed[2]
        if self.level >= 10:
            if self.hidden_level >=20:
                dam_buf = self.hidden_level / random.randrange(10, 50)
                self.damage = self.damage * dam_buf
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

        if self.name == 'Human':
            self.attack += 10
            self.health += 100
            self.magicka += 10
        elif self.name == 'Dwarf':
            self.attack += 10
            self.health += 150
            self.magicka += 5

#print(Race('Dwarf', 10, 100, 10).name)
#print(Race('Dwarf', 10, 100, 10).attack)
#print(Race('Dwarf', 10, 100, 10).health)
#print(Race('Dwarf', 10, 100, 10).magicka)

Main = Player('Glazey', Race('Dwarf', 10, 100, 10), Weapon('The Annihilator', 2000), ['AAA'], ['AAA'])
#print('Player {0.name}\n of race {0.race.name} with a base attack of {0.base_attack}\n now has an attack of {0.race.attack} because of weapon {0.curweapon.name}'.format(Main))
Woot = class_base('Testing', {'Wtf': 10, 'AAAAAA': 20})
