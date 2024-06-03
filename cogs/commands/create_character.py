from discord.ext import commands
import asyncio
from discord import Embed

class Create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="create")
    async def create(self, ctx):
        
        class_emojis = {
            "⚔️": "Warrior",
            "🧙‍♂️": "Magician",
            "🗡️": "Thief"
        }

        # sends a message and waits for an answer via reactions.
        embed = Embed(title="CHOOSE YOUR CLASS!", color=0xADD8E6)
        embed.add_field(name="WARRIOR", value="test")
        embed.add_field(name="MAGICIAN", value="test")
        embed.add_field(name="THIEF", value="test")
        embed.set_image(url="https://cdn.discordapp.com/attachments/474702643625984021/1247263771811119224/72fcadcd-905e-4db7-9065-ea523ca7638d.jpg?ex=665f6468&is=665e12e8&hm=5fc58203fe3fcffae54347b6726480f49e84e1ff4828bc0b16c22b7be4328013&")
        class_message = await ctx.send(embed=embed)
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
        embed = Embed(title=f"{user} - class", description="Character created _succesfully_!", color=0xADD8E6)  # Green color
        embed.add_field(name="class:", value=clase)
        if clase == "Magician":
            embed.set_image(url="https://cdn.discordapp.com/attachments/474702643625984021/1246905943997022299/310a8713-429a-41cf-835c-25e56a3873ee.jpg?ex=665ebfe7&is=665d6e67&hm=c17a5297bd9ffbd2aa06cc38a9613b167f3512fedb1432191e4109ab2201ca8f&")
        await ctx.send(embed=embed)
        
    
async def setup(bot):
    await bot.add_cog(Create(bot))