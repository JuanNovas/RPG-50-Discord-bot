from discord import app_commands, Embed, ButtonStyle
from discord.ext import commands
from discord.ui import View, Button
from cogs.utils.hero_actions import load_hero
from cogs.utils.game_loop.fight import NewFight
from cogs.utils.hero_check import hero_created
from cogs.game.zones.encounters import get_dungeon_from_zone, get_dungeon_loot_from_zone
from cogs.utils.querys import get_zone

class Dungeon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='dungeon', description="Creates an dungeon")
    @app_commands.choices(
        cooperative=[
            app_commands.Choice(name="No", value=2),
            app_commands.Choice(name="Yes", value=1)
        ]
    )
    async def dungeon(self, inte, cooperative: int):
        if not await hero_created(inte):
            return
        
        
        if cooperative == 1:
            view = View()
            
            embed = Embed(title="Dungeon", description="Enter the dungeon", color=0x3498db)
            embed.add_field(name="How to play", value="Click the play button")
            
            play_button = Button(label="Play", style=ButtonStyle.primary)
            play_button.callback = lambda i, player_name=inte.user.name, player_id=inte.user.id, player_inte = inte : self.load_players(i, player_name, player_id, player_inte)
            view.add_item(play_button)  
            
            await inte.response.send_message(embed=embed, view=view)
    
        elif cooperative == 2:
            hero = load_hero(inte.user.id, name=inte.user.name)
            if hero.level < 5:
                return await inte.response.send_message("Level 5 required to enter a dungeon")
            await inte.response.send_message("Loading")
            zone_id = get_zone(inte.user.id)
            enemies = get_dungeon_from_zone(zone_id)
            loot = get_dungeon_loot_from_zone(zone_id)
            await NewFight(inte).consecutive_fight(hero, enemies, bonus=loot)
            
            
            
    async def load_players(self, inte, player_name, player_id, player_inte):
        if inte.user.id == player_id:
            return 
        
        if not await hero_created(inte):
            return
        
        hero = load_hero(inte.user.id, name=inte.user.name)
        if hero.level < 5:
            return await inte.response.send_message("Level 5 required to enter a dungeon", ephemeral=True)
        
        zone_id = get_zone(player_id)
        bonus = 1.75
        if zone_id == 1:
            bonus = 3
        
        users_data = [
            (inte.user.id, hero, inte), # Places switched because in Fight turns change order, and first user should be the first to attack.
            (player_id, load_hero(player_id, name=player_name), player_inte)
        ]
        
        original_message = await player_inte.original_response()
        await original_message.delete()
        await inte.response.send_message("Loading")
        
        enemies = get_dungeon_from_zone(zone_id, bonus=bonus)
        loot = get_dungeon_loot_from_zone(zone_id)
        await NewFight(inte).consecutive_multi_fight(users_data, enemies, bonus=loot)
        
        
    

async def setup(bot):
    await bot.add_cog(Dungeon(bot))