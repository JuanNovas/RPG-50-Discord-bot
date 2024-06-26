from discord import app_commands, Embed, Color, ButtonStyle
from discord.ext import commands
from discord.ui import View, Button
from cogs.utils.database import execute_dict, execute

class Trade(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.resource_emojis = {
            1: '🌲',  # Wood
            2: '⛏️',  # Iron
            3: '🏆'   # Gold
        }

        self.resource_names = {
            1: 'Wood',
            2: 'Iron',
            3: 'Gold'
        }

    @app_commands.command(name='trade', description="Trade resources with other players")
    @app_commands.choices(
        give=[
            app_commands.Choice(name="Wood", value=1),
            app_commands.Choice(name="Iron", value=2),
            app_commands.Choice(name="Gold", value=3)
        ],
        receive=[
            app_commands.Choice(name="Wood", value=1),
            app_commands.Choice(name="Iron", value=2),
            app_commands.Choice(name="Gold", value=3)
        ]
    )
    async def trade(self, inte, give : int, give_amount : int, receive : int, receive_amount : int):
        if give == receive:
            return await inte.response.send_message("The resources must be diferents", ephemeral=True)
        elif give_amount < 0 or receive_amount < 0:
            return await inte.response.send_message("The amount of resources cannot be negative", ephemeral=True)
        elif give_amount == 0 and receive_amount == 0:
            return await inte.response.send_message("The amount of resources cannot be both 0", ephemeral=True)

        data = execute_dict('''
        SELECT * FROM hero WHERE user_id = (?)
        ''', (inte.user.id,))[0]

        if data[self.resource_names[give].lower()] < give_amount:
            return await inte.response.send_message("Not enough resources", ephemeral=True)


        embed = Embed(title="Trade Offer", color=Color.blue())
        embed.add_field(name=f"Offering {self.resource_names[give]} {self.resource_emojis[give]}", value=f"Amount: {give_amount}", inline=False)
        embed.add_field(name=f"Requesting {self.resource_names[receive]} {self.resource_emojis[receive]}", value=f"Amount: {receive_amount}", inline=False)
        
        view = View()
        accept_back = Button(label="Accept", style=ButtonStyle.primary)
        accept_back.callback = lambda i, inte=inte : self.make_trade(i, inte, give, give_amount, receive, receive_amount)
        view.add_item(accept_back)
        
        await inte.response.send_message(embed=embed, view=view)
        
        
    async def make_trade(self, interaction, inte, give : int, give_amount : int, receive : int, receive_amount : int):
        if interaction.user.id == inte.user.id:
            return await interaction.response.send_message("You cannot acept yout own trade offer", ephemeral=True)
        
        data = execute_dict('''
        SELECT * FROM hero WHERE user_id = (?)
        ''', (interaction.user.id,))[0]
        
        if data[self.resource_names[receive].lower()] < receive_amount:
            return await interaction.response.send_message("Not enough resources", ephemeral=True)
        
        data = execute_dict('''
        SELECT * FROM hero WHERE user_id = (?)
        ''', (inte.user.id,))[0]
        
        if data[self.resource_names[give].lower()] < give_amount:
            original =  await inte.original_response()
            await original.edit(view=None)
            return await interaction.response.send_message("Original trade is not valid", ephemeral=True)
        
        
        execute(f'''
        UPDATE hero SET
        {self.resource_names[give].lower()} = {self.resource_names[give].lower()} - (?),
        {self.resource_names[receive].lower()} = {self.resource_names[receive].lower()} + (?)
        WHERE user_id = (?)
        ''', (give_amount, receive_amount, inte.user.id))
        
        
        execute(f'''
        UPDATE hero SET
        {self.resource_names[give].lower()} = {self.resource_names[give].lower()} + (?),
        {self.resource_names[receive].lower()} = {self.resource_names[receive].lower()} - (?)
        WHERE user_id = (?)
        ''', (give_amount, receive_amount, interaction.user.id))
        
        original =  await inte.original_response()
        await original.edit(view=None)
        return await interaction.response.send_message("Trade completed succesfully")

async def setup(bot):
    await bot.add_cog(Trade(bot))