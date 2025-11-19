import discord
from discord.ext import commands
from discord import app_commands
from services.minecraft import *

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="onlineplayers", description="View online players")
    async def online_players(self, interaction: discord.Interaction):
        online_players = await get_online_players()
        embed = discord.Embed(
            title="Online Players",
            description="\n - ".join(online_players) if online_players else "No players online.",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Minecraft(bot))