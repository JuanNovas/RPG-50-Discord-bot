from discord.ext import commands
import asyncio
from discord import Embed

class Create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="create")
    async def create(self, ctx):
        
        # dicord user's username
        username = ctx.message.author.name

        class_emojis = {
            "⚔️": "Guerrero",
            "🧙‍♂️": "Mago",
            "🗡️": "Ladrón"
        }

        # sends a message and waits for an answer via reactions.
        class_message = await ctx.send("Select your class:")
        for emoji in class_emojis.keys():
            await class_message.add_reaction(emoji)
        
        # the reaction must be from the user that executed the command, must be an emoji defined in 'class_emojis'.
        def reaction_check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in class_emojis and reaction.message.id == class_message.id
        
        try:
            reaction, user = await self.bot.wait_for('reaction_add', check=reaction_check, timeout=60.0)
        except asyncio.TimeoutError:
            await ctx.send("Time out.")
            return

        clase = class_emojis[str(reaction.emoji)]
        # Create an embed with the character information
        embed = Embed(title=f"{user} - class", color=0x00ff00)  # Green color
        embed.add_field(name="Class", value=clase)
        await ctx.send(embed=embed)
        
    
async def setup(bot):
    await bot.add_cog(Create(bot))