import discord
from discord.ext import commands

classes = ['Warrior', 'Witcher', 'Paladin']

@commands.command()
async def create(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    username = ctx.message.author.name
    
    class_options = "\n".join([f"{i+1}. {cls}" for i, cls in enumerate(classes)])
    await ctx.send(f"Select your class:\n{class_options}")
    class_msg = await commands.wait_for('message', check=check)
    class_choice = int(class_msg.content) - 1

    if 0 <= class_choice < len(classes):
        clase = classes[class_choice]
        await ctx.send(f"{username}, {clase}")
    else:
        await ctx.send("Invalid option, please try again")
        create(ctx)