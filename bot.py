import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from  cogs.commands.pong import ping
from cogs.commands.create_character import create
# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener el token del bot desde la variable de entorno
TOKEN = os.getenv('DISCORD_TOKEN')

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

# Configuración del bot
prefix = "!"  # Puedes cambiar el prefijo del bot aquí si lo deseas
bot = commands.Bot(command_prefix=prefix, intents=intents)

# Evento de inicio del bot
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.add_command(ping)
bot.add_command(create)

# Iniciar el bot
bot.run(TOKEN)
