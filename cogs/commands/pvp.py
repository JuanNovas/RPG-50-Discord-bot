from discord import app_commands, Embed, ButtonStyle
from discord.ext import commands
from discord.ui import View, Button
from cogs.utils.hero_actions import load_hero
from cogs.utils.game_loop.fight import NewFight


class Pvp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='pvp', description="Creates a pvp combat")
    async def pvp(self, inte):
        view = View()
        
        embed = Embed(title="pvp", description=f"{inte.user.name} is challenging for a battle", color=0x3498db)
        embed.add_field(name="How to play", value="Click the play button")
        
        play_button = Button(label="Play", style=ButtonStyle.primary)
        play_button.callback = lambda i, player_name=inte.user.name, player_id=inte.user.id, player_inte = inte : self.load_players(i, player_name, player_id, player_inte)
        view.add_item(play_button)  
        
        
        await inte.response.send_message(embed=embed, view=view)
        self.message = await inte.original_response()
        
        
    async def load_players(self, inte, player_name, player_id, player_inte):
        if inte.user.id == player_id:
            return 
        
        users_data = [
            (player_id, load_hero(player_id), player_inte),
            (inte.user.id, load_hero(inte.user.id), inte)
        ]
        
        await self.message.delete()
        
        await NewFight(inte).pvp_fight(users_data)

async def setup(bot):
    await bot.add_cog(Pvp(bot))