from cogs.game.baseequipment import BaseEquipment

class BaseArmor(BaseEquipment):
    def __init__(self):
        super().__init__()
        self.type = "armor"
