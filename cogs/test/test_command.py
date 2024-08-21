from discord import app_commands
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='test', description="test command")
    async def test(self, inte):
        await inte.response.send_message("Pong!")

async def setup(bot):
    await bot.add_cog(Test(bot))