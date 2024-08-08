import discord
from discord import app_commands, Embed, SelectOption
from discord.ext import commands
from discord.ui import View, Select
from cogs.utils.database import execute
from cogs.utils.hero_actions import load_hero
from cogs.game.characters.ability_info import abilities_embed

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="stats", description="Shows user stats")
    async def stats(self, inte):
        class Dropdown(Select):
            def __init__(self,stats_obj):
                
                self.stats_obj = stats_obj
                
                options = [
                    SelectOption(value=1, label=f"Stats", emoji='🧪'),
                    SelectOption(value=2, label=f"Abilities", emoji='🌀')
                ]
                
                    
                super().__init__(placeholder='Select page', min_values=1, max_values=1, options=options)
        
        
            async def callback(self, interaction):
                if interaction.user.id != inte.user.id:
                    return
                if self.values[0] == "1":
                    embed = self.stats_obj.load_stats(data, inte)
                elif self.values[0] == "2":
                    embed = self.stats_obj.load_ability_info(inte)
                message = await inte.original_response()
                await message.edit(embed=embed)
                await interaction.response.defer()
        
        
        data = execute('''
        SELECT * FROM hero WHERE user_id=(?) AND active = 1
        ''', (inte.user.id,))
        
        view = View()
        view.add_item(Dropdown(self))
        
        embed = self.load_stats(data, inte)

        await inte.response.send_message(embed=embed, view=view)
        
        
        
    def load_stats(self, data, inte):
        hero = load_hero(inte.user.id)

        xp_needed = round(6.5 * (1.5 ** hero.level))
        progress = data[0][4] / xp_needed
        filled_length = int(20 * progress)
        bar = '█' * filled_length + '-' * (30 - filled_length)
        bar = f'[{bar}] {data[0][4]}/{xp_needed} XP'

        embed = Embed(title=f"{inte.user.name}'s stats", color=discord.Color.blue())
        embed.add_field(name="Class 🏹", value=hero.classname, inline=True)
        embed.add_field(name="Level 📈", value=hero.level, inline=True)
        embed.add_field(name="XP 🧪", value=bar, inline=False)
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
        embed.add_field(name="Weapon 🗡️", value=hero.weapon.name if hero.weapon else "None", inline=True)
        embed.add_field(name="Armor 🛡️", value=hero.armor.name if hero.armor else "None", inline=True)
        
        embed.set_image(url=hero.image)
        
        embed.set_footer(text="Character Stats")
        
        return embed
    
    
    def load_ability_info(self, inte):
        hero = load_hero(inte.user.id)
        embed = abilities_embed(hero, inte)
        
        return embed
        
async def setup(bot):
    await bot.add_cog(Stats(bot))

