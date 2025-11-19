import os
import requests
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
