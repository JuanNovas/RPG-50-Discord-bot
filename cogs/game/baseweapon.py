class BaseWeapon():
    def __init__(self):
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
        
    def custom_attack(self):
        pass