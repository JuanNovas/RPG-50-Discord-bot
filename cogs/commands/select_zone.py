from discord import app_commands, SelectOption, Embed, Color
from discord.ext import commands
from discord.ui import View, Select

class Select_zone(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='select_zone', description="Selects a zone of the map")
    async def select_zone(self, inte):
        class Dropdown(Select):
            def __init__(self):
                self.inte = inte
                
                options = [
                    SelectOption(value=1, label=f"Dungeon", emoji='⛓️'),
                    SelectOption(value=2, label=f"Forest", emoji='🌲'),
                    SelectOption(value=3, label=f"Desert", emoji='🏜️'),
                    SelectOption(value=4, label=f"Swamp", emoji='🐸')
                ]
                
                    
                super().__init__(placeholder='Select a zone', min_values=1, max_values=1, options=options)
        
        
            async def callback(self, interaction):
                if interaction.user.id != inte.user.id:
                    return
                await interaction.response.send_message(f"{self.values[0]}")
                
                
        view = View()
        view.add_item(Dropdown())

        embed = Embed(title="Zone selector", color=Color.blue())
        embed.add_field(name='⛓️ Dungeon', value="Low level zone, full of week enemies", inline=False)
        embed.add_field(name='🌲 Forest', value="Mid level zone, lots of resources", inline=False)
        embed.add_field(name='🏜️ Desert', value="Mid level zone, lots of gold", inline=False)
        embed.add_field(name='🐸 Swamp', value="High level zone, very strong enemies and high rarity loot", inline=False)

        await inte.response.send_message('Select a zone to go:', view=view, embed=embed)

async def setup(bot):
    await bot.add_cog(Select_zone(bot))