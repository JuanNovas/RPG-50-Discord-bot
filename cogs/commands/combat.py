from discord.ext import commands
from discord import Embed
from discord.ui import Button, View
from discord import ButtonStyle 
from cogs.game.characters import UserDummy
from cogs.game.enemies import EnemyDummy

class Combat(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command(name="combat")
    async def fight(self, ctx):
        user = UserDummy()
        enemy = EnemyDummy()

        def create_combat_embed():
            embed = Embed(title="COMBAT!", description="choose your action:", color=0xADD8E6)
            embed.add_field(name=f"{user.name} HP", value=user.hp, inline=True)
            embed.add_field(name=f"{enemy.name} HP", value=enemy.hp, inline=True)
            embed.add_field(name=f"{user.name} Mana", value=user.mana, inline=True)
            embed.add_field(name=f"{enemy.name} Mana", value=enemy.mana, inline=True)
            return embed

        view = View()

        async def attack_callback(interaction):
            if interaction.user != ctx.author:
                return
            
            damage = user.do_attack(enemy)
            if not enemy.is_alive():
                embed = Embed(title="COMBAT!", description=f"{user.name} wins!", color=0x00FF00)
                await interaction.response.edit_message(embed=embed, view=None)
                return

            enemy_damage = enemy.do_attack(user)
            if not user.is_alive():
                embed = Embed(title="COMBAT!", description=f"{enemy.name} wins!", color=0xFF0000)
                await interaction.response.edit_message(embed=embed, view=None)
                return
            
            await interaction.response.edit_message(embed=create_combat_embed(), view=view)

        attack_button = Button(label="Attack", style=ButtonStyle.primary)
        attack_button.callback = attack_callback

        view.add_item(attack_button)

        await ctx.send(embed=create_combat_embed(), view=view)

async def setup(bot):
    await bot.add_cog(Combat(bot))