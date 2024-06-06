def calculate_stats(base_class : object, level : int) -> dict:
    stats_dic = dict()
    stats = ["hp", "attack", "magic", "defense", "magic_resistance", "mana"]
    base_class = base_class()
    base = {
        "hp": base_class.base_hp,
        "attack": base_class.base_attack,
        "magic": base_class.base_magic,
        "defense": base_class.base_defense,
        "magic_resistance": base_class.base_magic_resistance,
        "mana": base_class.base_mana,
    }
    level = level - 1
    for stat in stats:
        stats_dic[stat] = base[stat] * (1.15 ** level)
        print(stats_dic[stat])
        
    return stats_dic