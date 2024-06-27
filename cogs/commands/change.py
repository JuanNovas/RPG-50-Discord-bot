from discord import app_commands, SelectOption
from discord.ext import commands
from discord.ui import View, Select
from cogs.utils.database import execute_dict, execute
from cogs.utils.hero_actions import class_dict

class ChangeHero(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='changehero', description="Change the hero selected")
    async def changehero(self, inte):
        class Dropdown(Select):
            def __init__(self):
                self.inte = inte
                data = execute_dict('''
                SELECT * FROM hero WHERE user_id = (?)
                ''', (inte.user.id, ))
                
                options = []
                
                for hero in data:
                    options.append(SelectOption(value=hero["id"], label=f"{class_dict[hero['class']].__name__} level {hero['level']}", description=f"gold: {hero['gold']} & xp:{hero['xp']}", emoji='🟦'))
                    
                super().__init__(placeholder='Select a Hero', min_values=1, max_values=1, options=options)
        
        
            async def callback(self, interaction):
                if interaction.user.id != inte.user.id:
                    return
                
                execute('''
                UPDATE hero SET
                active = 0
                WHERE user_id = (?)
                ''', (interaction.user.id,))
                execute('''
                UPDATE hero SET
                active = 1
                WHERE id = (?)
                ''', (self.values[0],))
                await interaction.response.send_message("Hero changed succesfully")
                
                
        # Crear la vista que muestra el Select
        view = View()
        view.add_item(Dropdown())

        # Enviar el mensaje con el Select
        await inte.response.send_message('Select a hero to use:', view=view)

async def setup(bot):
    await bot.add_cog(ChangeHero(bot))