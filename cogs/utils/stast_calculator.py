from cogs.game.characters import *
from cogs.utils.database import execute

def load_hero(hero_id : int) -> object:
    data = execute('''
    SELECT * FROM hero WHERE id=(?)
    ''', hero_id)
    
    hero_class = get_class_by_id(data[0][1])
    hero = hero_class(level=data[0][2])
    return hero
    
def calculate_stats(class_id : int, level : int) -> dict:
    stats_dic = dict()
    stats = ["hp", "attack", "magic", "defense", "magic_resistance", "mana"]
    base_class = get_class_by_id(class_id)()
    base = {
        "hp": base_class.max_hp,
        "attack": base_class.attack,
        "magic": base_class.magic,
        "defense": base_class.defense,
        "magic_resistance": base_class.magic_resistance,
        "mana": base_class.max_mana,
    }
    level = level - 1
    for stat in stats:
        stats_dic[stat] = round(base[stat] * (1.15 ** level))
        
    return stats_dic

def get_class_by_id(class_id : int) -> object:
    return class_dict[class_id]


class_dict = {
    1 : MagicDummy,
    2 : AssasinDummy
}