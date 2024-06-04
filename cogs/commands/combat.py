from discord.ext import commands
from discord import Embed
from discord.ui import Button, View
from discord import ButtonStyle
import asyncio
from cogs.game.characters import UserDummy
from cogs.game.enemies import EnemyDummy
from cogs.game.weapons import WeaponKnife

class Combat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.message = None
    
    def create_combat_embed(self, user, enemy, description="Choose your action:"):
        embed = Embed(title="COMBAT!", description=description, color=0xADD8E6)
        embed.add_field(name=f"{user.name} HP", value=user.hp, inline=True)
        embed.add_field(name=f"{enemy.name} HP", value=enemy.hp, inline=True)
        embed.add_field(name=f"{user.name} Mana", value=user.mana, inline=True)
        embed.add_field(name=f"{enemy.name} Mana", value=enemy.mana, inline=True)
        return embed

    async def perform_action(self, ctx, user, enemy, action_name):
        functions = {
            "Attack" : user.do_attack,
            "Weapon attack" : user.weapon_attack,
            "Heal" : user.heal
            # add functions here
        }

        action_function = functions.get(action_name)
        combat_description = f"`{user.name} used {action_name}!`\n"
        if message := action_function(enemy):
            combat_description += f"`{message}`\n"
        else: 
            combat_description += f"`{user.name} attempted to perform {action_name} but failed!`\n"

        message = await ctx.channel.fetch_message(self.message.id)
        await message.edit(embed=self.create_combat_embed(user, enemy, description=combat_description))

        if not enemy.is_alive():
            combat_description += f"`\n{user.name} wins!`"

        message = enemy.do_attack(user)
        combat_description += f"`{message}`\n"

        if not user.is_alive():
            combat_description += f"`\n{enemy.name} wins!`"

        message = await ctx.channel.fetch_message(self.message.id)
        await message.edit(embed=self.create_combat_embed(user, enemy, description=combat_description))


    @commands.command(name="combat")
    async def fight(self, ctx):
        user = UserDummy()
        enemy = EnemyDummy()
        user.equip(WeaponKnife())

        view = View()

        async def action_callback(interaction, action_name):
            if interaction.user != ctx.author:
                return
            await interaction.response.defer()
            await self.perform_action(self.message, user, enemy, action_name)

        actions = ["Attack", "Weapon attack", "Heal"]

        for action in actions:
            button = Button(label=action, style=ButtonStyle.primary)
            button.callback = lambda i, name=action: action_callback(i, name)
            view.add_item(button)
            
        self.message = await ctx.send(embed=self.create_combat_embed(user, enemy), view=view)

async def setup(bot):
    await bot.add_cog(Combat(bot))



