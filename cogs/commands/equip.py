from discord import app_commands, SelectOption
from discord.ui import Select, View
from discord.ext import commands
from cogs.utils.database import execute_dict, execute
from cogs.game.items.weapons import weapon_dict
from cogs.game.items.armors import armor_dict

class Equip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name='equip_weapon', description="Equips an equipment")
    async def equip_weapon(self, inte):
        class Dropdown(Select):
            def __init__(self):

                data = execute_dict('''
                SELECT * FROM inventory
                WHERE hero_id = (SELECT id from hero WHERE user_id = (?))
                AND type = 1
                ''', (inte.user.id,))

                options = []
                
                for item in data:
                    item_obj = weapon_dict[item["item_id"]]()
                    options.append(SelectOption(value=item["item_id"] ,label=item_obj.name, description=f"Id: {item_obj.id}  &  Level: {item['level']}", emoji='🟦'))
                
                super().__init__(placeholder='Choose your favourite colour...', min_values=1, max_values=1, options=options)

            async def callback(self, interaction):
                data = execute(f'''
                UPDATE hero SET
                weapon_id = (?)
                WHERE user_id = (?)
                ''', (self.values[0], inte.user.id))
                await interaction.response.send_message("Equiped")

        # Crear la vista que muestra el Select
        view = View()
        view.add_item(Dropdown())

        # Enviar el mensaje con el Select
        await inte.response.send_message('Select an equipment to equip:', view=view)
        
        
        
    @app_commands.command(name='equip_armor', description="Equips an equipment")
    async def equip_armor(self, inte):
        class Dropdown(Select):
            def __init__(self):

                data = execute_dict('''
                SELECT * FROM inventory
                WHERE hero_id = (SELECT id from hero WHERE user_id = (?))
                AND type = 2
                ''', (inte.user.id,))

                options = []
                
                for item in data:
                    item_obj = armor_dict[item["item_id"]]()
                    options.append(SelectOption(value=item["item_id"] ,label=item_obj.name, description=f"Id: {item_obj.id}  &  Level: {item['level']}", emoji='🟦'))
                
                super().__init__(placeholder='Choose your favourite colour...', min_values=1, max_values=1, options=options)

            async def callback(self, interaction):
                data = execute(f'''
                UPDATE hero SET
                armor_id = (?)
                WHERE user_id = (?)
                ''', (self.values[0], inte.user.id))
                await interaction.response.send_message("Equiped")

        # Crear la vista que muestra el Select
        view = View()
        view.add_item(Dropdown())

        # Enviar el mensaje con el Select
        await inte.response.send_message('Select an equipment to equip:', view=view)



    

async def setup(bot):
    await bot.add_cog(Equip(bot))