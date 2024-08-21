from discord import app_commands, Embed, Color, SelectOption
from discord.ext import commands
from discord.ui import View, Select
from cogs.utils.help_embeds import get_help_embed

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='help', description="help command")
    async def help(self, inte):
        class Dropdown(Select):
            def __init__(self, selected_id=None):
                # Lista de opciones con los IDs correspondientes
                all_options = [
                    (0, "Introduction", '✨'),
                    (1, "Combat", '⚔️'),
                    (2, "Stats", '📊'),
                    (3, "Zones", '🌍'),
                    (4, "Equipment", '🛡️'),
                    (5, "Heroes", '🦸'),
                    (6, "Commerce", '💰')
                ]

                # Filtrar la opción seleccionada previamente
                options = [
                    SelectOption(value=str(option_id), label=label, emoji=emoji)
                    for option_id, label, emoji in all_options
                    if option_id != selected_id
                ]
                
                super().__init__(placeholder='Select commands to get info', min_values=1, max_values=1, options=options)
                self.selected_id = selected_id
        
            async def callback(self, interaction):
                if interaction.user.id != inte.user.id:
                    return

                # Obtener el ID seleccionado y convertirlo en un entero
                command_id = int(self.values[0])

                # Actualizar el mensaje con el nuevo embed y generar una nueva vista
                message = await inte.original_response()
                new_view = View()
                new_view.add_item(Dropdown(selected_id=command_id))
                await message.edit(embed=get_help_embed(command_id), view=new_view)
                await interaction.response.defer()

        # Crear la vista inicial con la opción predeterminada seleccionada (0 - Introduction)
        view = View()
        view.add_item(Dropdown(selected_id=0))

        await inte.response.send_message(embed=get_help_embed(0), view=view)

async def setup(bot):
    await bot.add_cog(Help(bot))
