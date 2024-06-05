from cogs.game.basehero import BaseHero

class Loot():
    def __init__(self, gold=0, wood=0, iron=0, runes=0):
        self.gold = gold
        self.wood = wood
        self.iron = iron
        self.runes = runes
        
    def drop(self):
        message = "Dropped"
        if self.gold > 0:
            message = message + f" {self.gold} gold"
        if self.wood > 0:
            message = message + f" {self.wood} wood"
        if self.iron > 0:
            message = message + f" {self.iron} iron"
        if self.runes > 0:
            message = message + f" {self.runes} runes"
            
        return message

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
        
        self.loot = Loot(
            gold=10,
            wood=2
        )
        
