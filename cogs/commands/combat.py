from discord.ext import commands
from discord import app_commands
from cogs.utils.lock_manager import lock_manager
from cogs.game.characters.heros import UserDummy, MagicDummy, AssasinDummy
from cogs.game.characters.enemies import EnemyDummy
from cogs.utils.game_loop.fight import NewFight
from cogs.utils.hero_actions import load_hero
from cogs.game.items.weapons import WeaponKnife

class Combat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="combat", description="Simulats a combat with the user hero")
    async def combat(self, inte):
        if not lock_manager.command_lock(inte.user.id):
            await inte.response.send_message("User using a command")
            return

        user = load_hero(inte.user.id)
        enemy = EnemyDummy()
        
        await NewFight(inte).fight(user,enemy,end=lambda user_id=inte.user.id : lock_manager.unlock(user_id))

async def setup(bot):
    await bot.add_cog(Combat(bot))