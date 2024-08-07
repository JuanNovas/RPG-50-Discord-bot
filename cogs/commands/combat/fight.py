from discord import app_commands
from discord.ext import commands
from cogs.utils.lock_manager import lock_manager
from cogs.utils.game_loop.fight import NewFight
from cogs.utils.database import execute_dict
from cogs.game.zones.encounters import get_enemy_from_zone
from cogs.utils.hero_actions import load_hero
from cogs.utils.querys import get_zone

class Fight(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='fight', description="Command description")
    async def fight(self, inte):
        if not lock_manager.command_lock(inte.user.id):
            await inte.response.send_message("User using a command")
            return

        zone_id = get_zone(inte.user.id)
        
        user = load_hero(inte.user.id)
        enemy = get_enemy_from_zone(zone_id)
        
        await inte.response.send_message("Loading")
        
        await NewFight(inte).fight(user,enemy,end=lambda user_id=inte.user.id : lock_manager.unlock(user_id))

async def setup(bot):
    await bot.add_cog(Fight(bot))