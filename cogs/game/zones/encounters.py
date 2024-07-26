import pandas as pd
import random
from cogs.game.characters.enemies import enemy_dict

routes = [
    "cogs\game\zones\csv\Zone enemies - Training camp.csv",
    "cogs\game\zones\csv\Zone enemies - Dungeon.csv",
    "cogs\game\zones\csv\Zone enemies - Forest.csv"
]

df_list = [[]] # an empty list to skip index 0
probabilities = [[]]

for route in routes:
    df = pd.read_csv(route)
    df_list.append(df)
    probabilities.append(df['Probability'].tolist())

def get_enemy_from_zone(zone_id: int):
    enemy_data = random.choices(df_list[zone_id].to_dict(orient='records'), weights=probabilities[zone_id], k=1)[0]
    level = random.randint(enemy_data["Min-Level"], enemy_data["Max-Level"])
    enemy = enemy_dict[enemy_data["ID"]](level=level)
    return enemy


