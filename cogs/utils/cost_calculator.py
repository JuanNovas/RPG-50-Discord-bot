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