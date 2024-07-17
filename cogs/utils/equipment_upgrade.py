from cogs.utils.database import execute, execute_dict
from cogs.utils.progress import add_upgrade

def equipment_upgrade_cost(level : int, rarity : int) -> tuple:
    if not (0 <= level <= 49 and level < rarity * 10):
        return False
    
    # Gold
    gold_cost = level * (100 * ((level // 10) + 1))
    
    # Wood
    wood_cost = 10 + level ** 2 * 2
    
    # Iron
    iron_cost = round(level + 5 ** (0.1 * level))
    
    # Runes
    if rarity >= 4:
        match level:
            case 24:
                rune_cost = 1
            case 29:
                rune_cost = 4
            case 34:
                rune_cost = 6
            case 39:
                rune_cost = 12
            case 44:
                rune_cost = 18
            case 49:
                rune_cost = 35
            case _:
                rune_cost = 0
    else:
        rune_cost = 0
    
    return (gold_cost, wood_cost, iron_cost, rune_cost)


def make_upgrade(user_id : int, item : object) -> bool:
    data = execute('''
    SELECT hero_id, level FROM clean_inventory WHERE
    hero_id = (SELECT id from hero WHERE user_id = (?) AND active = 1)
    AND item_id = (?)
    AND type = (?)
    ''', (user_id, item.id, item.type))[0]

    cost = equipment_upgrade_cost(data[1], item.rarity)
    
    hero_id = data[0]
    
    data = execute_dict('''
    SELECT gold, wood, iron, runes FROM hero WHERE
    id = (?)
    ''', (hero_id,))[0]
    
    if data["gold"] >= cost[0] and data["wood"] >= cost[1] and data["iron"] >= cost[2] and data["runes"] >= cost[3]:
        execute('''
        UPDATE hero SET
        gold = gold - (?),
        wood = wood - (?),
        iron = iron - (?),
        runes = runes - (?)
        WHERE id = (?)
        ''', (cost[0], cost[1], cost[2], cost[3], hero_id))
        
        execute('''
        UPDATE inventory SET
        level = level + 1
        WHERE
        hero_id = (?)
        AND item_id = (?)
        AND type = (
            SELECT id FROM item_types WHERE type = (?)
        )
        ''', (hero_id, item.id, item.type))
        
        add_upgrade(user_id)
        
        return True
    
    return False
