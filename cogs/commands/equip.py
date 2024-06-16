from discord import app_commands
from discord.ext import commands
from cogs.utils.database import execute_dict, execute

class Equip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='equip', description="Equips an equipment")
    @app_commands.describe(type='Type of equipment to equip')
    @app_commands.choices(type=[
        app_commands.Choice(name='Weapon', value='weapon'),
        app_commands.Choice(name='Armor', value='armor')
    ])
    async def equip(self, inte, type : str, item_id : int):
        data = execute('''
        SELECT * FROM clean_inventory WHERE
        user_id = (?) AND
        type = (?) AND
        item_id = (?)
        ''', (inte.user.id, type, item_id))
        if data == []:
            return await inte.response.send_message("Item not found")
        
        match type: # Checking to avoid posible SQL injection
            case "weapon":
                item_type = "weapon_id"
            case "armor":
                item_type = "armor_id"
        
        data = execute(f'''
        UPDATE hero SET
        {item_type} = (?)
        WHERE user_id = (?)
        ''', (item_id, inte.user.id))
        
        return await inte.response.send_message("Item equiped")

async def setup(bot):
    await bot.add_cog(Equip(bot))