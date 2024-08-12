from discord import app_commands
from discord.ext import commands
from cogs.utils.hero_actions import load_hero
from cogs.utils.game_loop.fight import NewFight
from cogs.game.characters.enemies import EnemySlime
from cogs.utils.hero_check import hero_created

class Expedition(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='expedition', description="Creates an expedition")
    async def expedition(self, inte):
        if not await hero_created(inte):
            return
        
        
        hero = load_hero(inte.user.id, name=inte.user.name)
        await inte.response.send_message("Loading")
        await NewFight(inte).consecutive_fight(hero, [EnemySlime(level=10), EnemySlime()])
        
        
    

async def setup(bot):
    await bot.add_cog(Expedition(bot))