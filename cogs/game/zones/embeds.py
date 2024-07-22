from discord import app_commands, SelectOption, Embed, Color
from discord.ext import commands
from discord.ui import View, Select

zones_data = [
    {},
    {
        "name": "🏕️ Train camp",
        "level": "Low",
        "loot": "Low",
        "image": ""
    },
    {
        "name": "⛓️ Dungeon",
        "level": "Low",
        "loot": "Low",
        "image": ""
    },
    {
        "name": "🌲 Forest",
        "level": "Mid",
        "loot": "Low",
        "image": ""
    },
    {
        "name": "🏜️ Desert",
        "level": "Mid",
        "loot": "Mid",
        "image": ""
    },
    {
        "name": "🐸 Swamp",
        "level": "High",
        "loot": "High",
        "image": ""
    }
]


def get_zone_embed(zone_id: int):
    embed = Embed(title=zones_data[zone_id]["name"], color=Color.blue())
    embed.add_field(name="Zone level", value=zones_data[zone_id]["level"], inline=False)
    embed.add_field(name="Loot", value=zones_data[zone_id]["loot"], inline=True)
    embed.set_image(url=zones_data[zone_id]["image"])
    
    return embed  

