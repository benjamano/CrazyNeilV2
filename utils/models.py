class MCServerStatusDTO:
    def __init__(self, online_players: list[str], max_players: int, latency: float, status: str):
        self.online_players = online_players
        self.max_players = max_players
        self.latency = latency
        self.status = status

    def __str__(self):
        return f"""-
            - Status: {self.status}
            \n - Players: {len(self.online_players)}/{self.max_players}
            \n - Latency: {self.latency}ms
            \n - Online Players: {', '.join(self.online_players)}
        """