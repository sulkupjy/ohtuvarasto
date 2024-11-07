import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # Varmistetaan, että saldo on alussa 0
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    # Tässä ovat lisätestit haarautumakattavuuden varmistamiseksi

    def test_lisays_yli_tilavuuden(self):
        # Lisätään enemmän kuin varastoon mahtuu
        self.varasto.lisaa_varastoon(15)
        # Varmistetaan, että saldo ei ylitä varaston tilavuutta
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_otto_yli_saldon(self):
        # Otetaan enemmän kuin varastossa on
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(10)
        # Varmistetaan, että saatu määrä ei ylitä varaston saldoa
        self.assertAlmostEqual(saatu_maara, 5)
        # Ja varaston saldo on nyt 0
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivinen_lisays(self):
        # Yritetään lisätä negatiivinen määrä
        self.varasto.lisaa_varastoon(-5)
        # Varmistetaan, että saldo ei muutu
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivinen_otto(self):
        # Yritetään ottaa negatiivinen määrä
        saatu_maara = self.varasto.ota_varastosta(-5)
        # Varmistetaan, että otettu määrä on 0
        self.assertAlmostEqual(saatu_maara, 0)
        # Saldo pysyy ennallaan
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_negatiivinen_tilavuus(self):
        # Luodaan varasto negatiivisella tilavuudella
        varasto = Varasto(-10)
        # Varmistetaan, että tilavuus on nolla
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_konstruktori_negatiivinen_alku_saldo(self):
        # Luodaan varasto negatiivisella alkusaldo
        varasto = Varasto(10, -5)
        # Varmistetaan, että saldo on nolla
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_paljonko_mahtuu_kun_taynna(self):
        # Täytetään varasto kokonaan
        self.varasto.lisaa_varastoon(10)
        # Varmistetaan, että ei mahdu yhtään enempää
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_lisays_tasan_tilavuus(self):
    # Testataan, että täsmälleen tilavuuden verran lisääminen onnistuu
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_konstruktori_alkusaldo_suurempi_kuin_tilavuus(self):
    # Varmistetaan, että alkusaldo ei voi olla suurempi kuin tilavuus
        varasto = Varasto(10, 15)  # Saldo on alussa suurempi kuin tilavuus
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_str_metodi(self):
    # Alustetaan varasto saldolla 5
        varasto = Varasto(10, 5)
    # Odotettu tulos: "saldo = 5, vielä tilaa 5"
        self.assertEqual(str(varasto), "saldo = 5, vielä tilaa 5")