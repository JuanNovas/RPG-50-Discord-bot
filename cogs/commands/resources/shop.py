from discord import app_commands, Embed
from discord.ui import View
from discord.ext import commands
from cogs.utils.database import execute_dict, execute
from cogs.utils.progress import add_gold_spent

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='shop', description="Item Shop")
    async def shop(self, inte):
        embed = Embed(title="Shop", description="Prices: ", color=0x3498db)

        embed.add_field(
            name="/buy",
            value="🪙 15 Gold → 🌲 1 Wood\n🪙 150 Gold → ⛏️ 1 Iron",
            inline=False
        )
        
        view = View()
        await inte.response.send_message(embed=embed, view=view)
        
        
    @app_commands.command(name="buy", description="Buy something from the shop")
    @app_commands.choices(
        item=[
            app_commands.Choice(name="Wood", value="wood"),
            app_commands.Choice(name="Iron", value="iron")
        ]
    )
    async def buy(self, inte, item : str, amount : int):
        if amount <= 0:
            await inte.response.send_message(f"An amount of {amount} is not supported, it has to be at least 1")
            return
        
        
        prices = {
            "wood" : 15,
            "iron" : 150
        }
        
            
        data = execute_dict('''
        SELECT gold FROM hero WHERE user_id = (?) AND active = 1
        ''', (inte.user.id,))[0]
        
        user_gold = data["gold"]
        
        price = prices[item] * amount
        if price > user_gold:
            await inte.response.send_message("Don't enough gold")
            return
        
        execute(f'''
        UPDATE hero SET
        gold = gold - (?),
        {item} = {item} + (?)
        WHERE user_id = (?)
        AND active = 1
        ''', (price, amount, inte.user.id))
        
        add_gold_spent(inte.user.id, price)
        
        await inte.response.send_message(f"{amount} of {item} has been bought")
        

async def setup(bot):
    await bot.add_cog(Shop(bot))