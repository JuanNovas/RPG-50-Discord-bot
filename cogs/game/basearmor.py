from cogs.game.baseequipment import BaseEquipment

class BaseArmor(BaseEquipment):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = "armor"
    
