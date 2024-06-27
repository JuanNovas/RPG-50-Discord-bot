from discord.ext import commands
from cogs.utils.database import execute, execute_dict
from cogs.game.items.armors import armor_dict
from cogs.game.items.weapons import weapon_dict
import sqlite3
import os
        
class Sqlite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(name="reset")
    async def reset(self, ctx):
        sql_file_path = "data/schema.sql"
        
        if not os.path.isfile(sql_file_path):
            await ctx.send(f"The file {sql_file_path} does not exist.")
            return
        
        with open(sql_file_path, 'r') as sql_file:
            sql_script = sql_file.read()

        with sqlite3.connect("test.db") as conn:
            cursor = conn.cursor()
            cursor.executescript(sql_script)
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
        UPDATE hero SET level=(?) WHERE user_id=(?) AND active = 1
        ''', (level, ctx.author.id))
        await ctx.send("Level updated")
    
    
    @commands.command(name="add_item")
    async def add_item(self, ctx, type_id : int, item_id : int):
        execute('''
        INSERT INTO inventory (hero_id, type, item_id)
        VALUES ((SELECT id FROM hero WHERE user_id=(?) AND active = 1),?,?)
        ''', (ctx.author.id, type_id, item_id))
        await ctx.send("Item added to inventory")
        
    @commands.command(name="equip")
    async def equip(self, ctx, item_id : int):
        data = execute_dict('''
        SELECT * FROM inventory
        WHERE hero_id = (
            SELECT id FROM hero WHERE user_id=(?) AND active = 1
        ) AND item_id = (?)
        ''', (ctx.author.id, item_id))[0]
        
        
        if data["type"] == 1:
            equipment_type = "weapon_id"
        elif data["type"] == 2:
            equipment_type = "armor_id"
        else:
            return
        
        execute_dict(f'''
        UPDATE hero SET {equipment_type} = (?)
        WHERE id = (?)
        ''', (data["item_id"], data["hero_id"]))
        
        await ctx.send("Item equipped")
        
        
    @commands.command(name="add_all")
    async def add_all(self, ctx):
        hero_id = execute('''
        SELECT id FROM hero WHERE user_id=(?) AND active = 1
        ''', (ctx.author.id,))[0]
        
        for armor in armor_dict.values():
            armor = armor()
            execute('''
            INSERT INTO inventory (hero_id, type, item_id)
            VALUES (?,?,?)
            ''', (hero_id[0], armor.type_id, armor.id))
            
        for weapon in weapon_dict.values():
            weapon = weapon()
            execute('''
            INSERT INTO inventory (hero_id, type, item_id)
            VALUES (?,?,?)
            ''', (hero_id[0], weapon.type_id, weapon.id))
            
            
        await ctx.send("All items added to inventory")
        
        
    @commands.command(name="add_resources")
    async def add_resources(self, ctx):
        execute('''
        UPDATE hero SET 
        gold = 999999,
        wood = 999999,
        iron = 999999,
        runes = 999999
        WHERE user_id=(?)
        AND active = 1
        ''', (ctx.author.id,))
        await ctx.send("Resources added")

async def setup(bot):
    await bot.add_cog(Sqlite(bot))