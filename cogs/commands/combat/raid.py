from discord import app_commands, Embed, ButtonStyle
from discord.ext import commands
from discord.ui import View, Button
from cogs.utils.hero_actions import load_hero
from cogs.utils.game_loop.fight import NewFight
from cogs.game.zones.encounters import get_enemy_from_zone
from cogs.utils.querys import get_zone
from cogs.utils.hero_check import hero_created

class Raid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='raid', description="A strong enemy raid")
    async def raid(self, inte):
        if not await hero_created(inte):
            return
        
        hero = load_hero(inte.user.id)
        if hero.level < 10:
            return await inte.response.send_message("Level 10 required to enter a raid")
        
        view = View()
        
        embed = Embed(title="Raid", description="Raid battle", color=0x3498db)
        embed.add_field(name="How to play", value="Click the play button")
        
        play_button = Button(label="Play", style=ButtonStyle.primary)
        play_button.callback = lambda i, player_name=inte.user.name, player_id=inte.user.id, player_inte = inte : self.load_players(i, player_name, player_id, player_inte)
        view.add_item(play_button)  
        
        
        await inte.response.send_message(embed=embed, view=view)
        
    
    async def load_players(self, inte, player_name, player_id, player_inte):
        if inte.user.id == player_id:
            return 
        
        if not await hero_created(inte):
            return
        
        hero = load_hero(inte.user.id, name=inte.user.name)
        if hero.level < 10:
            return await inte.response.send_message("Level 10 required to enter a raid", ephemeral=True)
        
        zone = get_zone(player_id)
        bonus = 1.75
        if zone == 1:
            bonus = 3
        
        users_data = [
            (player_id, load_hero(player_id, name=player_name), player_inte),
            (inte.user.id, hero, inte)
        ]
        
        original_message = await player_inte.original_response()
        await original_message.delete()
        await inte.response.send_message("Loading")
        
        await NewFight(inte).multi_fight(users_data, get_enemy_from_zone(zone, bonus=bonus))

async def setup(bot):
    await bot.add_cog(Raid(bot))