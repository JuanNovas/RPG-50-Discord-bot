from discord.ext import commands
from cogs.utils.stast_calculator import calculate_stats
from cogs.game.characters import AssasinDummy
import sqlite3
        
class Sqlite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(name="reset")
    async def reset(self, ctx):
        with sqlite3.connect("test.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''DROP TABLE heroe''')
            cursor.execute('''
            CREATE TABLE heroe (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                class INTEGER NOT NULL,
                level INTEGER NOT NULL DEFAULT 1,
                xp INTEGER NOT NULL DEFAULT 0,
                gold INTEGER NOT NULL DEFAULT 0,
                wood INTEGER NOT NULL DEFAULT 0,
                iron INTEGER NOT NULL DEFAULT 0,
                runes INTEGER NOT NULL DEFAULT 0
            );
            ''')
            cursor.execute('''
            INSERT INTO heroe (class) VALUES (1)
            ''')
            conn.commit()
        await ctx.send("Databae reseted")
        
    @commands.command(name="stats")
    async def stats(self, ctx):
        with sqlite3.connect("test.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
            SELECT * FROM heroe WHERE id = 1
            ''')
            
            data = cursor.fetchall()[0]
            data2 = calculate_stats(AssasinDummy, data[1])
            
            stats_1 = f"Class: {data[0]}\nLevel: {data[1]}\nXP: {data[2]}\nGold: {data[3]}\nWood: {data[4]}\nIron: {data[5]}\nRunes: {data[6]}\n"
            stats_2 = f"Hp: {data2['hp']}\nAttack: {data2['attack']}\nMagic: {data2['magic']}\nDefense: {data2['defense']}\nMagic Resistance: {data2['magic_resistance']}\nMana: {data2['mana']}"
            await ctx.send(stats_1 + stats_2)
            conn.commit()

async def setup(bot):
    await bot.add_cog(Sqlite(bot))