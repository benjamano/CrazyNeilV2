import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from mcstatus import JavaServer

load_dotenv()

serverAddress = str(os.getenv("MINECRAFT_SERVER_ADDRESS"))

server = JavaServer.lookup(serverAddress)

async def get_online_players():
    playerNames = []
    
    try:
        status = server.status()
        if status.players.sample is not None:
            for player in status.players.sample:
                playerNames.append(f"- {player.name}")
    except Exception as e:
        print(f"Error fetching player names: {e}")
        playerNames.append("Could not fetch player names")

    return playerNames

async def get_player_playtime_today():
    playtimes = []
    
    if os.path.exists("serverPlaytime.txt"):
        with open("serverPlaytime.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    player, time = parts
                    playtimes.append(f"- {player}: {time} minute(s)")

    return playtimes