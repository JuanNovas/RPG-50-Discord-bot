import discord
import asyncio
from discord.ext import commands
import os
from dotenv import load_dotenv

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

# Cargar la extensión
async def load_extensions():
        await load("cogs/commands")

async def load(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".py") and filename != "__init__.py":
            cog_name = folder.replace("/", ".").replace("\\",".") + "." + filename[:-3]
            await bot.load_extension(cog_name)

# Evento de inicio del bot
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Iniciar el bot
bot.run(TOKEN)

