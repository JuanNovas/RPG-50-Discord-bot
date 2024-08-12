from discord import app_commands, SelectOption
from discord.ext import commands
from discord.ui import View, Select
from cogs.game.zones.embeds import get_zone_embed
from cogs.utils.database import execute_dict
from cogs.utils.hero_check import hero_created
from cogs.utils.hero_actions import load_hero

class ChangeZone(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='change_zone', description="Selects a zone of the map")
    async def change_zone(self, inte):
        if not await hero_created(inte):
            return
        
        hero = load_hero(inte.user.id)
        
        class Dropdown(Select):
            def __init__(self):
                
                options = [
                    SelectOption(value=1, label=f"Train camp", emoji='🏕️')
                ]
                
                if hero.level >= 10:
                    options.append(SelectOption(value=2, label=f"Dungeon", emoji='⛓️'))
                    if hero.level >= 20:
                        options.append(SelectOption(value=3, label=f"Forest", emoji='🌲'))
                        if hero.level >= 25:
                            options.append(SelectOption(value=4, label=f"Desert", emoji='🏜️'))
                            if hero.level >= 35:
                                options.append(SelectOption(value=4, label=f"Desert", emoji='🏜️'))
                            else:
                                options.append(SelectOption(value=0, label=f"A new zone will be unlocked at level 35", emoji='🔒'))
                        else:
                            options.append(SelectOption(value=0, label=f"A new zone will be unlocked at level 25", emoji='🔒'))
                    else:
                        options.append(SelectOption(value=0, label=f"A new zone will be unlocked at level 20", emoji='🔒'))
                else:
                    options.append(SelectOption(value=0, label=f"A new zone will be unlocked at level 10", emoji='🔒'))
                    
                super().__init__(placeholder='Select a zone', min_values=1, max_values=1, options=options)
        
        
            async def callback(self, interaction):
                if interaction.user.id != inte.user.id:
                    return
                zone_id = int(self.values[0])
                if zone_id == 0:
                    return await interaction.response.defer()
                message = await inte.original_response()
                await message.edit(embed=get_zone_embed(zone_id))
                execute_dict('''
                UPDATE hero SET zone_id = (?) WHERE active = 1 AND user_id = (?)
                ''', (zone_id, inte.user.id))
                await interaction.response.defer()
              
        
        data = execute_dict('''
        SELECT zone_id FROM hero WHERE active = 1 AND user_id = (?)
        ''', (inte.user.id,))[0]
                
                
        view = View()
        view.add_item(Dropdown())

        

        await inte.response.send_message('Select a zone to go:', view=view, embed=get_zone_embed(data["zone_id"]))

async def setup(bot):
    await bot.add_cog(ChangeZone(bot))