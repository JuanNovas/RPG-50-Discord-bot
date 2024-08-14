import discord
from discord import app_commands
from discord.ext import commands
from cogs.utils.database import execute_dict
from cogs.game.items.weapons import weapon_dict
from cogs.game.items.armors import armor_dict
from discord import Embed
from cogs.utils.hero_check import hero_created

class Inventory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='inventory', description="Shows the inventory")
    async def inventory(self, inte):
        if not await hero_created(inte):
            return
        
        data = execute_dict('''
        SELECT * FROM inventory
        WHERE hero_id = (SELECT id from hero WHERE user_id = (?) AND active = 1) ORDER BY level DESC
        ''', (inte.user.id,))
        if data == []:
            return await inte.response.send_message("No items")
        
        embed = Embed(title="Inventory", color=discord.Color.blue())
        
        for item in data:
            match item["type"]:
                case 1 :
                    item_dict = weapon_dict
                case 2:
                    item_dict = armor_dict
                    
            item_obj = item_dict[item["item_id"]]()
            embed.add_field(name=item_obj.name, value=f"Type: {item_obj.type}  &  Level: {item['level']}")
        
        return await inte.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Inventory(bot))