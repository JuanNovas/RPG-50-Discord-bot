from cogs.game.baseweapon import BaseWeapon

class WeaponKnife(BaseWeapon):
    def __init__(self):
        super().__init__()
        
        self.plain["attack"] = 4
        
    def custom_attack(self, user, enemy):
        damage = 10
        enemy.hp -= damage
        
        message = f"{user.name} dealt {damage} damage to {enemy.name}"
        return message