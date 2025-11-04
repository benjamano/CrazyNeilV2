import os
import discord
from dotenv import load_dotenv
from discord.ext import tasks
from itertools import cycle
from services.minecraft import *

load_dotenv()

statuses = cycle(str(os.getenv("BOT_STATUSES")).split(","))

def startTasks(bot):
    changeStatus.start(bot)
    checkUserPlayTime.start(bot)

@tasks.loop(seconds=10)
async def changeStatus(bot):
    await bot.change_presence(activity=discord.Game(next(statuses)))

@tasks.loop(minutes=1)
async def checkUserPlayTime(bot):
    online_players = await get_online_players()

    for player in online_players:
        lines = []
        
        if os.path.exists("serverPlaytime.txt"):
            with open("serverPlaytime.txt", "r") as f:
                lines = f.readlines()

            with open("serverPlaytime.txt", "w") as f:
                found = False
                for line in lines:
                    if line.startswith(player + ":"):
                        parts = line.strip().split(":")
                        playtime = int(parts[1]) + 1
                        f.write(f"{player}:{playtime}\n")
                        found = True
                    else:
                        f.write(line)
                if not found:
                    f.write(f"{player}:1\n")
        else:
            with open("serverPlaytime.txt", "w") as f:
                f.write(f"{player}:1\n")
                
@tasks.loop(minutes=30)
async def verifyUserPlayTime(bot):
    playtime = await get_player_playtime_today()
    
    for entry in playtime:
        parts = entry.split(":")
        if len(parts) == 2:
            player = parts[0].strip()
            time = int(parts[1].strip().split()[0])
            if time >= 300:
                await send_message_to_server(f"§6§l[§c§lWARNING§6§l]§r §e{player}§r, you have been online for §c§l{time} minutes§r today! §a§oPlease consider taking a break and playing again tomorrow.§r §7- Crazy Neil")

@tasks.loop(time=discord.utils.utcnow().replace(hour=0, minute=0, second=0, microsecond=0).time())
async def resetPlayTime(bot):
    if os.path.exists("serverPlaytime.txt"):
        os.remove("serverPlaytime.txt")