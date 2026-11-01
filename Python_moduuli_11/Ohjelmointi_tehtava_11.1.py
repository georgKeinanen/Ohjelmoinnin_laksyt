#Ohjelmointi tehtävä 11.1: Kirja on julkaisu myös.

class Julkaisu:
    def __init__(self, nimi):
        self.nimi=nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, sivumaara, kirjailia):
        super().__init__(nimi)
        self.sivut = sivumaara
        self.kirjailia=kirjailia

    def tulosta_tiedot (self):
        print(f"Kirjan nimi: {self.nimi}")
        print(f"Krijan sivumäärä: {self.sivut}")
        print(f"Kirjan kirjailija: {self.kirjailia}")
        print("")

class Lehti(Julkaisu):
    def __init__(self, nimi, head_suplier):
        super().__init__(nimi)
        self.suplier=head_suplier

    def tulosta_tiedot (self):
        print(f"Lehden nimi: {self.nimi}")
        print(f"Lehden Päätoimittaja: {self.suplier}")
        print("")

#Kirja("Homestuck", 8000, "Andrew Hussie")

julkaisut=[]
#julkaisut.append(Kirja("Homestuck", 8000, "Andrew Hussie"))
julkaisut.append(Lehti("Aku Ankka", "Aki Hyypä"))
julkaisut.append(Kirja("Hytti nro 6", 200, "Rosa Liksom"))

for julkaisu in julkaisut:
    julkaisu.tulosta_tiedot()


