from cogs.game.characters.basehero import BaseHero
from cogs.utils.decorators import mana_ability, health_ability
    
# ID 1
class MagicDummy(BaseHero):
    def __init__(self, **kwargs):
        super().__init__(
            hp=20,
            attack=3,
            magic=7,
            defense=3,
            magic_resistance=4,
            mana=20,
            **kwargs
        )
        self.name = "User"
        self.classname = "Wizard"
        self.image = "https://cdn.discordapp.com/attachments/474702643625984021/1249850968577933393/magicdummy2.jpeg?ex=6668cdec&is=66677c6c&hm=0d946dc04407fcc92df9ac02dada07f8090ef839b0a29b70958bd065a6b105e8&"
        
        level = kwargs.get('level', 1)
        
        self.abilities["Magic flame"] = self.magic_flame
        
        if level >= 10:
            self.abilities["Heal"] = self.heal
            
            
    @mana_ability(cost=5)
    def magic_flame(self, enemy):
        return self.do_magic(enemy, 10)
    
    @mana_ability(cost=10)
    def heal(self, enemy):
        amount = self.magic * 2
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        return f"{self.name} healed {amount} HP"
    
# ID 2
class AssasinDummy(BaseHero):
    def __init__(self, **kwargs):
        super().__init__(
            hp=25,
            attack=5,
            magic=2,
            defense=4,
            magic_resistance=5,
            mana=10,
            **kwargs
        )
        self.name = "User"
        self.classname = "Assasin"
        self.image = "https://cdn.discordapp.com/attachments/474702643625984021/1249850320217964704/assasindummy2.jpeg?ex=6668cd51&is=66677bd1&hm=bdd64f0f8281af7d9bf29c6dd5c8ec879809a5296a5d122a0ee7d26972ed8e7e&"
        
        level = kwargs.get('level', 1)
        
        self.abilities["Super hit"] = self.super_hit
        
        if level >= 10:
            self.abilities["Sacrifice"] = self.sacrifice
        
    @mana_ability(cost=5)
    def super_hit(self, enemy):
        return self.do_attack(enemy, 20)
    
    @health_ability(cost=10)
    def sacrifice(self, enemy):
        return self.do_attack(enemy, 35)
    
    
# ID 3
class Tank(BaseHero):
    def __init__(self, **kwargs):
        super().__init__(
            hp=30,
            attack=3,
            magic=1,
            defense=6,
            magic_resistance=6,
            mana=10,
            **kwargs
        )
        self.name = "User"
        self.classname = "Tank"
        self.image = "https://cdn.discordapp.com/attachments/474702643625984021/1271109367076229170/DALLE_2024-08-08_11.14.42_-_A_fantasy_RPG_style_image_of_a_Tank_class_hero_in_a_medieval_training_field._The_hero_has_a_semi-realistic_appearance_with_heavy_armor_a_large_shield.webp?ex=66b62459&is=66b4d2d9&hm=13c260f3ff409466d40a100757753af705e8f615e330499ba18469eb50373f0c&"
        
        level = kwargs.get('level', 1)
        
        self.abilities["Smash"] = self.smash
        
        if level >= 10:
            self.abilities["Reforce"] = self.reforce
            
            
    @mana_ability(cost=10)
    def smash(self, enemy):
        return self.do_attack(enemy, 20)
    
    @mana_ability(cost=10)
    def reforce(self, enemy):
        self.defense += self.magic
        self.magic_resistance += self.magic
        return f"{self.name} incresed its defense and magic resistance in {self.magic} points"