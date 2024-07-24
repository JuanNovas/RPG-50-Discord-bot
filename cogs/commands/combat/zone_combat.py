from discord import app_commands
from discord.ext import commands
from cogs.utils.lock_manager import lock_manager
from cogs.utils.game_loop.fight import NewFight
from cogs.utils.database import execute_dict
from cogs.game.zones.encounters import get_enemy_from_zone
from cogs.utils.hero_actions import load_hero

class ZoneCombat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='zone_combat', description="Command description")
    async def zone_combat(self, inte):
        if not lock_manager.command_lock(inte.user.id):
            await inte.response.send_message("User using a command")
            return
        
        data = execute_dict('''
        SELECT * FROM hero WHERE user_id = (?) AND active = 1
        ''', (inte.user.id,))[0]

        zone_id = data["zone_id"]
        
        user = load_hero(inte.user.id)
        enemy = get_enemy_from_zone(zone_id)
        
        await inte.response.send_message("Loading")
        
        await NewFight(inte).fight(user,enemy,end=lambda user_id=inte.user.id : lock_manager.unlock(user_id))

async def setup(bot):
    await bot.add_cog(ZoneCombat(bot))