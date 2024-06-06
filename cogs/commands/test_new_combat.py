from discord.ext import commands
from cogs.utils.decorators import lock_command
from cogs.utils.lock_manager import lock_manager
from cogs.game.characters import UserDummy, MagicDummy, AssasinDummy
from cogs.game.enemies import EnemyDummy
from cogs.utils.fight import NewFight

class Test_new_combat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @lock_command(name="test_new_combat")
    async def test_new_combat(self, ctx):
        user = AssasinDummy()
        enemy = EnemyDummy()
        
        await NewFight(ctx).fight(user,enemy,end=lambda user_id=ctx.author.id : lock_manager.unlock(user_id))
async def setup(bot):
    await bot.add_cog(Test_new_combat(bot))