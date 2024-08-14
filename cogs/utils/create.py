from cogs.utils.database import execute, execute_dict
from discord import Embed, ButtonStyle, Color
from discord.ui import Button, View
from cogs.game.characters.heros import *

async def create_hero(inte):
    async def callback(interaction, class_name, id):
        if interaction.user != inte.user:
            return  # assure that the user is the same that started the command


        data = execute('''
        SELECT * FROM hero WHERE user_id = (?) AND active = 1
        ''', (interaction.user.id,))
        if data == []:
            execute('''
            INSERT INTO hero (user_id, class, active) VALUES (?,?,1)
            ''', (interaction.user.id, id))
        else:
            execute('''
            INSERT INTO hero (user_id, class, active) VALUES (?,?,0)
            ''', (interaction.user.id, id))

        embed = Embed(title=f"{interaction.user}'s class", description="Hero created _successfully_!", color=0x1E90FF)
        embed.add_field(name="Class:", value=class_name)
        embed.set_image(url=class_images[class_name])
        original_message = await inte.original_response() # inte not interaction to get the last message
        await original_message.edit(embed=embed, view=None)
    
    # Each class with their picture 
    class_images = {
        "🧙‍♂️ Magician": MagicDummy().image,
        "🔪 Assasin": AssasinDummy().image,
        "🛡️ Tank": Tank().image
    }
    
    data = execute_dict('''
    SELECT DISTINCT class FROM hero WHERE user_id = (?) ORDER BY class
    ''',(inte.user.id,))
    clases_owned = [clas["class"] for clas in data]
    
    if len(clases_owned) == len(class_images):
        await inte.response.send_message("All hero types already created")
        return

    # sends a message and waits for an answer via buttons.
    embed = Embed(title=f"{inte.user.name}, CHOOSE YOUR CLASS!", color=Color.blue(), description="Click a button to choose your class")
    embed.set_image(url="https://cdn.discordapp.com/attachments/474702643625984021/1272664340142489600/DALLE_2024-08-12_18.13.40_-_A_fantasy_RPG_style_image_of_a_hero_standing_on_a_mountain_seen_from_the_back_holding_a_sword_and_looking_out_towards_a_distant_castle._The_hero_has.webp?ex=66bbcc87&is=66ba7b07&hm=aa8882e4b47cb20fbadfbad4164037a80bb696bb77776d0e7fba77daaea715a7&")
    
    #creates buttons
    view = View()
        
    for index, class_name in enumerate(class_images):
        if index+1 in clases_owned:
            continue
        button = Button(label=class_name, style=ButtonStyle.primary)
        
        button.callback = lambda i, class_name=class_name, id=index+1 : callback(i, class_name, id)
        view.add_item(button)

    await inte.response.send_message(embed=embed, view=view, ephemeral=True)