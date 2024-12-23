import unittest
from unittest.mock import Mock, ANY
from kassapaate import Kassapaate, HINTA
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo.return_value = 10
        
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo.return_value = 4
        
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_not_called()

    def test_lataa_lisaa_maksukortille_ladattavan_summan_jos_se_on_positiivinen(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo.return_value = 10

        self.kassa.lataa(maksukortti_mock, 5)

        maksukortti_mock.lataa.assert_called_with(5)

    def test_lataa_ei_tee_maksukortille_mitaan_jos_ladattava_summa_on_negatiivinen(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo.return_value = 10

        self.kassa.lataa(maksukortti_mock, -5)

        maksukortti_mock.lataa.assert_not_called()
