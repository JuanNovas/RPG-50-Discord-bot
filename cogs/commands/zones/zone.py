from discord import app_commands
from discord.ext import commands
from cogs.game.zones.embeds import get_zone_full_embed

class Zone(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='zone', description="zone description")
    async def zone(self, inte):
        await inte.response.send_message(embed=get_zone_full_embed(inte.user.id))

async def setup(bot):
    await bot.add_cog(Zone(bot))