from cogs.game.items.basearmor import BaseArmor 


class ArmorIron(BaseArmor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.plain["defense"] = 2
        self.plain["magic resistance"] = 3
        
        self.id = 1
        self.rarity = 1
        self.name = "iron"


armor_dict =  {
    1 : ArmorIron
}