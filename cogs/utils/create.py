from cogs.utils.database import execute
from discord import Embed, ButtonStyle
from discord.ui import Button, View

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
        "🧙‍♂️ Magician": "https://cdn.discordapp.com/attachments/474702643625984021/1249850968577933393/magicdummy2.jpeg?ex=6668cdec&is=66677c6c&hm=0d946dc04407fcc92df9ac02dada07f8090ef839b0a29b70958bd065a6b105e8&",
        "🔪 Assasin": "https://cdn.discordapp.com/attachments/474702643625984021/1249850320217964704/assasindummy2.jpeg?ex=6668cd51&is=66677bd1&hm=bdd64f0f8281af7d9bf29c6dd5c8ec879809a5296a5d122a0ee7d26972ed8e7e&",
        "🛡️ Tank": "https://cdn.discordapp.com/attachments/474702643625984021/1271109367076229170/DALLE_2024-08-08_11.14.42_-_A_fantasy_RPG_style_image_of_a_Tank_class_hero_in_a_medieval_training_field._The_hero_has_a_semi-realistic_appearance_with_heavy_armor_a_large_shield.webp?ex=66b62459&is=66b4d2d9&hm=13c260f3ff409466d40a100757753af705e8f615e330499ba18469eb50373f0c&"
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