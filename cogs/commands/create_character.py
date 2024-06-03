from discord.ext import commands
from discord import Embed
from discord.ui import Button, View
from discord import ButtonStyle  

class Create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# test
    @commands.command(name="create")
    async def create(self, ctx):
        
        # Each class with their picture 
        class_images = {
            "Warrior": "https://cdn.pixabay.com/photo/2023/08/18/15/02/dog-8198719_640.jpg",
            "🧙‍♂️ Magician": "https://cdn.pixabay.com/photo/2023/08/18/15/02/dog-8198719_640.jpg",
            "Thief": "https://cdn.pixabay.com/photo/2023/08/18/15/02/dog-8198719_640.jpg"
        }

        # sends a message and waits for an answer via buttons.
        embed = Embed(title=f"{ctx.message.author.name}, CHOOSE YOUR CLASS!", color=0xADD8E6, description="Click a button to choose your class")
        embed.set_image(url="https://cdn.discordapp.com/attachments/474702643625984021/1247263771811119224/72fcadcd-905e-4db7-9065-ea523ca7638d.jpg?ex=665f6468&is=665e12e8&hm=5fc58203fe3fcffae54347b6726480f49e84e1ff4828bc0b16c22b7be4328013&")
        
        #creates buttons 
        view = View()
        
        original_message = await ctx.send(embed=embed)

        for class_name, image_url in class_images.items():
            button = Button(label=class_name, style=ButtonStyle.primary)
            async def button_callback(interaction):
                if interaction.user != ctx.author:
                    return  # assure that the user is the same that started the command

                embed = Embed(title=f"{interaction.user}'s class", description="Character created _successfully_!", color=0xADD8E6)
                embed.add_field(name="Class:", value=class_name)
                embed.set_image(url=image_url)
                await interaction.response.send_message(embed=embed)
                await original_message.delete()  # delete original message
                button.callback = button_callback
                view.add_item(button)

            button.callback = button_callback
            view.add_item(button)

        await original_message.edit(view=view)

async def setup(bot):
    await bot.add_cog(Create(bot))