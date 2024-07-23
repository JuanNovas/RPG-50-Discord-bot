from cogs.game.characters.basehero import BaseHero
from cogs.game.items.weapons import WeaponKnife
from cogs.game.items.armors import ArmorScale
from cogs.game.characters.loot import Loot
from cogs.utils.decorators import mana_ability

        
class EnemyDummy(BaseHero):
    def __init__(self, **kwargs):
        super().__init__(
            hp=40,
            attack=2,
            magic=1,
            defense=7,
            magic_resistance=3,
            mana=100,
            **kwargs
        )
        self.name = "Dummy"
        self.image = "https://cdn.discordapp.com/attachments/474702643625984021/1248370223644672050/tplImg448cf06ed22b4c25bee83fed318624bd.jpg?ex=6665651e&is=6664139e&hm=9c4481d293279c988d33a3aa998d8559d3f02635059da297b03a37b86353155f&"
        self.id = 1
        
        self.ability = {
            "name" : "test",
            "cost" : 10,
            "func" : self.special_attack
        }
        
        self.loot = Loot(
            gold=10,
            wood=2,
            xp=10,
            equipment = WeaponKnife,
            level=kwargs.get('level', 1)
        )
        
        
    
    @mana_ability(cost=10)
    def special_attack(self, enemy):
        return self.do_magic(enemy, 20)
    
        
class EnemySlime(BaseHero):
    def __init__(self, **kwargs):
        super().__init__(
           hp=20,
           attack=1,
           magic=3,
           defense=2,
           magic_resistance=2,
           mana=10,
           **kwargs
        )
        self.name = 'Slime'
        self.image = 'https://cdn.discordapp.com/attachments/474702643625984021/1248374929783521280/13712f15-7631-468d-a5cb-4d55d4cddfdc.jpeg?ex=66729880&is=66714700&hm=bb6b4be5d85aae3ed91c6728e488b1f0114acdf310217859fb34e29f3d39888e&'
        self.id = 2

        self.ability = {
            "name" : "Sticky shot",
            "cost" : 10,
            "func" : self.special_attack
        }
        
        self.loot = Loot(
           gold=1,
           wood=0,
           iron=0,
           runes=0,
           xp=4,
           equipment=None,
           level=kwargs.get('level', 1)
        )
        
        
    @mana_ability(cost=10)
    def special_attack(self, enemy):
        return self.do_magic(enemy, 30)
        
class EnemyLavaDragon(BaseHero):
    def __init__(self, **kwargs):
        super().__init__(
            hp=50,
            attack=5,
            magic=7,
            defense=4,
            magic_resistance=9,
            mana=50,
            **kwargs
        )
        self.name = 'LavaDragon'
        self.image = 'https://cdn.discordapp.com/attachments/474702643625984021/1255177713472508035/fire_dragon.jpeg?ex=667c2ed6&is=667add56&hm=c0d22dfa4d431f5bf6c93f14d1b6c125e82b7cb964638390605d4b6468135bb4&'
        self.id = 3

        self.ability = {
            "name" : "Infernal breath",
            "cost" : 25,
            "func" : self.special_attack
        }
        
        self.loot = Loot(
            gold=60,
            wood=5,
            iron=0,
            runes=0,
            xp=10,
            equipment=ArmorScale,
            drop_rate=0.05,
            level=kwargs.get('level', 1)
        )
        
         
    @mana_ability(cost=25)
    def special_attack(self, enemy):
        enemy.mana -= 10
        if enemy.mana < 0:
            enemy.mana = 0
        message = self.do_magic(enemy, 40)
        message += f"{enemy.name} loosed 10 mana"
        return message
        
class EnemySkeleton(BaseHero):
    def __init__(self, **kwargs):
        super().__init__(
            hp=30,
            attack=3,
            magic=1,
            defense=1,
            magic_resistance=2,
            mana=10,
            **kwargs
        )
        self.name = 'Skeleton'
        self.image = 'https://cdn.discordapp.com/attachments/474702643625984021/1256033175818473472/skeleton.jpeg?ex=667f4b8d&is=667dfa0d&hm=1f4f3dc7de924fb5ff26856001a5d51aa3a03256fdbe7e7adced7cc961f9f862&'
        self.id = 4

        self.ability = {
            "name" : "Bones picking",
            "cost" : 10,
            "func" : self.special_attack
        }
        
        self.loot = Loot(
            gold=1,
            wood=1,
            iron=0,
            runes=0,
            xp=2,
            equipment=None,
            level=kwargs.get('level', 1)
        )
        
        
    @mana_ability(cost=10)
    def special_attack(self, enemy):
        amount = self.magic * 5
        if self.hp + amount > self.max_hp:
            amount = self.max_hp - self.hp
            self.hp = self.max_hp
        else:
            self.hp += amount
        return f"{self.name} restored {amount} HP"
        
class EnemyGoblin(BaseHero):
    def __init__(self, **kwargs):
        super().__init__(
            hp=10,
            attack=4,
            magic=1,
            defense=2,
            magic_resistance=2,
            mana=10,
            **kwargs
        )
        self.name = 'Goblin'
        self.image = 'https://cdn.discordapp.com/attachments/474702643625984021/1265311340176736257/DALLE_2024-07-23_11.15.25_-_A_fantasy_RPG_style_image_of_a_goblin_in_a_fighting_stance_standing_in_a_medieval_training_field._The_goblin_has_green_skin_pointy_ears_and_is_wear.webp?ex=66a10c83&is=669fbb03&hm=070ea131dda78975751ae19bcd053eba7956e3963b522bc23578c6d3102ab960&'
        self.id = 5

        self.ability = {
            "name" : "Bite",
            "cost" : 10,
            "func" : self.special_attack
        }
        
        self.loot = Loot(
            gold=2,
            wood=0,
            iron=0,
            runes=0,
            xp=3,
            equipment=None,
            level=kwargs.get('level', 1)
        )
        
        
    @mana_ability(cost=10)
    def special_attack(self, enemy):
        return self.do_attack(enemy, power=20)
    
    
class EnemyCrow(BaseHero):
    def __init__(self, **kwargs):
        super().__init__(
            hp=15,
            attack=7,
            magic=1,
            defense=2,
            magic_resistance=2,
            mana=5,
            **kwargs
        )
        self.name = 'Crow'
        self.image = 'https://cdn.discordapp.com/attachments/474702643625984021/1265316305914036225/DALLE_2024-07-23_11.35.10_-_A_fantasy_RPG_style_image_of_a_crow_perched_on_a_wooden_post._The_crow_has_glossy_black_feathers_a_sharp_beak_and_piercing_eyes_with_a_semi-realist.webp?ex=66a11123&is=669fbfa3&hm=ee543d69c19e97c5912237c13172f333e19964edbc5ca7d50b09dfa93ac4171f&'
        self.id = 6
        
        self.ability = {
            "name" : "Scream",
            "cost" : 5,
            "func" : self.special_attack
        }

        self.loot = Loot(
            gold=1,
            wood=0,
            iron=0,
            runes=0,
            xp=2,
            equipment=None,
            level=kwargs.get('level', 1)
        )
        
        
    @mana_ability(cost=5)
    def special_attack(self, enemy):
        return self.do_attack(enemy, power=15)
        
        
enemy_dict = {
    1 : EnemyDummy,
    2 : EnemySlime,
    3 : EnemyLavaDragon,
    4 : EnemySkeleton,
    5 : EnemyGoblin,
    6 : EnemyCrow
}