from discord import Embed
from discord.ui import Button, View
from discord import ButtonStyle
from cogs.utils.progress import add_kill
import random

class NewFight():
    def __init__(self, inte):
        self.inte = inte
        self.username = inte.user.name
        self.view = View()
        
    async def fight(self, user, enemy, end=None):
        async def action_callback(interaction, user_action_name):
            if interaction.user != self.inte.user:
                return
            await interaction.response.defer()
            await simulate_turn(user_action_name)
        
        def create_combat_embed(description="Choose your action:"):
            embed = Embed(title="⚔️ COMBAT! ⚔️", description=description, color=0x3498db)  # Blue color
            embed.set_image(url=enemy.image)  # Example background

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
                    await end()
                return 
            
            # Enemy attack
            combat_description += enemy_turn(enemy, user)
            
            # Message update
            await self.message.edit(embed=create_combat_embed(description=combat_description))
        
            # Check win
            if await fight_completed():
                if end:
                    await end()
                return 
            
        def use_attack(enemy : object, action, action_name : str) -> str:
            if message := action(enemy):
                return f"`{self.username} {message}`\n"
            else:
                return f"`{self.username} attempted to perform {action_name} but failed!`\n"


        def enemy_turn(enemy, user):
            if enemy.ability:
                x = random.randint(1,2)
                if x == 1:
                    return use_attack(user, enemy.ability["func"], enemy.ability["name"])
            return use_attack(user, enemy.do_attack, "Hit")
            

        async def fight_completed():
            if not user.is_alive():
                combat_description = f"`{enemy.name} wins!`\n"
                await self.message.edit(embed=create_combat_embed(description=combat_description), view=None)
                return True
            if not enemy.is_alive():
                combat_description = f"`{self.username} wins!`\n"
                
                combat_description += enemy.loot.drop(self.inte.user.id)
                
                add_kill(self.inte.user.id)
                
                await self.message.edit(embed=create_combat_embed(description=combat_description), view=None)
                return True
            return False
        
        
        
        for ability in user.abilities:
            button = Button(label=ability, style=ButtonStyle.primary)
            button.callback = lambda i, name=ability: action_callback(i, name)
            self.view.add_item(button)
            
        self.message = await self.inte.original_response()
        await self.message.edit(embed=create_combat_embed(), view=self.view)
        



    async def multi_fight(self, users_data : list, enemy : object, end=None):
        async def action_callback(interaction, user_action_name, user_id):
            if interaction.user.id != user_id:
                return
            if self.button_message:
                await self.button_message.delete()
            await interaction.response.defer()
            await simulate_turn(interaction, user_action_name)
        
        def enemy_turn(enemy, user):
            if enemy.ability:
                x = random.randint(1,2)
                if x == 1:
                    return use_attack(user, enemy.ability["func"], enemy.ability["name"])
            return use_attack(user, enemy.do_attack, "Hit")
        
        def use_attack(enemy : object, action, action_name : str) -> str:
            if message := action(enemy):
                return f"`{self.username} {message}`\n"
            else:
                return f"`{self.username} attempted to perform {action_name} but failed!`\n"
        
        async def simulate_turn(interaction, user_action_name):
            
            if self.turn < len(users_data):
                user = users_data[self.turn][1]
                
                action_function = user.abilities[user_action_name]
                combat_description =  f"`{interaction.user.name} used {user_action_name}!`\n"
                
                # Users attack
                combat_description += use_attack(enemy, action_function, user_action_name)

                # Message update
                await self.message.edit(embed=create_combat_embed(user, description=combat_description))
            
                # Check win
                if enemy.hp <= 0:
                    if end:
                        await end()
                        
                    combat_description = f"`{self.username} wins!`\n"
                    for user_data in users_data:
                        combat_description += enemy.loot.drop(user_data[0])
                        add_kill(user_data[0])
                    
                        
                    
                    await self.message.edit(embed=create_combat_embed(user, description=combat_description), view=None)
                    return 
                
                self.turn += 1
                
                if self.turn >= len(users_data):
                    await self.message.edit(embed=create_combat_embed(users_data[0][1], description=combat_description), view=None)
                    await simulate_turn(interaction, user_action_name)
                else:

                    await self.message.edit(embed=create_combat_embed(users_data[self.turn][1], description=combat_description))
                    await send_turn_message()
                
            else:
                
                user = users_data[0][1]
            
                # Enemy attack
                combat_description = enemy_turn(enemy, user)
                
                # Message update
                await self.message.edit(embed=create_combat_embed(user, description=combat_description))
            
                # Check win
                if user.hp <= 0:
                    if end:
                        await end()
                    combat_description += f"{user.name} has fainted"
                    users_data.pop(0)
                    buttons.pop(0)
                    if not users_data:
                        combat_description += "enemy has won"
                        await self.message.edit(embed=create_combat_embed(user, description=combat_description))
                        return
                
                self.turn = 0
                
            
                    
                await self.message.edit(embed=create_combat_embed(users_data[self.turn][1], description=combat_description), view=None)
                await send_turn_message()
            
            
            
        def create_combat_embed(user, description="Choose your action:"):
            embed = Embed(title="⚔️ COMBAT! ⚔️", description=description, color=0x3498db)  # Blue color
            embed.set_image(url=enemy.image)

            # First line: user's HP and Mana
            embed.add_field(name=f"{self.username} HP", value=f"❤️ {user.hp}", inline=True)
            embed.add_field(name=f"{self.username} Mana", value=f"🔮 {user.mana}", inline=True)
            embed.add_field(name="\u200b", value="\u200b", inline=True)  # empty field to align correctly

            # Second line: enemy's HP and Mana
            embed.add_field(name=f"👹 {enemy.name} HP", value=f"❤️ {enemy.hp}", inline=True)
            embed.add_field(name=f"👹 {enemy.name} Mana", value=f"🔮 {enemy.mana}", inline=True)
            embed.add_field(name="\u200b", value="\u200b", inline=True)  # empty field to align correctly

            return embed
        
        
        async def send_turn_message():
            
            
            view = View()
            for ability in buttons[self.turn]:
                view.add_item(ability)
            
            self.button_message = await users_data[self.turn][2].followup.send("Select an ability", ephemeral=True, view=view)
        
        
        buttons = []
        
        for user in users_data:
            temp = []
            for ability in user[1].abilities:
                button = Button(label=ability, style=ButtonStyle.primary)
                button.callback = lambda i, name=ability, user_id=user[0]: action_callback(i, name, user_id)
                temp.append(button)
                
            buttons.append(temp.copy())
            
        self.button_message = None
        self.turn = 0
        view = View()
        
        await self.inte.response.send_message(embed=create_combat_embed(users_data[0][1]), view=view)
        self.message = await self.inte.original_response()
        await send_turn_message()
        
        
        
        
        
        
        
    async def consecutive_fight(self, user, enemys : list, end=None):
        if not enemys:
            if end:
                await end()
            message = await self.inte.original_response()
            await message.edit(embed = Embed(title="⚔️ COMBAT! ⚔️", description="Expedition ended succesfully", color=0x3498db))
            return
        enemy = enemys.pop()
        await self.fight(user,enemy,end=lambda user=user, enemys=enemys, end=end : self.consecutive_fight(user, enemys, end=end))
        
        
        
        
        
        
        
        
        
        
    
    async def pvp_fight(self, users_data : list, end=None):
        async def action_callback(interaction, user_action_name, user_id, hero, enemy):
            if interaction.user.id != user_id:
                return
            if self.button_message:
                await self.button_message.delete()
            await interaction.response.defer()
            await simulate_turn(interaction, user_action_name, hero, enemy)
        
        def use_attack(enemy : object, action, action_name : str) -> str:
            if message := action(enemy):
                return f"`{self.username} {message}`\n"
            else:
                return f"`{self.username} attempted to perform {action_name} but failed!`\n"
        
        async def simulate_turn(interaction, user_action_name, user, enemy):
            
            action_function = user.abilities[user_action_name]
            combat_description =  f"`{interaction.user.name} used {user_action_name}!`\n"
            
            # Users attack
            combat_description += use_attack(enemy, action_function, user_action_name)
            
            # Message update
            await self.message.edit(embed=create_combat_embed(user, enemy, description=combat_description))
            
            # Check win
            if enemy.hp <= 0:
                if end:
                    await end()
                    
                combat_description = f"`{self.username} wins!`\n"
                
                await self.message.edit(embed=create_combat_embed(user, enemy, description=combat_description), view=None)
                return 

            if self.turn_id == 0:
                self.turn_id = 1
            else:
                self.turn_id = 0

            await self.message.edit(embed=create_combat_embed(enemy, user, description=combat_description))
            await send_turn_message()
            
            
            
        def create_combat_embed(user, enemy, description="Choose your action:"):
            embed = Embed(title="⚔️ COMBAT! ⚔️", description=description, color=0x3498db)  # Blue color

            # First line: user's HP and Mana
            embed.add_field(name=f"{self.username} HP", value=f"❤️ {user.hp}", inline=True)
            embed.add_field(name=f"{self.username} Mana", value=f"🔮 {user.mana}", inline=True)
            embed.add_field(name="\u200b", value="\u200b", inline=True)  # empty field to align correctly

            # Second line: enemy's HP and Mana
            embed.add_field(name=f"👹 {enemy.name} HP", value=f"❤️ {enemy.hp}", inline=True)
            embed.add_field(name=f"👹 {enemy.name} Mana", value=f"🔮 {enemy.mana}", inline=True)
            embed.add_field(name="\u200b", value="\u200b", inline=True)  # empty field to align correctly

            return embed
        
        
        async def send_turn_message():
            
            
            view = View()
            for ability in buttons[self.turn_id]:
                view.add_item(ability)
            
            self.button_message = await users_data[self.turn_id][2].followup.send("Select an ability", ephemeral=True, view=view)
        
        
        buttons = []
        
        turn_id = 0
        enemy_id = 1
        
        for user in users_data:
            temp = []
            for ability in user[1].abilities:
                button = Button(label=ability, style=ButtonStyle.primary)
                button.callback = lambda i, name=ability, user_id=user[0], hero=users_data[turn_id][1], enemy=users_data[enemy_id][1]: action_callback(i, name, user_id, hero, enemy)
                temp.append(button)
            
            turn_id = 1
            enemy_id = 0
                
            buttons.append(temp.copy())
            
        self.button_message = None
        view = View()
        self.turn_id = 0
        
        await self.inte.response.send_message(embed=create_combat_embed(users_data[0][1], users_data[1][1]), view=view)
        self.message = await self.inte.original_response()
        await send_turn_message()