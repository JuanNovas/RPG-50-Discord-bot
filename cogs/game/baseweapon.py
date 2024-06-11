from cogs.game.baseequipment import BaseEquipment

class BaseWeapon(BaseEquipment):
    def __init__(self):
        super().__init__()
        self.type = "weapon"
    
    def custom_attack(self):
        pass




