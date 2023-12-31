"""
module doctstring
"""

import unittest
from varasto import Varasto
# pylint: disable=missing-function-docstring non-ascii-name

class TestVarasto(unittest.TestCase):
    """
    Testejä varastolle
    """
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uusi_varasto_negatiivinen_tilavuus(self):
        varasto = Varasto(-10)
        self.assertEqual(varasto.tilavuus, 0)

    def test_uusi_varasto_negatiivinen_saldo(self):
        varasto = Varasto(10, alku_saldo=-10)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_lisays_lisaa_saldoa_yli(self):
        self.varasto.lisaa_varastoon(18)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(10)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_saldoa_negatiivinen(self):
        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_väärä_otto_palauttaa_0(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-3), 0)

    def test_kaikki_mita_voidaan(self):
        self.varasto.lisaa_varastoon(2)
        kmv = self.varasto.ota_varastosta(3)
        self.assertAlmostEqual(kmv, 2)

    def test___str__(self):
        self.assertAlmostEqual("saldo = 0, vielä tilaa 10",
                               str(self.varasto))
