import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    FIN_players = filter(lambda player: player['nationality'] == 'FIN', response)
    FIN_players = list(FIN_players)
    #print(FIN_players)

    sorted_players = sorted(FIN_players,reverse=True,key=lambda player: player['goals'] + player['assists'])

    print(sorted_players)

    players = []

    for player_dict in sorted_players:
        player = Player(player_dict)
        players.append(player)

    print(players)

    print("Players from FIN \n\n")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()