class BaseEquipment:
    def __init__(self):
        self.plain = {
            "attack": 0,
            "magic": 0,
            "defense": 0,
            "magic_resistance": 0,
            "max_mana": 0
        }

        self.multi = {
            "attack": 0,
            "magic": 0,
            "defense": 0,
            "magic_resistance": 0,
            "max_mana": 0
        }

        self.baseplain = {
            "attack": 0,
            "magic": 0,
            "defense": 0,
            "magic_resistance": 0,
            "max_mana": 0
        }

        self.basemulti = {
            "attack": 0,
            "magic": 0,
            "defense": 0,
            "magic_resistance": 0,
            "max_mana": 0
        }

        self.level = 1
        self.xp = 0

    def update_level(self):
        PROGRESS = 1.2
        level = self.level - 1

        for stat in self.plain:
            self.plain[stat] = round(self.baseplain[stat] * PROGRESS ** level)
            self.multi[stat] = round(self.basemulti[stat] * PROGRESS ** level)
