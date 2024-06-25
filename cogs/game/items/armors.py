from cogs.game.items.basearmor import BaseArmor 


class ArmorIron(BaseArmor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.plain["defense"] = 2
        self.plain["magic_resistance"] = 3
        
        self.id = 1
        self.rarity = 1
        self.name = "iron"
        
        
class ArmorScale(BaseArmor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.plain["magic"] = 2
        self.plain["magic_resistance"] = 5
        
        self.id = 2
        self.rarity = 5
        self.name = "scale"


armor_dict =  {
    1 : ArmorIron,
    2 : ArmorScale
}