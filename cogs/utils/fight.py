from discord.ext import commands
from discord import Embed
from discord.ui import Button, View
from discord import ButtonStyle
from cogs.game.characters import UserDummy, MagicDummy, AssasinDummy
from cogs.game.enemies import EnemyDummy
from cogs.game.weapons import WeaponKnife
from cogs.utils.lock_manager import LockManager  # Import LockManager


class NewFight():
    def __init__(self, ctx):
        self.ctx = ctx
        self.username = ctx.message.author.name
        self.view = View()
        
    async def fight(self, user, enemy, end=None):
        async def action_callback(interaction, user_action_name):
            if interaction.user != self.ctx.author:
                return
            await interaction.response.defer()
            await simulate_turn(user_action_name)
        
        def create_combat_embed(description="Choose your action:"):
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
        
        async def simulate_turn(user_action_name):
            action_function = user.abilities[user_action_name]
            combat_description =  f"`{self.username} used {user_action_name}!`\n"
            
            # Users attack
            combat_description += use_attack(enemy, action_function, user_action_name)

            # Message update
            await self.message.edit(embed=create_combat_embed(description=combat_description))
        
            # Check win
            if await fight_completed():
                if end:
                    end()
                return 
            
            # Enemy attack
            combat_description += use_attack(user, enemy.do_attack, "Hit")
            
            # Message update
            await self.message.edit(embed=create_combat_embed(description=combat_description))
        
            # Check win
            if await fight_completed():
                if end:
                    end()
                return 
            
        def use_attack(enemy : object, action, action_name : str) -> str:
            if message := action(enemy):
                return f"`{self.username} {message}`\n"
            else:
                return f"`{self.username} attempted to perform {action_name} but failed!`\n"


        async def fight_completed():
            if not user.is_alive():
                combat_description = f"`{enemy.name} wins!`\n"
                await self.message.edit(embed=create_combat_embed(description=combat_description), view=None)
                return True
            if not enemy.is_alive():
                combat_description = f"`{self.username} wins!`\n"
                await self.message.edit(embed=create_combat_embed(description=combat_description), view=None)
                return True
            return False
        
        
        
        for ability in user.abilities:
            button = Button(label=ability, style=ButtonStyle.primary)
            button.callback = lambda i, name=ability: action_callback(i, name)
            self.view.add_item(button)
            
        self.message = await self.ctx.send(embed=create_combat_embed(), view=self.view)

