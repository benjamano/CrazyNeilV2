class MCServerStatusDTO:
    def __init__(self, online_players: int, max_players: int, latency: float, status: str, player_list: list[str], vm_status: str):
        self.online_players = online_players
        self.max_players = max_players
        self.latency = latency
        self.status = status
        self.player_list = player_list
        self.vm_status = vm_status

    def __str__(self):
        return f"""
            - Status: {self.status}
            \n - Machine Status: {self.vm_status}
            \n - Players: {self.online_players}/{self.max_players}
            \n - Latency: {self.latency}ms
            \n - Online Players: {', '.join(self.player_list) if self.player_list else 'None'}
        """
        
class VMStatusDTO:
    def __init__(self, vmid: int, name: str, status: str, cpu_usage: float, memory_usage: int, uptime: int):
        self.vmid = vmid
        self.name = name
        self.status = status
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage
        self.uptime = uptime
        
    def __str__(self):
        hours, remainder = divmod(self.uptime, 3600)
        minutes, seconds = divmod(remainder, 60)
        if hours > 0:
            uptime_str = f"{hours}:{minutes:02d}:{seconds:02d}"
        else:
            uptime_str = f"{minutes}:{seconds:02d}"
        
        if self.memory_usage >= 1024**3:  # GB
            memory_str = f"{self.memory_usage / (1024**3):.2f} GB"
        else: 
            memory_str = f"{self.memory_usage / (1024**2):.2f} MB"
        
        return f"""
            - VM ID: {self.vmid}
            \n - Name: {self.name}
            \n - Status: {self.status}
            \n - CPU Usage: {(self.cpu_usage*100):.1f}%
            \n - Memory Usage: {memory_str}
            \n - Uptime: {uptime_str}
        """