from discord import Embed
from discord.ui import Button, View
from discord import ButtonStyle
from cogs.utils.progress import add_kill
from cogs.utils.hero_actions import see_enemy
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

            embed = Embed(title="⚔️ COMBAT! ⚔️", description=description, color=0x3498db)
            embed.set_image(url=enemy.image)

            # User stats
            embed.add_field(name=f"{self.username}",
                            value=f"**LEVEL:** 📈 {user.level}\n**HP:** ❤️ {user.hp}\n**Mana:** 🔮 {user.mana}",
                            inline=True)
            embed.set_thumbnail(url=user.image)

            # Enmy stats
            embed.add_field(name=f"{enemy.name}",
                            value=f"**LEVEL:** 📈 {enemy.level}\n**HP:** ❤️ {enemy.hp}\n**Mana:** 🔮 {enemy.mana}",
                            inline=True)



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
            
        def use_attack(enemy: object, action, action_name: str, name: str = self.username) -> str:
            if message := action(enemy):
                return f"`{name} {message}`\n"
            else:
                return f"`{name} attempted to perform {action_name} but failed!`\n"


        def enemy_turn(enemy, user):
            if enemy.ability["cost"] <= enemy.mana:
                x = random.randint(1,2)
                if x == 1:
                    return use_attack(user, enemy.ability["func"], enemy.ability["name"], name=enemy.name)
            return use_attack(user, enemy.do_attack, "Hit")
            

        async def fight_completed():
            if not user.is_alive():
                combat_description = f"`{enemy.name} wins!`\n"
                self.winner = False
                await self.message.edit(embed=create_combat_embed(description=combat_description), view=None)
                return True
            if not enemy.is_alive():
                combat_description = f"`{self.username} wins!`\n"
                self.winner = True
                combat_description += f"`{enemy.loot.drop(self.inte.user.id, name=self.inte.user.name)}`\n"
                
                add_kill(self.inte.user.id)
                
                await self.message.edit(embed=create_combat_embed(description=combat_description), view=None)
                return True
            return False
        
        see_enemy(self.inte.user.id, enemy.id)
        
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
            if enemy.ability["cost"] <= enemy.mana:
                x = random.randint(1,2)
                if x == 1:
                    return use_attack(user, enemy.ability["func"], enemy.ability["name"], enemy.name)
            return use_attack(user, enemy.do_attack, "Hit", enemy.name)
        
        def use_attack(enemy : object, action, action_name : str, name: str) -> str:
            if message := action(enemy):
                return f"`{name} {message}`\n"
            else:
                return f"`{name} attempted to perform {action_name} but failed!`\n"
        
        async def simulate_turn(interaction, user_action_name):
            
            if self.turn < len(users_data):
                user = users_data[self.turn][1]
                
                action_function = user.abilities[user_action_name]
                combat_description =  f"`{interaction.user.name} used {user_action_name}!`\n"
                
                # Users attack
                combat_description += use_attack(enemy, action_function, user_action_name, user.name)

                # Message update
                await self.message.edit(embed=create_combat_embed(user, description=combat_description))
            
                # Check win
                if enemy.hp <= 0:
                    if end:
                        await end()
                        
                    combat_description = f"`{self.username} wins!`\n"
                    for user_data in users_data:
                        combat_description += f"`{enemy.loot.drop(user_data[0], name=user_data[1].name)}`\n"
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
                    combat_description += f"`{user.name} has fainted`\n"
                    users_data.pop(0)
                    buttons.pop(0)
                    if not users_data:
                        combat_description += "`enemy has won`"
                        await self.message.edit(embed=create_combat_embed(user, description=combat_description))
                        return
                
                self.turn = 0
                
            
                    
                await self.message.edit(embed=create_combat_embed(users_data[self.turn][1], description=combat_description), view=None)
                await send_turn_message()
            
            
            
        def create_combat_embed(userx, description="Choose your action:"):
            embed = Embed(title="⚔️ COMBAT! ⚔️", description=description, color=0x3498db)
            embed.set_image(url=enemy.image)

            for i, user in enumerate(users_data):
                if i == self.turn:
                    turn = "➡️ "
                else:
                    turn = ""
                # User stats
                user = user[1]
                embed.add_field(name=f"{turn}{user.name}",
                                value=f"**LEVEL:** 📈 {user.level}\n**HP:** ❤️ {user.hp}\n**Mana:** 🔮 {user.mana}",
                                inline=True)

            embed.set_thumbnail(url=userx.image)
            embed.add_field(name="\u200b", value="\u200b", inline=False)

            # Enmy stats
            embed.add_field(name=f"{enemy.name}",
                            value=f"**LEVEL:** 📈 {enemy.level}\n**HP:** ❤️ {enemy.hp}\n**Mana:** 🔮 {enemy.mana}",
                            inline=True)
            
            return embed
        
        
        async def send_turn_message():
            
            
            view = View()
            for ability in buttons[self.turn]:
                view.add_item(ability)
            
            self.button_message = await users_data[self.turn][2].followup.send("Select an ability", ephemeral=True, view=view)
        
        
        buttons = []
        
        for user in users_data:
            temp = []
            see_enemy(user[0], enemy.id)
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
        
        
        
        
        
        
        
    async def consecutive_fight(self, user, enemys : list, bonus=None, end=None):
        if not enemys:
            if end:
                await end()
            message = await self.inte.original_response()
            if self.winner:
                description = "Dungeon ended succesfully!\n"
                if bonus:
                    description += bonus.drop(self.inte.user.id, name=self.username)
            elif not self.winner:
                description = "Dungeon failed."
            await message.edit(embed = Embed(title="⚔️ COMBAT! ⚔️", description=description, color=0x3498db))
            return
        enemy = enemys.pop()
        self.view = View()
        await self.fight(user,enemy,end=lambda user=user, enemys=enemys,bonus=bonus, end=end : self.consecutive_fight(user, enemys, bonus=bonus, end=end))
        
        
        
        
        
        
        
        
        
        
    
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
            
            
            
        def create_combat_embed(userx, enemyx, description="Choose your action:"):
            embed = Embed(title="⚔️ COMBAT! ⚔️", description=description, color=0x3498db)
            user = users_data[0][1]
            enemy = users_data[1][1]
            if self.turn_id == 0:
                user_turn = "➡️ "
                enemy_turn = ""
                embed.set_thumbnail(url=user.image)
                embed.set_image(url=enemy.image)
            else:
                user_turn = ""
                enemy_turn = "➡️ "
                embed.set_thumbnail(url=enemy.image)
                embed.set_image(url=user.image)

            # User stats
            embed.add_field(name=f"{user_turn}{user.name}",
                            value=f"**LEVEL:** 📈 {user.level}\n**HP:** ❤️ {user.hp}\n**Mana:** 🔮 {user.mana}",
                            inline=True)

            # Enmy stats
            embed.add_field(name=f"{enemy_turn}{enemy.name}",
                            value=f"**LEVEL:** 📈 {enemy.level}\n**HP:** ❤️ {enemy.hp}\n**Mana:** 🔮 {enemy.mana}",
                            inline=True)



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