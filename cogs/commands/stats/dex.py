from discord import app_commands, SelectOption
from discord.ext import commands
from discord.ui import View, Select
from cogs.utils.dex import get_dex_embed

class Dex(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='dex', description="Information about enemies and equipment")
    async def dex(self, inte):
        class Dropdown(Select):
            def __init__(self):
                
                options = [
                    SelectOption(value=1, label=f"Enemies", emoji='🐉'),
                    SelectOption(value=2, label=f"Equipment", emoji='⚔️')
                ]
                
                    
                super().__init__(placeholder='Select a zone', min_values=1, max_values=1, options=options)
        
        
            async def callback(self, interaction):
                if interaction.user.id != inte.user.id:
                    return
                id = int(self.values[0])
                message = await inte.original_response()
                await message.edit(embed=get_dex_embed(interaction.user.id, id))
                await interaction.response.defer()         
                
        view = View()
        view.add_item(Dropdown())
        
        await inte.response.send_message('Select a zone to go:', view=view, embed=get_dex_embed(1,1))

async def setup(bot):
    await bot.add_cog(Dex(bot))