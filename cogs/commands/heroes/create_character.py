import discord
from discord.ext import commands
from discord.ui import Button, View
from discord import Embed, app_commands
from cogs.utils.database import execute_dict
from cogs.utils.hero_check import hero_created
from cogs.utils.create import create_hero


class Create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="create", description="Hero creation")
    async def create(self, inte):
        
        async def choose_no(inte):
            await inte.delete_original_response()
        
        async def choose_yes(inte, i):
            await inte.delete_original_response()
            await create_hero(i)
        
        if not await hero_created(inte):
            return
        
        data = execute_dict('''
        SELECT * FROM hero WHERE user_id = (?)
        ''',(inte.user.id,))
        
        for hero in data:
            if hero["level"] < 20:
                return await inte.response.send_message("All heroes must be level 20 to create a new one")
            
            
        embed = Embed(title=f"Create new hero", color=discord.Color.blue())
        embed.add_field(name="⚠️ IMPORTANT ⚠️", value="Are you sure you want to create a new Hero?\nYou woud not be able to create another until you reach level 20", inline=True)
        
        view = View()
        
        button_yes = Button(label="Yes", style=discord.ButtonStyle.primary)
        button_yes.callback = lambda i, inte=inte: choose_yes(inte, i)
        view.add_item(button_yes)
        button_no = Button(label="No", style=discord.ButtonStyle.primary)
        button_no.callback = lambda i, inte=inte: choose_no(inte)
        view.add_item(button_no)
        
        self.message = await inte.response.send_message(embed=embed, view=view, ephemeral=True)
        
        
        
        
    

async def setup(bot):
    await bot.add_cog(Create(bot))