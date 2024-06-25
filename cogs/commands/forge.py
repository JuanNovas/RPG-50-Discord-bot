from discord import app_commands
from discord.ext import commands

class Forge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='forge', description="Equipment Upgrades")
    async def forge(self, inte):
        await inte.response.send_message("Pong!")

async def setup(bot):
    await bot.add_cog(Forge(bot))