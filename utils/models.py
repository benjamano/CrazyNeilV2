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