import discord
from datetime import datetime
from discord.ext import commands
from discord import app_commands
from services.minecraft import *
from services.proxmox import *

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

    @app_commands.command(name="playtime", description="View the playtime of online players today")
    async def playtime(self, interaction: discord.Interaction):
        online_players = await get_playtime_for_date(datetime.now().date())
        embed = discord.Embed(
            title="Online Players",
            description="\n - ".join(online_players) if online_players else "",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)
        
    @app_commands.command(name="serverstatus", description="View the status of the minecraft server")
    async def server_status(self, interaction: discord.Interaction):
        server_status = await get_server_status()
        embed = discord.Embed(
            title="Server Status",
            description=str(server_status),
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Minecraft(bot))