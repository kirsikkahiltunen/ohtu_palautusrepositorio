import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_palauttaa_oikean_pelaajan_tiedot(self):
        self.assertEqual(str(self.stats.search("Kurri")), 'Kurri EDM 37 + 53 = 90')
    
    def test_search_palauttaa_None_jos_pelaajaa_ei_loydy(self):
        self.assertEqual(self.stats.search("Selanne"), None)

    def test_team_palauttaa_joukkueen_jasenet_oikein(self):
        teams_players = self.stats.team("EDM")
        team  = []
        for player in teams_players:
            player = str(player)
            team.append(player)
        self.assertEqual(team, ['Semenko EDM 4 + 12 = 16', 'Kurri EDM 37 + 53 = 90', 'Gretzky EDM 35 + 89 = 124'])
    
    def test_top_palauttaa_pelaajat_paremmuusjarjestyksessa_tehopisteiden_perusteella(self):
        top_players = self.stats.top(2,1)
        top = []
        for player in top_players:
            player = str(player)
            top.append(player)
        self.assertEqual(top, ['Gretzky EDM 35 + 89 = 124', 'Lemieux PIT 45 + 54 = 99', 'Yzerman DET 42 + 56 = 98'])

    def test_top_palauttaa_pelaajat_paremmuusjarjestyksessa_maalien_perusteella(self):
        top_players = self.stats.top(2,2)
        top = []
        for player in top_players:
            player = str(player)
            top.append(player)
        self.assertEqual(top, ['Lemieux PIT 45 + 54 = 99', 'Yzerman DET 42 + 56 = 98', 'Kurri EDM 37 + 53 = 90'])

    def test_top_palauttaa_pelaajat_paremmuusjarjestyksessa_syottojen_perusteella(self):
        top_players = self.stats.top(2,3)
        top = []
        for player in top_players:
            player = str(player)
            top.append(player)
        self.assertEqual(top, ['Gretzky EDM 35 + 89 = 124', 'Yzerman DET 42 + 56 = 98', 'Lemieux PIT 45 + 54 = 99'])
    
    