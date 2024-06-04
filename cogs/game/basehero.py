import random

class BaseHero():
    def __init__(self,level=1,hp=0,attack=0,magic=0,defense=0,magic_resistance=0,mana=0):
        self.level = level
        self.base_hp = hp
        self.base_attack = attack
        self.base_magic = magic
        self.base_defense = defense
        self.base_magic_resistance = magic_resistance
        self.base_mana = mana
        
        
        self.hp = self.base_hp
        self.attack = self.base_attack
        self.magic = self.base_magic
        self.defense = self.base_defense
        self.magic_resistance = self.base_magic_resistance
        self.max_mana = self.base_mana
        self.mana = self.base_mana
        
    def do_attack(self, enemy, power=10):
        CRIT_CHANCE = 0.05
        crit = False
        
        damage = round((((self.attack**1.5) * power) / (self.attack + enemy.defense + 10)) * random.uniform(0.8, 1))
        if random.random() >= CRIT_CHANCE:
            damage *= 2
            crit = True
        enemy.hp -= damage
        
        if crit:
            message = f"{self.name} dealt a critical hit dealing {damage} damage to {enemy.name}"
        else:
            message = f"{self.name} dealt {damage} damage to {enemy.name}"
        return message
    
    def is_alive(self):
        return self.hp > 0
    
    def weapon_attack(self):
        pass
    
    def equip(self, weapon):
        self.attack += weapon.plain["attack"]
        self.magic += weapon.plain["magic"]
        self.defense += weapon.plain["defense"]
        self.magic_resistance += weapon.plain["magic_resistance"]
        self.max_mana += weapon.plain["max_mana"]
        
        
        self.attack *= (1 + weapon.multi["attack"])
        self.magic *= (1 + weapon.multi["magic"])
        self.defense *= (1 + weapon.multi["defense"])
        self.magic_resistance *= (1 + weapon.multi["magic_resistance"])
        self.max_mana *= (1 + weapon.multi["max_mana"])
        
        self.mana = self.max_mana
        
        self.weapon_attack = weapon.custom_attack