from cogs.game.baseequipment import BaseEquipment

class BaseWeapon(BaseEquipment):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = "weapon"
    
    def custom_attack(self):
        pass




