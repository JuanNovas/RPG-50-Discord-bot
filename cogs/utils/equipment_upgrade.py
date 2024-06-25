from cogs.utils.database import execute, execute_dict

def equipment_upgrade_cost(level : int, rarity : int) -> tuple:
    if not (0 <= level <= 49 and level < rarity * 10):
        raise ValueError
    
    # Gold
    gold_cost = level * (100 * ((level // 10) + 1))
    
    # Wood
    wood_cost = 10 + level ** 2 * 2
    
    # Iron
    iron_cost = level + 5 ** (0.1 * level)
    
    # Runes
    if rarity >= 4:
        match level:
            case 34:
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
    user_id = (?)
    AND item_id = (?)
    AND class_type = (?)
    ''', (user_id, item.id, item.type))[0]
    
    cost = equipment_upgrade_cost(data[1], item.rarity)
    
    hero_id = data[0]
    
    data = execute_dict('''
    SELECT gold, wood, iron, runes FROM hero WHERE
    id = (?)
    ''', (hero_id,))
    
    if data["gold"] >= cost[0] and data["wood"] >= cost[1] and data["iron"] >= cost[2] and data["runes"] >= cost[3]:
        execute('''
        UPDATE hero ON
        gold = gold - (?)
        AND wood = wood - (?)
        AND iron = iron - (?)
        AND runes = runes - (?)
        WHERE id = (?)
        ''', (cost[0], cost[1], cost[2], cost[3], hero_id))
        
        execute('''
        UPDATE inventory ON
        level = level + 1
        WHERE
        hero_id = (?)
        AND item_id = (?)
        AND class_type = (
            SELECT id FROM item_types WHERE type = (?)
        )
        ''', (hero_id, item.id, item.type))
        
        return True
    
    return False