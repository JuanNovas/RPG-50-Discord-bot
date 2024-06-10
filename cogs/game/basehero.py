import random
from cogs.game.weapons import weapon_dict
from cogs.game.armors import armor_dict

class BaseHero():
    def __init__(self,level=1,hp=0,attack=0,magic=0,defense=0,magic_resistance=0,mana=0,weapon_id=None,armor_id=None):
        if weapon_id:
            self.equip(weapon_dict[weapon_id])
        else:
            self.weapon = None
        if armor_id:
            self.equip(armor_dict[armor_id])
        else:
            self.armor = None
        
        self.level = level 
        level = level - 1
        self.max_hp = round(hp * (1.15 ** level))
        self.hp = self.max_hp
        self.attack = round(attack * (1.15 ** level))
        self.magic = round(magic * (1.15 ** level))
        self.defense = round(defense * (1.15 ** level))
        self.magic_resistance = round(magic_resistance * (1.15 ** level))
        self.max_mana = round(mana * (1.15 ** level))
        self.mana = self.max_mana
        
        self.abilities = {"Hit" : self.do_attack}
        
    def do_attack(self, enemy, power=10):
        CRIT_CHANCE = 0.05
        crit = False
        
        damage = round((((self.attack**1.5) * power) / (self.attack + enemy.defense + 10)) * random.uniform(0.8, 1))
        if random.random() <= CRIT_CHANCE:
            damage *= 2
            crit = True
        enemy.hp -= damage
        
        if crit:
            message = f"dealt a critical hit dealing {damage} damage to {enemy.name}"
        else:
            message = f"dealt {damage} damage to {enemy.name}"
        return message
    
    def do_magic(self, enemy, power):
        damage = round((((self.magic**1.5) * power) / (self.magic + enemy.magic_resistance + 10)) * random.uniform(0.8, 1))
        enemy.hp -= damage
        
        message = f"dealt {damage} damage to {enemy.name}"
        return message
    
    def is_alive(self):
        return self.hp > 0
    
    def use_mana(self, amount):
        if self.mana >= amount:
            self.mana -= amount
            return True
        else:
            return False
            
    def use_health(self, amount):
        if self.hp > amount:
            self.hp -= amount
            return True
        else:
            return False
    
    def weapon_attack(self, enemy):
        if self.weapon:
            return self.weapon.custom_attack(self, enemy)
        else:
            return False
    
    def equip(self, equipment):
        self.attack += equipment.plain["attack"]
        self.magic += equipment.plain["magic"]
        self.defense += equipment.plain["defense"]
        self.magic_resistance += equipment.plain["magic_resistance"]
        self.max_mana += equipment.plain["max_mana"]
        
        
        self.attack *= (1 + equipment.multi["attack"])
        self.magic *= (1 + equipment.multi["magic"])
        self.defense *= (1 + equipment.multi["defense"])
        self.magic_resistance *= (1 + equipment.multi["magic_resistance"])
        self.max_mana *= (1 + equipment.multi["max_mana"])
        
        self.mana = self.max_mana
        
        if equipment.type == "weapon":
            self.weapon = equipment
            self.abilities["Weapon Attack"] = self.weapon_attack
        elif equipment.type == "armor":
            self.armor = equipment