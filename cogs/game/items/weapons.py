from cogs.game.items.baseweapon import BaseWeapon
from cogs.utils.decorators import weapon_mana_ability, weapon_health_ability

class WeaponKnife(BaseWeapon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.plain["attack"] = 4
        self.update_level()
        
        self.id = 1
        self.rarity = 1
        self.name = "Knife"
        self.boosts = f'attack +{self.plain["attack"]}'
        self.attack_description = "**Stabs with a knife dealing 10 damage**\nCOST: 0"
        
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

        self.id = 2
        self.rarity = 3
        self.name = "Crossbow"
        self.boosts = f'attack + {self.plain["attack"]} | max mana + {self.plain["max_mana"]}'
        self.attack_description = "**Shoots an arrow**\nPOWER: 25\nCOST: 10"

    @weapon_mana_ability(cost=10)
    def custom_attack(self, user, enemy):
        return user.do_attack(enemy, power=25)
    

class WeaponPan(BaseWeapon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.plain["defense"] = 3
        self.plain["magic_resistance"] = 2
        self.update_level()

        self.id = 3
        self.rarity = 2
        self.name = "Pan"
        self.boosts = f'defense + {self.plain["defense"]} | magic resistance + {self.plain["magic_resistance"]}'
        self.attack_description = "**Reduces enemy mana by 10**\nCOST: 10"

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

        self.id = 4
        self.rarity = 4
        self.name = "Medkit"
        self.boosts = f'magic resistance + {self.multi["magic_resistance"]}%'
        self.attack_description = "**Heals 10% of HP**\nCOST: 15"

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

        self.id = 5
        self.rarity = 5
        self.name = "Relic"
        self.boosts = f'attack + {self.plain["attack"]} | magic + {self.plain["magic"]} | magic resistance + {self.plain["magic_resistance"]}'
        self.attack_description =  "**Deals damage with magic**\nPOWER: 30\nCOST: 25% HP"

    @weapon_health_ability(cost=25)
    def custom_attack(self, user, enemy):
        return user.do_magic(enemy, power=30)
    
    
class WeaponGloves(BaseWeapon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.plain["defense"] = 1
        self.update_level()

        self.id = 6
        self.rarity = 1
        self.name = "Gloves"
        self.boosts = f'defense + {self.plain["defense"]}'
        self.attack_description =  "**Punches the enemy 2 times**\nPOWER: 5*2\nCOST: 5"

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

        self.id = 7
        self.rarity = 4
        self.name = "Spear"
        self.boosts = f'attack + {self.plain["attack"]} | attack + {self.multi["attack"]}%'
        self.attack_description =  "**Throwes a spear**\nPOWER: 20\nCOST: 15% HP"

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
