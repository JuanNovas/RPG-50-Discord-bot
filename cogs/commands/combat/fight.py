from discord import app_commands
from discord.ext import commands
from cogs.utils.game_loop.fight import NewFight
from cogs.utils.hero_check import hero_created
from cogs.game.zones.encounters import get_enemy_from_zone
from cogs.utils.hero_actions import load_hero
from cogs.utils.querys import get_zone

class Fight(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='fight', description="Command description")
    async def fight(self, inte):
        if not await hero_created(inte):
            return


        zone_id = get_zone(inte.user.id)
        
        user = load_hero(inte.user.id, name=inte.user.name)
        enemy = get_enemy_from_zone(zone_id)
        
        await inte.response.send_message("Loading")
        
        await NewFight(inte).fight(user,enemy)

async def setup(bot):
    await bot.add_cog(Fight(bot))