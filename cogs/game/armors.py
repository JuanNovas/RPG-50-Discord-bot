from cogs.game.basearmor import BaseArmor

# ID 1
class ArmorIron(BaseArmor):
    def __init__(self):
        super().__init__()
        
        self.plain["defense"] = 2
        self.plain["magic resistance"] = 3
        
        
armor_dict = {
    1 : ArmorIron
}