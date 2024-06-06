import discord
import sqlite3
from discord.ext import commands
import os
from dotenv import load_dotenv
from cogs.utils.lock_manager import LockManager

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
lock_manager = LockManager() # command lock 

# if user sends a message and is currently using a command, this message appears.
@bot.event
async def on_command(ctx):
    user_id = ctx.author.id
    if lock_manager.is_locked(user_id):
        await ctx.send("You are currently busy with another command. Please wait until it finishes.")
        raise commands.CommandError("User is busy")

# when the command is completed, the bot unlocks.
@bot.event
async def on_command_completion(ctx):
    user_id = ctx.author.id
    if lock_manager.is_locked(user_id):
        lock_manager.unlock(user_id)

# Cargar la extensión
async def load_extensions():
        await load("cogs/commands")
        #await load("cogs/utils/utilcogs")

async def load(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".py") and filename != "__init__.py":
            cog_name = folder.replace("/", ".").replace("\\",".") + "." + filename[:-3]
            await bot.load_extension(cog_name)

# Evento de inicio del bot
@bot.event
async def on_ready():
    await load_extensions()
    print(f'{bot.user.name} has connected to Discord!')

# Iniciar el bot
bot.run(TOKEN)

