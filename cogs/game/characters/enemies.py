from cogs.game.characters.basehero import BaseHero
from cogs.game.items.weapons import WeaponKnife
from cogs.game.items.armors import ArmorScale
from cogs.game.characters.loot import Loot

        
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
        
        self.loot = Loot(
            gold=10,
            wood=2,
            xp=10,
            equipment = WeaponKnife,
            level=kwargs.get('level', 1)
        )
        
        
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

        self.loot = Loot(
           gold=1,
           wood=0,
           iron=0,
           runes=0,
           xp=4,
           equipment=None,
           level=kwargs.get('level', 1)
        )
        
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
        
        
enemy_dict = {
    1 : EnemyDummy,
    2 : EnemySlime,
    3 : EnemyLavaDragon
}