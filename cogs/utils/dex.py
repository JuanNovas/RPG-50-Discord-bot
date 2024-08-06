from discord import Embed, Color
from cogs.utils.database import execute_dict

AMOUNT_OF_ZONES = 5
enemies_amount = [[]] # Extra list for 0 index
for i in range(AMOUNT_OF_ZONES):
    data = execute_dict('''
    SELECT COUNT(id) AS amount FROM enemies WHERE zone = (?)
    ''', (i+1,))[0]
    enemies_amount.append(data)
    
embed_titles = [[], # Extra list for 0 index
                {
                    "name": "**🏕️ Train camp**"
                },
                {
                    "name": "**⛓️ Dungeon**"
                },
                {
                    "name": "**🌲 Forest**"
                },
                {
                    "name": "**🏜️ Desert**"
                },
                {
                    "name": "**🐸 Swamp**"
                },]


def get_seen_by_zone(zone_id: int, user_id: int) -> list[dict]:
    data_list = execute_dict('''
    SELECT * FROM dex INNER JOIN enemies ON enemies.id = dex.enemy_id WHERE dex.hero_id = (
        SELECT id FROM hero WHERE user_id = (?) AND active = 1
    ) AND enemies.zone = (?)
    ''',(user_id, zone_id))
    return data_list


def get_dex_embed(user_id: int):
    embed = Embed(title="Enemy Dex", description="Enemies spotted in each zone", color=Color.blue())

    for i in range(AMOUNT_OF_ZONES):
        zone_id = i + 1
        data_list = get_seen_by_zone(zone_id, user_id)
        enemies_list = ""
        for data in data_list:
            enemies_list += "🟢 " + data["name"] + "\n"
        dif = enemies_amount[zone_id]["amount"] - len(data_list)
        if dif != 0:
            for i in range(dif):
                enemies_list += "❔ Undiscovered\n"
        embed.add_field(name=embed_titles[zone_id]["name"], value=enemies_list, inline=False)

    
    
    return embed