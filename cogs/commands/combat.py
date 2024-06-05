from discord.ext import commands
from discord import Embed
from discord.ui import Button, View
from discord import ButtonStyle
from cogs.game.characters import UserDummy, MagicDummy, AssasinDummy
from cogs.game.enemies import EnemyDummy
from cogs.game.weapons import WeaponKnife
from cogs.utils.lock_manager import LockManager  # Import LockManager

lock_manager = LockManager()  # Instantiate LockManager

class Combat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.message = None

    @commands.command(name="combat")
    async def fight(self, ctx):
        if lock_manager.is_locked(ctx.author.id):
            await ctx.send("`You are already in a combat.`")
            return
        
        lock_manager.lock(ctx.author.id)

        user = AssasinDummy()
        enemy = EnemyDummy()
        user.equip(WeaponKnife())
        self.username = ctx.message.author.name

        view = View()

        async def action_callback(interaction, action_name):
            if interaction.user != ctx.author:
                return
            await interaction.response.defer()
            await self.perform_action(ctx, user, enemy, action_name)

        actions = []
        for ability in user.abilities:
            actions.append(ability)

        for action in actions:
            button = Button(label=action, style=ButtonStyle.primary)
            button.callback = lambda i, name=action: action_callback(i, name)
            view.add_item(button)
            
        self.message = await ctx.send(embed=self.create_combat_embed(user, enemy), view=view)

    def create_combat_embed(self, user, enemy, description="Choose your action:"):
        embed = Embed(title="⚔️ COMBAT! ⚔️", description=description, color=0x3498db)  # Blue color
        embed.set_thumbnail(url="https://i.imgur.com/vpA37vR.png")  # Example thumbnail
        embed.set_image(url="https://i.imgur.com/aZ3qkZJ.jpg")  # Example background

        # First line: user's HP and Mana
        embed.add_field(name=f"{self.username} HP", value=f"❤️ {user.hp}", inline=True)
        embed.add_field(name=f"{self.username} Mana", value=f"🔮 {user.mana}", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)  # empty field to align correctly

        # Second line: enemy's HP and Mana
        embed.add_field(name=f"👹 {enemy.name} HP", value=f"❤️ {enemy.hp}", inline=True)
        embed.add_field(name=f"👹 {enemy.name} Mana", value=f"🔮 {enemy.mana}", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)  # empty field to align correctly

        return embed

    async def perform_action(self, ctx, user, enemy, action_name):
        action_function = user.abilities[action_name]
        combat_description = f"`{self.username} used {action_name}!`\n"
        if message := action_function(enemy):
            combat_description += f"`{self.username} {message}`\n"
        else:
            combat_description += f"`{self.username} attempted to perform {action_name} but failed!`\n"

        message = await ctx.channel.fetch_message(self.message.id)
        await message.edit(embed=self.create_combat_embed(user, enemy, description=combat_description))

        if not enemy.is_alive():
            combat_description += f"`{self.username} wins!`\n"
            message = await ctx.channel.fetch_message(self.message.id)
            await message.edit(embed=self.create_combat_embed(user, enemy, description=combat_description), view=None)
            lock_manager.unlock(ctx.author.id)  # Unlock after combat ends
            return

        message = enemy.do_attack(user)
        combat_description += f"`{message}`\n"

        if not user.is_alive():
            combat_description += f"`\n{enemy.name} wins!`"
            message = await ctx.channel.fetch_message(self.message.id)
            await message.edit(embed=self.create_combat_embed(user, enemy, description=combat_description), view=None)
            lock_manager.unlock(ctx.author.id)  # Unlock after combat ends
            return
        
        message = await ctx.channel.fetch_message(self.message.id)
        await message.edit(embed=self.create_combat_embed(user, enemy, description=combat_description))


async def setup(bot):
    await bot.add_cog(Combat(bot))
