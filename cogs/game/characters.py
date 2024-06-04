from cogs.game.basehero import BaseHero

class UserDummy(BaseHero):
    def __init__(self):
        self.name = "Good Dummy"
        self.level = 1
        self.max_hp = 100
        self.hp = self.max_hp
        self.attack = 20
        self.magic = 1
        self.defense = 10
        self.magic_resistance = 3
        self.max_mana = 100
        self.mana = self.max_mana
        
    def heal(self):
        COST = 10
        HP_HEAL = 10
        if self.mana >= COST:
            self.mana -= COST
            self.hp += HP_HEAL
            if self.hp > self.max_hp:
                self.hp = self.max_hp
                
            return True
        else:
            return False