from discord.ext import commands
from discord import app_commands, Interaction, ButtonStyle, Embed
from discord.ui import View, Button

class Paginator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.page = 0
        self.message = None

    @app_commands.command(name='paginator', description="Muestra 5 objetos por página y permite cambiar de página")
    async def paginator(self, inte: Interaction):

        def create_embed(page):
            embed = Embed(title="Forge", description="Select an item to Upgrade", color=0x3498db)
            for item in page:
                embed.add_field(name=item, value="Level X")
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
            for item in page:
                button = Button(label=f"item:{item}", style=ButtonStyle.primary)
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
        items = range(56)
        self.pages = [items[i:i + PER_PAGE] for i in range(0, len(items), PER_PAGE)]

        await create_message(self.pages[0])

async def setup(bot):
    await bot.add_cog(Paginator(bot))
