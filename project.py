import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()


def get_token():   
    TOKEN = os.getenv('DISCORD_TOKEN')
    if TOKEN == None:
        raise RuntimeError("The 'DISCORD_TOKEN' environment variable was not found. Please make sure it is set in your .env file.")
    return TOKEN
    
    
# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True


prefix = "!"  
bot = commands.Bot(command_prefix=prefix, intents=intents, help_command=None)


async def load_extensions():
        await load("cogs/commands/combat")
        await load("cogs/commands/equipment")
        await load("cogs/commands/heroes")
        await load("cogs/commands/resources")
        await load("cogs/commands/stats")
        await load("cogs/commands/help")
        await load("cogs/commands/zones")
        return True

async def load(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".py") and filename != "__init__.py":
            cog_name = folder.replace("/", ".").replace("\\",".") + "." + filename[:-3]
            await bot.load_extension(cog_name)
            
    return True


@bot.event
async def on_ready():
    print("Loading")
    await load_extensions()
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
    print(f'{bot.user.name} has connected to Discord!')
    
def main():
    TOKEN = get_token()
    bot.run(TOKEN)
    
if __name__ == "__main__":
    main()