from cogs.game.items.baseweapon import BaseWeapon

class WeaponKnife(BaseWeapon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.plain["attack"] = 4
        self.update_level()
        self.name = "Knife"
        
        self.id = 1
        
    def custom_attack(self, user, enemy):
        damage = 10
        enemy.hp -= damage
        
        message = f"dealt {damage} damage to {enemy.name}"
        return message

weapon_dict = {
    1 : WeaponKnife
}