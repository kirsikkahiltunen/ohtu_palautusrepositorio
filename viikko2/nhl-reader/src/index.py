from rich import print
from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    def select():
        print("[cyan]Select nationality [AUT/CZE/AUS/SWE/GER/DEN/SUI/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR/]: [cyan]", end="")
        nationality = input()
        url = "https://studies.cs.helsinki.fi/nhlstats/"+season+"/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)
        playerlist=[]
        for player in players:
            playerlist.append(str(player))
        table(playerlist, nationality, season)
        select()

    def table(playerlist, nationality, season):
        table = Table(title=f"Players from {nationality} season {season}")

        table.add_column("name", style="cyan", no_wrap=True)
        table.add_column("team", style="magenta")
        table.add_column("goals", justify="right", style="green")
        table.add_column("assists", justify="right", style="green")
        table.add_column("points", justify="right", style="green")

        for player in playerlist:
            player_splitted=player.split(", ")
            table.add_row(player_splitted[0], player_splitted[1], player_splitted[2], player_splitted[3], player_splitted[4])

        console = Console()
        console.print(table, justify="center")

    print ("NHL statistics by nationality\n")
    print("[cyan]Select season [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/]: [/cyan]", end="")
    season = input()
    select()

if __name__ == "__main__":
    main()