from cogs.game.characters.heros import *
from cogs.utils.database import execute_dict, execute

def load_hero(user_id : int) -> object:
    data = execute_dict('''
    SELECT * FROM clean_hero WHERE user_id=(?) AND active = 1
    ''', (user_id,))[0]
    hero_class = get_class_by_id(data["class"])
    hero = hero_class(level=data["level"], weapon_id=data["weapon_id"], weapon_level=data["weapon_level"], armor_id=data["armor_id"], armor_level=data["armor_level"])
    return hero

def get_class_by_id(class_id : int) -> object:
    return class_dict[class_id]

class_dict = {
    1 : MagicDummy,
    2 : AssasinDummy,
    3 : Tank
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
        SELECT id FROM hero WHERE user_id = (?) AND active = 1
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
    ((SELECT id FROM hero WHERE user_id = (?) AND active = 1), (SELECT id FROM item_types WHERE type = (?)), (?))
    ''', (user_id, item.type, item.id))
    
    
def see_enemy(user_id: int, enemy_id: int) -> None:
    execute('''
    INSERT INTO dex (hero_id, enemy_id)
    SELECT hero.id, (?)
    FROM hero
    WHERE hero.user_id = (?) AND hero.active = 1
    AND NOT EXISTS (
        SELECT 1 
        FROM dex 
        WHERE dex.hero_id = hero.id AND dex.enemy_id = (?)
    );
    ''', (enemy_id, user_id, enemy_id))
