from cogs.utils.database import execute
from discord import Embed, ButtonStyle
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

        embed = Embed(title=f"{interaction.user}'s class", description="Character created _successfully_!", color=0x1E90FF)
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

    # sends a message and waits for an answer via buttons.
    embed = Embed(title=f"{inte.user.name}, CHOOSE YOUR CLASS!", color=0xADD8E6, description="Click a button to choose your class")
    embed.set_image(url="https://cdn.discordapp.com/attachments/474702643625984021/1247263771811119224/72fcadcd-905e-4db7-9065-ea523ca7638d.jpg?ex=665f6468&is=665e12e8&hm=5fc58203fe3fcffae54347b6726480f49e84e1ff4828bc0b16c22b7be4328013&")
    
    #creates buttons
    view = View()
        
    for index, class_name in enumerate(class_images):
        button = Button(label=class_name, style=ButtonStyle.primary)
        
        button.callback = lambda i, class_name=class_name, id=index+1 : callback(i, class_name, id)
        view.add_item(button)

    await inte.response.send_message(embed=embed, view=view, ephemeral=True)