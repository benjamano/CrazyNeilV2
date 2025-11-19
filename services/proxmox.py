import os
import requests
from utils.models import *
from dotenv import load_dotenv

load_dotenv(".env")

apiAddress = str(os.getenv("API_HOST"))

async def get_vm_status() -> str:
    vmStatus = ""
    
    try:
        status = requests.get(f"https://{apiAddress}/proxmox/getvmstatus?vmid={os.getenv("MCServerVMId")}").json()
        if status["status"] is not None:
            if (status["status"] == "running"):
                vmStatus = "VM is ONLINE"
            else:
                vmStatus = "VM is OFFLINE"
    except Exception as e:
        print(f"Error fetching VM status: {e}")
        vmStatus = "Could not fetch VM status, error: " + str(e)

    return vmStatus