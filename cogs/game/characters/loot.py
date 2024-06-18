from cogs.utils.database import execute
from cogs.utils.hero_actions import add_if_new


class Loot():
    def __init__(self, gold=0, wood=0, iron=0, runes=0, xp=0, equipment=None, drop_rate=0.1, level=1):
        self.gold = gold 
        self.wood = wood
        self.iron = iron
        self.runes = runes
        self.xp = round(xp * (1.07 ** level))
        self.equipment = equipment
        self.drop_rate = drop_rate
    
    def drop(self, user_id):
        # Get xp info
        data = execute('''
        SELECT level, xp FROM hero WHERE user_id=(?)
        ''', (user_id,))
        
        # Update xp and level
        xp_needed = round(6.5 * (1.5 ** data[0][0]))
        if xp_needed <= data[0][1] + self.xp:
            final_xp = data[0][1] + self.xp - xp_needed
            level_up = 1
        else:
            final_xp = data[0][1] + self.xp
            level_up = 0
        
        # Load resources data
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
        
        # Create message
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
            
        # If new equipment load it
        if self.equipment:
            equipment = equipment()
            if add_if_new(user_id, equipment):
                message += f"\n User has gained a new item {equipment.name}"
            
            
        return message