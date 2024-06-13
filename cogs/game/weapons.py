from cogs.game.baseweapon import BaseWeapon

# ID 1
class WeaponKnife(BaseWeapon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.plain["attack"] = 4
        self.update_level()
        self.name = "Knife"
        
    def custom_attack(self, user, enemy):
        damage = 10
        enemy.hp -= damage
        
        message = f"dealt {damage} damage to {enemy.name}"
        return message
    

weapon_dict = {
    1 : WeaponKnife
}