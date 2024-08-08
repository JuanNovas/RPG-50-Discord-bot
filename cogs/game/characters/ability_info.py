import discord
from discord import Embed


def abilities_embed(hero: object, inte):
    embed = Embed(title=f"{inte.user.name}'s abilities", color=discord.Color.blue())
    embed.add_field(name="Class 🏹", value=hero.classname, inline=True)
    embed.add_field(name="Hit", value="**Punchs the enemy**\nPOWER: 10\nCOST: 0", inline=False)
    embed.set_image(url=hero.image)
    match hero.classname:
        case "Wizard":
            embed.add_field(name="Magic flame", value="**Deals fire attack**\nPOWER: 10\nCOST: 5", inline=False)
            if hero.level >= 10:
                embed.add_field(name="Heal", value="**Heals hp based in user Magic**\nCOST: 10", inline=False)
        case "Assasin":
            embed.add_field(name="Super hit", value="**Knifes the enemy**\nPOWER: 20\nCOST: 5", inline=False)
            if hero.level >= 10:
                embed.add_field(name="Sacrifice", value="**Sacrifices health for massive damage**\nPOWER: 35\nCOST: 10 HP", inline=False)
        case "Tank":
            embed.add_field(name="Smash", value="**Smashs the enemy**\nPOWER: 20\nCOST: 10", inline=False)
            if hero.level >= 10:
                embed.add_field(name="Reforce", value="**Increase the deffenses**\nCOST: 10", inline=False)
                
    
                
    return embed