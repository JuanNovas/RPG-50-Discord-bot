from cogs.game.basehero import BaseHero
from cogs.utils.database import execute

class Loot():
    def __init__(self, gold=0, wood=0, iron=0, runes=0, xp=0):
        self.gold = gold
        self.wood = wood
        self.iron = iron
        self.runes = runes
        self.xp = xp
    
    def drop(self, user_id):
        data = execute('''
        SELECT level, xp FROM hero WHERE user_id=(?)
        ''', (user_id,))
        
        xp_needed = round(6.5 * (1.5 ** data[0][0]))
        if xp_needed <= data[0][1] + self.xp:
            final_xp = data[0][1] + self.xp - xp_needed
            level_up = 1
        else:
            final_xp = data[0][1] + self.xp
            level_up = 0
        
        execute('''
        UPDATE hero SET
        level = level + (?),
        xp = (?),
        gold = gold + (?),
        wood = wood + (?),
        iron = iron + (?),
        runes = runes + (?)
        WHERE user_id = (?)
        ''', (level_up, int(final_xp), self.gold, self.wood, self.iron, self.runes, user_id))
        
        message = "Dropped"
        if self.gold > 0:
            message = message + f" {self.gold} gold"
        if self.wood > 0:
            message = message + f" {self.wood} wood"
        if self.iron > 0:
            message = message + f" {self.iron} iron"
        if self.runes > 0:
            message = message + f" {self.runes} runes"
        message = message + f"\nAnd User gained {self.xp} XP"
        if level_up:
            message += "\n User level up"
        return message
        
        

class EnemyDummy(BaseHero):
    def __init__(self):
        self.name = "Dummy"
        self.level = 1
        self.max_hp = 40
        self.hp = self.max_hp
        self.attack = 2
        self.magic = 1
        self.defense = 7
        self.magic_resistance = 3
        self.max_mana = 100
        self.mana = self.max_mana
        self.image = "https://cdn.discordapp.com/attachments/474702643625984021/1248370223644672050/tplImg448cf06ed22b4c25bee83fed318624bd.jpg?ex=6665651e&is=6664139e&hm=9c4481d293279c988d33a3aa998d8559d3f02635059da297b03a37b86353155f&"
        
        self.loot = Loot(
            gold=10,
            wood=2,
            xp=10
        )
        
