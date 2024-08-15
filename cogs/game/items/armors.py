from cogs.game.items.basearmor import BaseArmor 


class ArmorIron(BaseArmor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.plain["defense"] = 2
        self.plain["magic_resistance"] = 3
        self.update_level()
        
        self.id = 1
        self.rarity = 1
        self.name = "Iron"
        self.boosts = f'defense + {self.plain["defense"]} | magic resistance + {self.plain["magic_resistance"]}'
        
        
class ArmorScale(BaseArmor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.plain["magic"] = 2
        self.plain["magic_resistance"] = 5
        self.update_level()
        
        self.id = 2
        self.rarity = 4
        self.name = "Scale"
        self.boosts = f'magic + {self.plain["magic"]} | magic resistance + {self.plain["magic_resistance"]}'
        
        
class ArmorBearSkin(BaseArmor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.plain["defense"] = 4
        self.plain["attack"] = 1
        self.update_level()
        
        self.id = 3
        self.rarity = 4
        self.name = "Bear skin"
        self.boosts = f'defense + {self.plain["defense"]} | attack + {self.plain["attack"]}'
        
        
class ArmorStrawHelmet(BaseArmor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.plain["defense"] = 2
        self.plain["magic_resistance"] = 2
        self.update_level()
        
        self.id = 4
        self.rarity = 1
        self.name = "Straw helmet"
        self.boosts = f'defense + {self.plain["defense"]} | magic resistance + {self.plain["magic_resistance"]}'


armor_dict =  {
    1 : ArmorIron,
    2 : ArmorScale,
    3 : ArmorBearSkin,
    4 : ArmorStrawHelmet
}