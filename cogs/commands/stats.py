import discord
from discord import app_commands, Embed
from discord.ext import commands
from cogs.utils.database import execute
from cogs.utils.stast_calculator import get_class_by_id

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="stats", description="Shows user stats")
    async def stats(self, inte):
        data = execute('''
        SELECT * FROM hero WHERE user_id=(?)
        ''', (inte.user.id,))
        
        hero_class = get_class_by_id(data[0][2])
        hero = hero_class(level=data[0][3])
        
        
        embed = Embed(title=f"{inte.user.name}'s stats", color=discord.Color.blue())
        embed.add_field(name="Class 🏹", value=hero.classname, inline=True)
        embed.add_field(name="Level 📈", value=hero.level, inline=True)
        embed.add_field(name="XP 🧪", value=data[0][4], inline=True)
        embed.add_field(name="Gold 💰", value=data[0][5], inline=True)
        embed.add_field(name="Wood 🌲", value=data[0][6], inline=True)
        embed.add_field(name="Iron ⛏️", value=data[0][7], inline=True)
        embed.add_field(name="Runes 🧿", value=data[0][8], inline=True)
        embed.add_field(name="HP ❤️", value=hero.hp, inline=True)
        embed.add_field(name="Attack ⚔️", value=hero.attack, inline=True)
        embed.add_field(name="Magic 🔮", value=hero.magic, inline=True)
        embed.add_field(name="Defense 🛡️", value=hero.defense, inline=True)
        embed.add_field(name="Magic Resistance ✨", value=hero.magic_resistance, inline=True)
        embed.add_field(name="Mana 🔵", value=hero.mana, inline=True)
        embed.add_field(name="Weapon 🗡️", value=hero.weapon, inline=True)
        embed.add_field(name="Armor 🛡️", value=hero.armor, inline=True)
        
        embed.set_image(url=hero.image)
        
        embed.set_footer(text="Character Stats")

        await inte.response.send_message(embed=embed)
            
        
async def setup(bot):
    await bot.add_cog(Stats(bot))