from discord.ext import commands
from cogs.game.enemies import EnemyDummy
from cogs.utils.lock_manager import LockManager

lock_manager = LockManager()

class Dungeon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.current_step = 0
        self.total_steps = 5 # NUMBER OF COMBATS IN THE DUNGEON !! IMPORTANT


    @commands.command(name="dungeon")
    async def start_dungeon(self, ctx):
        if lock_manager.is_locked(ctx.author.id):
            await ctx.send("You are already in a dungeon")
            return
        

        self.current_step = 0
        await self.next_combat(ctx)

    async def next_combat(self, ctx):
        if self.current_step < self.total_steps:
            enemy = EnemyDummy() # GENERATE NEW ENEMY FOR THIS STEP
            await self.bot.get_cog('Fight').fight(ctx, enemy, self.combat_completed)
            self.current_step += 1 
        else:
            await ctx.send("Dungeon completed!")

    async def combat_completed(self, ctx, user):
        await ctx.send(f"Combat {self.current_step} completed!")
        await self.next_combat(ctx)


async def setup(bot):
    await bot.add_cog(Dungeon(bot))


