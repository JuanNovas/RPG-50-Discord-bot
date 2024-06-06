from discord.ext import commands
from cogs.utils.stast_calculator import calculate_stats
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
                class INTEGER NOT NULL,
                level INTEGER NOT NULL DEFAULT 1,
                xp INTEGER NOT NULL DEFAULT 0,
                gold INTEGER NOT NULL DEFAULT 0,
                wood INTEGER NOT NULL DEFAULT 0,
                iron INTEGER NOT NULL DEFAULT 0,
                runes INTEGER NOT NULL DEFAULT 0
            );
            ''')
            conn.commit()
        await ctx.send("Databae reseted")
        
    @commands.command(name="stats")
    async def stats(self, ctx, id=1):
        with sqlite3.connect("test.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
            SELECT * FROM hero WHERE id = (?)
            ''', (id,))
            
            data = cursor.fetchall()[0]
            data2 = calculate_stats(data[1], data[2])
            
            stats_1 = f"Class: {data[1]}\nLevel: {data[2]}\nXP: {data[3]}\nGold: {data[4]}\nWood: {data[5]}\nIron: {data[6]}\nRunes: {data[7]}\n"
            stats_2 = f"Hp: {data2['hp']}\nAttack: {data2['attack']}\nMagic: {data2['magic']}\nDefense: {data2['defense']}\nMagic Resistance: {data2['magic_resistance']}\nMana: {data2['mana']}"
            conn.commit()
            await ctx.send(stats_1 + stats_2)
            
    @commands.command(name="new")
    async def new(self, ctx, class_id=1, level=1):
        with sqlite3.connect("test.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO hero (class, level) VALUES (?,?)             
            ''', (class_id, level))
            
            conn.commit()
        await ctx.send("Heroe created")

async def setup(bot):
    await bot.add_cog(Sqlite(bot))