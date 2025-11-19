import discord
from discord.ext import commands
from services.proxmox import *

class ProxMox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="vmstatus", description="Gets the status of a VM by its ID")
    async def proxmox_command(self, interaction: discord.Interaction, value: int):
        vm_status = await get_vm_detailed_status(value)
        embed = discord.Embed(
            title="VM Status",
            description=vm_status,
            color=discord.Color.orange()
        )
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(ProxMox(bot))