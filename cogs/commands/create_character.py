from discord.ext import commands

class Create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="create")
    async def create(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
        # dicord user's username
        username = ctx.message.author.name

        classes = ['Warrior', 'Witcher', 'Paladin']

        # asigns numbers for each class and waits for an answer
        class_options = "\n".join([f"{i+1}. {cls}" for i, cls in enumerate(classes)])
        await ctx.send(f"Select your class:\n{class_options}")
        class_msg = await self.bot.wait_for('message', check=check)
        class_choice = int(class_msg.content) - 1

        if 0 <= class_choice < len(classes):
            clase = classes[class_choice]
            await ctx.send(f"{username}, {clase}")
        else:
            await ctx.send("Invalid option, please try again")
            await self.create(ctx)
    
async def setup(bot):
    await bot.add_cog(Create(bot))