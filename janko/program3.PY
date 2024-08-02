class Supa:
    def __init__(self, v, p, k) -> None:
        self.vrsta = v
        self.grami_soli = p
        self.kolicina = k
        pass

    def dodaj_soli(self):
        self.grami_soli += 10

    def prikazi_stavke(self):
        print(
            f"Vrsta supe {self.vrsta} ima {self.grami_soli} grama soli i ima {self.kolicina} litara u serpi"
        )


class Tenk:
    def __init__(self, m, k, ms, mc, e, z) -> None:
        self.motor = m
        self.kalibar = k
        self.najveca_brzina = ms
        self.velicina_posade = mc
        self.eksplozija = e
        self.zastita = z
        pass


t_84 = Tenk("dizel", 100, 75, 6, 30, 50)


govedja_supa = Supa("govedja", 40, 60)
govedja_supa.dodaj_soli()
govedja_supa.prikazi_stavke()
