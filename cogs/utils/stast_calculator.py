from cogs.game.characters import *
from cogs.utils.database import execute

def load_hero(user_id : int) -> object:
    data = execute('''
    SELECT * FROM hero WHERE user_id=(?)
    ''', (user_id,))
    hero_class = get_class_by_id(data[0][2])
    hero = hero_class(level=data[0][3], weapon_id=data[0][9], armor_id=data[0][10])
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


def add_if_new(user_id : int, item : object) -> bool:
    if not has_item(user_id, item):
        add_item(user_id, item)
        return True
    else:
        return False


def has_item(user_id : int, item : object) -> bool:
    data = execute('''
    SELECT * FROM inventory
    WHERE hero_id = (
        SELECT id FROM hero WHERE user_id = (?)
    )
    AND item_id = (?)
    AND type = (
        SELECT id FROM item_types WHERE type = (?)
    )
    ''', (user_id, item.id, item.type))
    return data != []


def add_item(user_id : int, item : object) -> None:
    execute('''
    INSERT INTO inventory
    (hero_id, type, item_id)
    VALUES
    ((SELECT id FROM hero WHERE user_id = (?)), (SELECT id FROM item_types WHERE type = (?)), (?))
    ''', (user_id, item.type, item.id))
    
    
