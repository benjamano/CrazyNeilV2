import os
import requests
from utils.models import *
from dotenv import load_dotenv
load_dotenv(".env")

apiAddress = str(os.getenv("API_HOST"))

async def get_online_players() -> list[str]:
    playerNames = []
    
    try:
        status = requests.get(f"https://{apiAddress}/minecraft/playerlist").json()
        if status["players"] is not None:
            for player in status["players"]:
                playerNames.append(player)
    except Exception as e:
        print(f"Error fetching player names: {e}")
        playerNames.append("Could not fetch player names, error: " + str(e))

    return playerNames

async def get_playtime_for_date(date) -> list[str]:
    playerPlaytimes = []
    
    try:
        response = requests.get(f"https://{apiAddress}/minecraft/getplaytime?date={date}")
        data = response.json()
        
        if 'playtime' in data:
            for player, minutes in data['playtime'].items():
                playerPlaytimes.append(f"{player}: {minutes} minutes")
                    
    except Exception as e:
        print(f"Error fetching playtime data: {e}")
        playerPlaytimes.append("Could not fetch playtime data, error: " + str(e))

    return playerPlaytimes

async def get_server_status() -> MCServerStatusDTO:
    try:
        status = requests.get(f"https://{apiAddress}/minecraft/status").json()
        
        online_players = status.get("players_online", 0)
        max_players = status.get("max_players", 0)
        latency = status.get("latency", 0.0)
        server_status = "Online" if status.get("online", False) else "Offline"
        
        return MCServerStatusDTO(
            online_players=online_players,
            max_players=max_players,
            latency=latency,
            status=server_status
        )
    except Exception as e:
        print(f"Error fetching server status: {e}")
        return MCServerStatusDTO(
            online_players=[],
            max_players=0,
            latency=0.0,
            status="Error fetching status"
        )