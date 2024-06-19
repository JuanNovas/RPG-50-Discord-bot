from discord.ext import commands
from discord import app_commands, Interaction, ButtonStyle, Embed
from discord.ui import View, Button
from cogs.utils.database import execute_dict
from cogs.game.items.weapons import weapon_dict
from cogs.game.items.armors import armor_dict


class Forge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='forge', description="Equipment Upgrades")
    async def forge(self, inte):

        def create_embed(page):
            embed = Embed(title="Forge", description="Select an item to Upgrade", color=0x3498db)
            for i, item in enumerate(page):
                if item['type'] == "armor":
                    dict = armor_dict
                elif item["type"] == "weapon":
                    dict = weapon_dict
                embed.add_field(name=f"{i+1} {dict[item['item_id']].__name__}", value=f"Level: {item['level']}")
            return embed

        async def back(interaction):
            if self.page >= 1:
                self.page -= 1
                await create_message(self.pages[self.page])
            await interaction.response.defer()

        async def forward(interaction):
            if len(self.pages) > self.page + 1:
                self.page += 1
                await create_message(self.pages[self.page])
            await interaction.response.defer()

        async def create_message(page):
            view = View()  # Create a new view every time to reset buttons
            embed = create_embed(page)

            button_back = Button(label="<<", style=ButtonStyle.primary)
            button_back.callback = back
            view.add_item(button_back)
            
            # Create item buttons
            for i in range(len(page)):
                button = Button(label=f"{i+1}", style=ButtonStyle.primary)
                view.add_item(button)
                
            button_forward = Button(label=">>", style=ButtonStyle.primary)
            button_forward.callback = forward
            view.add_item(button_forward)

            if self.message:
                await self.message.edit(embed=embed, view=view)
            else:
                await inte.response.send_message(embed=embed, view=view)
                self.message = await inte.original_response()

        PER_PAGE = 5
        self.page = 0
        self.message = None
        data = execute_dict('''
        SELECT type, level, item_id FROM clean_inventory
        WHERE user_id = (?)
        ''', (inte.user.id,))
        self.pages = [data[i:i + PER_PAGE] for i in range(0, len(data), PER_PAGE)]

        await create_message(self.pages[0])

async def setup(bot):
    await bot.add_cog(Forge(bot))