from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

        self._players = self.reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = filter(lambda player: player['nationality'] == nationality, self._players)
        players = list(filtered_players)

        sorted_players = sorted(players,reverse=True,key=lambda player: player['goals'] + player['assists'])

        return sorted_players
