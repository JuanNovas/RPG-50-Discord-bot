import discord
from discord.ext import commands
from discord import app_commands
from cogs.utils.decorators import lock_command
from cogs.utils.lock_manager import lock_manager
from cogs.game.characters import UserDummy, MagicDummy, AssasinDummy
from cogs.game.enemies import EnemyDummy
from cogs.utils.fight import NewFight
from cogs.utils.stast_calculator import load_hero

class Combat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    #@lock_command
    @app_commands.command(name="combat", description="Simulates a combat")
    async def combat(self, inte):
        user = AssasinDummy()
        enemy = EnemyDummy()
        
        await NewFight(inte).fight(user,enemy,end=lambda user_id=inte.user.id : lock_manager.unlock(user_id))
        

async def setup(bot):
    await bot.add_cog(Combat(bot))