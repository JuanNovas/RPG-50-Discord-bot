import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener el token del bot desde la variable de entorno
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!", intents= discord.Intents.all())

@bot.event
async def on_ready():
    await bot.load_extension("cogs.commands.hello")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
    print("Bot is ready")
        
@bot.tree.command(name="hello")
async def hello(interaction: discord.Integration):
    await interaction.response.send_message(f"Hey {interaction.user.mention} ! This is a slash command!")
    
@bot.tree.command(name="ping")
async def hello(interaction: discord.Integration):
    await interaction.response.send_message(f"Slash pong")
    

    
bot.run(TOKEN)

