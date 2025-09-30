import discord
from discord.ext import commands
from services.minecraft import *

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def OnlinePlayers(self, ctx):
        online_players = await get_online_players()
        embed = discord.Embed(
            title="Online Players",
            description="\n".join(online_players) if online_players else "No players online.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)
        
    @commands.command()
    async def Playtime(self, ctx):
        online_players = await get_player_playtime_today()
        embed = discord.Embed(
            title="Player Playtimes",
            description="\n".join(online_players) if online_players else "No playtime data available.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Minecraft(bot))