from cogs.game.basearmor import BaseArmor

class ArmorIron(BaseArmor):
    def __init__(self):
        super().__init__()
        
        self.plain["defense"] = 2
        self.plain["magic resistance"] = 3