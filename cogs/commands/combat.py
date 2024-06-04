from discord.ext import commands
from discord import Embed
from discord.ui import Button, View
from discord import ButtonStyle
import asyncio
from cogs.game.characters import UserDummy
from cogs.game.enemies import EnemyDummy

class Combat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="combat")
    async def fight(self, ctx):
        user = UserDummy()
        enemy = EnemyDummy()

        def create_combat_embed(description="Choose your action:"):
            embed = Embed(title="COMBAT!", description=description, color=0xADD8E6)
            embed.add_field(name=f"{user.name} HP", value=user.hp, inline=True)
            embed.add_field(name=f"{enemy.name} HP", value=enemy.hp, inline=True)
            embed.add_field(name=f"{user.name} Mana", value=user.mana, inline=True)
            embed.add_field(name=f"{enemy.name} Mana", value=enemy.mana, inline=True)
            return embed

        view = View()

        async def attack_callback(interaction):
            if interaction.user != ctx.author:
                return

            # User's attack
            user_damage = user.do_attack(enemy)
            combat_description = f"`{user.name} attacked {enemy.name} for {user_damage} damage!`\n"

            if not enemy.is_alive():
                embed = create_combat_embed(description=combat_description + f"{user.name} wins!")
                await interaction.response.edit_message(embed=embed, view=None)
                return

            await interaction.response.edit_message(embed=create_combat_embed(description=combat_description), view=view)
            await asyncio.sleep(1)

            # Enemy's attack
            enemy_damage = enemy.do_attack(user)
            combat_description += f"`{enemy.name} attacked {user.name} for {enemy_damage} damage!`"

            if not user.is_alive():
                embed = create_combat_embed(description=combat_description + f"\n{enemy.name} wins!")
                await interaction.edit_original_response(embed=embed, view=None)
                return

            embed = create_combat_embed(description=combat_description)
            await interaction.edit_original_response(embed=embed, view=view)

        # Healing option

        async def heal_callback(interaction):
            if interaction.user != ctx.author:
                return

            if user.heal():
                combat_description = f"`{user.name} healed for 10 HP!`\n"
            else:
                combat_description = f"`{user.name} tried to heal but didn't have enough mana!`\n"

            await interaction.response.edit_message(embed=create_combat_embed(description=combat_description), view=view)
            await asyncio.sleep(1)

            # Enemy's attack after healing
            enemy_damage = enemy.do_attack(user)
            combat_description += f"`{enemy.name} attacked {user.name} for {enemy_damage:.2f} damage!`"

            if not user.is_alive():
                embed = create_combat_embed(description=combat_description + f"\n{enemy.name} wins!")
                await interaction.edit_original_response(embed=embed, view=None)
                return

            embed = create_combat_embed(description=combat_description)
            await interaction.edit_original_response(embed=embed, view=view)

        # Button style
        attack_button = Button(label="Attack", style=ButtonStyle.primary)
        attack_button.callback = attack_callback
        heal_button = Button(label="Heal", style=ButtonStyle.primary)
        heal_button.callback = heal_callback

        view.add_item(attack_button)
        view.add_item(heal_button)

        await ctx.send(embed=create_combat_embed(), view=view)

async def setup(bot):
    await bot.add_cog(Combat(bot))
