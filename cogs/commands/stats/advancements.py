from discord import app_commands, Embed, Color
from discord.ext import commands
from cogs.utils.database import execute_dict
from cogs.utils.hero_check import hero_created

class Advancements(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='advancements', description="Users advancements")
    async def advancements(self, inte):
        if not await hero_created(inte):
            return
        
        def create_bar(progress: int, total: int) -> str:
            percent = progress / total
            filled_length = int(40 * percent)
            bar = '█' * filled_length + '-' * (40 - filled_length)
            
            return f'`[{bar}]`'
        
        data = execute_dict('''
        SELECT * FROM advancements WHERE hero_id = (SELECT id FROM hero WHERE user_id = (?) AND active = 1)
        ''', (inte.user.id,))[0]
        
        
        embed = Embed(title=f"{inte.user.name}'s advancements", color=Color.blue())
        embed.add_field(name=f'Kill 100 monsters ({data["kills"]}/100)', value=create_bar(data["kills"],100), inline=False)
        embed.add_field(name=f'Upgrade equipments 30 times ({data["upgrades"]}/30)', value=create_bar(data["upgrades"], 30), inline=False)
        embed.add_field(name=f'Spent 100.000 coints ({data["gold_spent"]}/100000)', value=create_bar(data["gold_spent"], 100000), inline=False)
        
        await inte.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Advancements(bot))