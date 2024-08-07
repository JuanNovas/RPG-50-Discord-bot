from discord import app_commands
from discord.ext import commands
from cogs.utils.hero_actions import load_hero
from cogs.utils.game_loop.fight import NewFight
from cogs.game.characters.enemies import EnemySlime
from cogs.game.zones.encounters import get_dungeon_from_zone
from cogs.utils.querys import get_zone

class Dungeon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='dungeon', description="Creates an dungeon")
    async def dungeon(self, inte):
        
        hero = load_hero(inte.user.id)
        await inte.response.send_message("Loading")
        enemies = get_dungeon_from_zone(get_zone(inte.user.id))
        await NewFight(inte).consecutive_fight(hero, enemies)
        
        
    

async def setup(bot):
    await bot.add_cog(Dungeon(bot))