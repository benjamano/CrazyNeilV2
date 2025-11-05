import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from services.minecraft import send_message_to_server
from utils.tasks import startTasks

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and not filename.startswith("_"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded cog: {filename}")

class Bot(commands.Bot):
    async def setup_hook(self):
        await load_cogs()
        self.add_command(Help)
        await self.tree.sync()

@commands.command()
async def Help(ctx):
    embed = discord.Embed(
        title="Help - List of Commands",
        description="""
        **oioi help** - Show this help message
        **oioi OnlinePlayers** - List the currently online server players
        **oioi Playtime** - Show playtime of server's players today
        """,
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

bot = Bot(command_prefix="oioi ", intents=intents, activity=discord.Game(name="Back from the Dead! oioi help for commands", status=discord.Status.online), help_command=None, case_insensitive=True)

@bot.event
async def on_ready():
    startTasks(bot)
    if bot.user:
        print(f"Logged in as {bot.user.name}")

        await send_message_to_server("§b§lCrazy Neil §r§ais Watching...")

bot.run(str(os.getenv("DISCORD_TOKEN")))