from cogs.game.basehero import BaseHero

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
                
            message = f"{self.name} healed up to {self.hp} HP"
        else:
            return False
        
        return message