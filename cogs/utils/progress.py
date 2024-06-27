from cogs.utils.database import execute


def add_kill(user_id : int, amount=1):
    execute('''
    UPDATE advancements SET
    kills = kills + (?)
    WHERE hero_id = (
        SELECT id FROM hero WHERE user_id = (?) AND active = 1
    )
    ''', (amount, user_id))
    
    
def add_upgrade(user_id : int, amount=1):
    execute('''
    UPDATE advancements SET
    upgrades = upgrades + (?)
    WHERE hero_id = (
        SELECT id FROM hero WHERE user_id = (?) AND active = 1
    )
    ''', (amount, user_id))
    
    
def add_gold_spent(user_id : int, amount : int):
    execute('''
    UPDATE advancements SET
    gold_spent = gold_spent + (?)
    WHERE hero_id = (
        SELECT id FROM hero WHERE user_id = (?) AND active = 1
    )
    ''', (amount, user_id))