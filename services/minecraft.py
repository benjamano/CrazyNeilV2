import os
import requests
from dotenv import load_dotenv
load_dotenv("../.env")

apiAddress = str(os.getenv("API_HOST"))

async def get_online_players() -> list[str]:
    playerNames = []
    
    try:
        status = requests.get(f"http://{apiAddress}/minecraft/playerlist").json()
        if status["players"] is not None:
            for player in status["players"]:
                playerNames.append(player)
    except Exception as e:
        print(f"Error fetching player names: {e}")
        playerNames.append("Could not fetch player names")

    return playerNames