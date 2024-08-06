from discord import app_commands
from discord.ext import commands
from cogs.utils.dex import get_dex_embed

class Dex(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='dex', description="Information about enemies and equipment")
    async def dex(self, inte):     
        await inte.response.send_message('Select a zone to go:', embed=get_dex_embed(inte.user.id))

async def setup(bot):
    await bot.add_cog(Dex(bot))