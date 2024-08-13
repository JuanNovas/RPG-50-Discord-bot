from cogs.game.items.baseweapon import BaseWeapon
from cogs.utils.decorators import weapon_mana_ability, weapon_health_ability

class WeaponKnife(BaseWeapon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.plain["attack"] = 4
        self.update_level()
        self.name = "Knife"
        
        self.id = 1
        self.rarity = 1
        
    def custom_attack(self, user, enemy):
        damage = 10
        enemy.hp -= damage
        
        message = f"dealt {damage} damage to {enemy.name}"
        return message


class WeaponCrossbow(BaseWeapon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.plain["attack"] = 2
        self.plain["max_mana"] = 10
        self.update_level()
        self.name = "crossbow"

        self.id = 2
        self.rarity = 3

    @weapon_mana_ability(cost=10)
    def custom_attack(self, user, enemy):
        return user.do_attack(enemy, power=25)
    

class WeaponPan(BaseWeapon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.plain["defense"] = 3
        self.plain["magic_resistance"] = 2
        self.update_level()
        self.name = "pan"

        self.id = 3
        self.rarity = 2

    def custom_attack(self, user, enemy):
        enemy.mana -= 10
        if enemy.mana < 0:
            enemy.mana = 0
        return f"reduced {enemy.name} mana in 10"
    
    
class WeaponMedkit(BaseWeapon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.multi["magic_resistance"] = 0.01
        self.update_level()
        self.name = "medkit"

        self.id = 4
        self.rarity = 4

    @weapon_mana_ability(cost=15)
    def custom_attack(self, user, enemy):
        user.hp += user.max_hp / 10
        if user.hp > user.max_hp:
            user.hp = user.max_hp
        return f"was cured to {user.hp} of hp"
    
    
class WeaponRelic(BaseWeapon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.plain["attack"] = 1
        self.plain["magic"] = 4
        self.plain["magic_resistance"] = 2
        self.update_level()
        self.name = "relic"

        self.id = 5
        self.rarity = 5

    @weapon_health_ability(cost=25)
    def custom_attack(self, user, enemy):
        return user.do_magic(enemy, power=30)
    
    
class WeaponGloves(BaseWeapon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.plain["defense"] = 1
        self.update_level()
        self.name = "gloves"

        self.id = 6
        self.rarity = 1

    @weapon_mana_ability(cost=5)
    def custom_attack(self, user, enemy):
        message = user.do_attack(enemy, power=5)
        message += "\nand " + user.do_attack(enemy, power=5)
        return message + "\n whit a double attack"
    
class WeaponSpear(BaseWeapon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.plain["attack"] = 2
        self.multi["attack"] = 0.01
        self.update_level()
        self.name = "spear"

        self.id = 7
        self.rarity = 4

    @weapon_health_ability(cost=15)
    def custom_attack(self, user, enemy):
        return user.do_attack(enemy, power=20)

weapon_dict = {
    1 : WeaponKnife,
    2 : WeaponCrossbow,
    3 : WeaponPan,
    4 : WeaponMedkit,
    5 : WeaponRelic,
    6 : WeaponGloves,
    7 : WeaponSpear
}
