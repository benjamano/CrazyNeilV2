import discord
from discord.ext import commands
from services.proxmox import *

class ProxMox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ServerLoad(self, ctx):
        server_load = await get_server_load()
        embed = discord.Embed(
            title="Server Load",
            description=f"Current server load: {server_load}%",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ProxMox(bot))