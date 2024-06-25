from discord import app_commands
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='ping', description="Checks bot status")
    async def ping(self, inte):
        await inte.response.send_message("Pong!")

async def setup(bot):
    await bot.add_cog(Ping(bot))


