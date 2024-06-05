from cogs.game.basehero import BaseHero

class EnemyDummy(BaseHero):
    def __init__(self):
        self.name = "Dummy"
        self.level = 1
        self.max_hp = 40
        self.hp = self.max_hp
        self.attack = 2
        self.magic = 1
        self.defense = 7
        self.magic_resistance = 3
        self.max_mana = 100
        self.mana = self.max_mana