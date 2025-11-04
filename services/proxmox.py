import os
from dotenv import load_dotenv
from proxmoxer import ProxmoxAPI

load_dotenv()

proxmoxHostAddress = str(os.getenv("PROXMOX_HOST_ADDRESS"))
proxmoxPassword = str(os.getenv("PROXMOX_PASSWORD"))

proxmox = ProxmoxAPI(
    proxmoxHostAddress, user="root@pam", password=proxmoxPassword, verify_ssl=False
)

async def get_server_load():
    node = proxmox.nodes.get("proxmox")
    if (node is not None):
        return node["status"]["cpu"]["load"]
    return None