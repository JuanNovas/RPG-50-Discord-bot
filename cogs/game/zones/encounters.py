import pandas as pd
import random
from cogs.game.characters.enemies import enemy_dict

routes = [
    "cogs\game\zones\csv\Zone enemies - Training camp.csv",
    "cogs\game\zones\csv\Zone enemies - Dungeon.csv",
    "cogs\game\zones\csv\Zone enemies - Forest.csv",
    "cogs\game\zones\csv\Zone enemies - Desert.csv"
]

df_list = [[]] # an empty list to skip index 0
probabilities = [[]]
bosses = [[]]

for route in routes:
    df = pd.read_csv(route)
    df_list.append(df)
    probabilities.append(df['Probability'].tolist())
    bosses.append(df[df['Boss'] == True].to_dict(orient='records'))
    

def get_enemy_from_zone(zone_id: int, bonus: float=None):
    enemy_data = random.choices(df_list[zone_id].to_dict(orient='records'), weights=probabilities[zone_id], k=1)[0]
    level = random.randint(enemy_data["Min-Level"], enemy_data["Max-Level"])
    if bonus:
        level = round(level * bonus)
    enemy = enemy_dict[enemy_data["ID"]](level=level)
    return enemy


def get_boos_from_zone(zone_id: int, bonus: float=None):
    boss_data = random.choices(bosses[zone_id])[0]
    boss_level = random.randint(boss_data["Min-Level"], boss_data["Max-Level"])
    if bonus:
        boss_level = round(boss_level * bonus)
    boss = enemy_dict[boss_data["ID"]](level=boss_level)
    return boss


def get_dungeon_from_zone(zone_id: int) -> list:
    enemy_amount = 2 + zone_id
    enemy_list = []

    boss = get_boos_from_zone(zone_id)
    enemy_list.append(boss)
    
    for _ in range(enemy_amount):
        enemy_list.append(get_enemy_from_zone(zone_id))
        
    return enemy_list
    