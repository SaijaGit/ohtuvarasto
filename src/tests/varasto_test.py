import unittest
from varasto import Varasto

# Yksikkötestit luokalle varasto.py

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

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
    
    def test_lisays_lisaa_liikaa_saldoa(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(20)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_liikaa_varastosta(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(20)

        self.assertAlmostEqual(saatu_maara, 8)
    
    def test_liikaa_ottaminen_tyhjentaa_varaston(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(20)

        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_lisays_lisaa_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_ota_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(-10)

        self.assertAlmostEqual(saatu_maara, 0)
    
    def test_negatiivisen_ottaminen_ei_muuta_tilaa(self):
        self.varasto.lisaa_varastoon(5)

        self.varasto.ota_varastosta(-5)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 5)

    def test_ala_luo_negatiivista_varastoa(self):
        varasto = Varasto(-5, 0)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_ala_luo_varastoa_negatiivisella_saldolla(self):
        varasto = Varasto(10,-5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_ala_luo_varastoa_jossa_liikaa_tavaraa(self):
        varasto = Varasto(5, 10)
        self.assertAlmostEqual(varasto.saldo, 5)

    def test_ala_luo_liian_suurta_varastoa_vaikka_taytta(self):
        varasto = Varasto(5, 10)
        self.assertAlmostEqual(varasto.tilavuus, 5)
    
    def test_tilateksti_oikein(self):
        self.varasto.lisaa_varastoon(8.5)
        self.assertEqual(str(self.varasto), "saldo = 8.5, vielä tilaa 1.5")