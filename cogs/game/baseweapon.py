class BaseWeapon():
    def __init__(self):
        # To modify
        self.plain = {
            "attack" : 0,
            "magic" : 0,
            "defense" : 0,
            "magic_resistance" : 0,
            "max_mana" : 0
        }
        
        self.multi = {
            "attack" : 0,
            "magic" : 0,
            "defense" : 0,
            "magic_resistance" : 0,
            "max_mana" : 0
        }
        
        # To not modify
        self.baseplain = {
            "attack" : 0,
            "magic" : 0,
            "defense" : 0,
            "magic_resistance" : 0,
            "max_mana" : 0
        }
        
        self.basemulti = {
            "attack" : 0,
            "magic" : 0,
            "defense" : 0,
            "magic_resistance" : 0,
            "max_mana" : 0
        }
        
        
        self.level = 1
        self.xp = 0
        self.type = "weapon"
        
    def custom_attack(self):
        pass
    
    def update_level(self):
        PROGRESS = 1.2
        level = self.level -1
        
        self.plain["attack"] = round(self.baseplain["attack"] * PROGRESS ** level)
        self.plain["magic"] = round(self.baseplain["magic"] * PROGRESS ** level)
        self.plain["defense"] = round(self.baseplain["defense"] * PROGRESS ** level)
        self.plain["magic_resistance"] = round(self.baseplain["magic_resistance"] * PROGRESS ** level)
        self.plain["max_mana"] = round(self.baseplain["max_mana"] * PROGRESS ** level)
        
        
        self.multi["attack"] = round(self.basemulti["attack"] * PROGRESS ** level)
        self.multi["magic"] = round(self.basemulti["magic"] * PROGRESS ** level)
        self.multi["defense"] = round(self.basemulti["defense"] * PROGRESS ** level)
        self.multi["magic_resistance"] = round(self.basemulti["magic_resistance"] * PROGRESS ** level)
        self.multi["max_mana"] = round(self.basemulti["max_mana"] * PROGRESS ** level)