from discord.ext import commands
from cogs.utils.stast_calculator import calculate_stats
from cogs.utils.database import execute
import sqlite3
        
class Sqlite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(name="reset")
    async def reset(self, ctx):
        with sqlite3.connect("test.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''DROP TABLE hero''')
            cursor.execute('''
            CREATE TABLE hero (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL UNIQUE,
                class INTEGER NOT NULL,
                level INTEGER NOT NULL DEFAULT 1,
                xp INTEGER NOT NULL DEFAULT 0,
                gold INTEGER NOT NULL DEFAULT 0,
                wood INTEGER NOT NULL DEFAULT 0,
                iron INTEGER NOT NULL DEFAULT 0,
                runes INTEGER NOT NULL DEFAULT 0,
                weapon_id INTEGER DEFAULT NULL,
                armor_id INTEGER DEFAUUT NULL
            );
            ''')
            cursor.execute('''
            CREATE UNIQUE INDEX user_id_index ON hero(user_id);
            ''')
            conn.commit()
        await ctx.send("Databae reseted")
        
    
    @commands.command(name="all_data")
    async def all_data(self, ctx):
        data = execute('''
        SELECT * FROM hero
        ''')
        await ctx.send(data)
        
        
    @commands.command(name="set_level")
    async def set_level(self, ctx, level:int):
        execute('''
        UPDATE hero SET level=(?) WHERE user_id=(?)
        ''', (level, ctx.author.id))
        await ctx.send("Level updated")

async def setup(bot):
    await bot.add_cog(Sqlite(bot))