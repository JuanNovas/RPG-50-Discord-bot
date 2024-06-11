from cogs.game.basehero import BaseHero
from cogs.utils.decorators import mana_ability, health_ability

class UserDummy(BaseHero):
    def __init__(self):
        self.name = "Good Dummy"
        self.level = 1
        self.max_hp = 80
        self.hp = self.max_hp
        self.attack = 5
        self.magic = 1
        self.defense = 6
        self.magic_resistance = 3
        self.max_mana = 100
        self.mana = self.max_mana
        
    def heal(self, *args):
        COST = 10
        HP_HEAL = 10
        
        if self.mana >= COST:
            self.mana -= COST
            self.hp += HP_HEAL
            if self.hp > self.max_hp:
                self.hp = self.max_hp
        
            message = f"healed up to {self.hp} HP"
        else:
            return False
        
        return message
    
# ID 1
class MagicDummy(BaseHero):
    def __init__(self, level=1, weapon_id=None, armor_id=None):
        super().__init__(
            weapon_id=weapon_id,
            armor_id=armor_id,
            level=level,
            hp=20,
            attack=3,
            magic=7,
            defense=3,
            magic_resistance=4,
            mana=20
        )
        self.name = "User"
        self.classname = "MagicDummy"
        self.image = "https://cdn.discordapp.com/attachments/474702643625984021/1249850968577933393/magicdummy2.jpeg?ex=6668cdec&is=66677c6c&hm=0d946dc04407fcc92df9ac02dada07f8090ef839b0a29b70958bd065a6b105e8&"
        self.abilities["Magic flame"] = self.magic_flame
        
    @mana_ability(cost=15)
    def magic_flame(self, enemy):
        return self.do_magic(enemy, 15)
    
# ID 2
class AssasinDummy(BaseHero):
    def __init__(self, level=1, weapon_id=None, armor_id=None):
        super().__init__(
            weapon_id=weapon_id,
            armor_id=armor_id,
            level=level,
            hp=30,
            attack=5,
            magic=2,
            defense=4,
            magic_resistance=5,
            mana=10
        )
        self.name = "User"
        self.classname = "AssasinDummy"
        self.image = "https://cdn.discordapp.com/attachments/474702643625984021/1249850320217964704/assasindummy2.jpeg?ex=6668cd51&is=66677bd1&hm=bdd64f0f8281af7d9bf29c6dd5c8ec879809a5296a5d122a0ee7d26972ed8e7e&"
        self.abilities["Super hit"] = self.super_hit
        self.abilities["Sacrifice"] = self.sacrifice
        
    @mana_ability(cost=5)
    def super_hit(self, enemy):
        return self.do_attack(enemy, 20)
    
    @health_ability(cost=10)
    def sacrifice(self, enemy):
        return self.do_attack(enemy, 35)