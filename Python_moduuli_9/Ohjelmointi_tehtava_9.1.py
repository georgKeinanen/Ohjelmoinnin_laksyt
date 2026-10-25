#Ohjelmointi tehtävä 9.1: Autojen luonti

class Auto:
    def __init__(self,rekisteri_nro, huippu_nopeus):
        self.rekisteri=rekisteri_nro
        self.max_nopeus=huippu_nopeus
        self.nopeus=0
        self.kuljettu=0

auto1=Auto("ABC-123",142)
print(f"Auton Rekisteri tunnus {auto1.rekisteri}, huippunopeus: {auto1.max_nopeus}km/h, kuljettumatka: {auto1.kuljettu}km ja tämän hetkinen nopeus: {auto1.nopeus}km/h")