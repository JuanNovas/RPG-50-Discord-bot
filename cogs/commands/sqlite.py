from discord.ext import commands
        
class Sqlite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(name="reset")
    async def reset(self, ctx):
        self.bot.cursor.execute('''DROP TABLE heroe''')
        self.bot.cursor.execute('''
        CREATE TABLE heroe (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            level INTEGER NOT NULL,
            xp INTEGER NOT NULL,
            gold INTEGER NOT NULL,
            wood INTEGER NOT NULL,
            iron INTEGER NOT NULL,
            runes INTEGER NOT NULL
        );
        ''')
        await ctx.send("Databae reseted")

async def setup(bot):
    await bot.add_cog(Sqlite(bot))