#Ohjelmointi tehtävä 11.2: Moottorityyppi +kulje

class Auto:
    def __init__(self,rekisteri_nro, huippu_nopeus, nopeus=0, kuljettu_matka=0):
        self.rekisteri=rekisteri_nro
        self.max_nopeus=huippu_nopeus
        self.nopeus=nopeus
        self.kuljettu=kuljettu_matka


class Polttomoootri_auto(Auto):
    def __init__ (self,rekisteri_nro, huippu_nopeus, tankin_koko, nopeus=0, kuljettu_matka=0):
        super().__init__(rekisteri_nro, huippu_nopeus)
        self.nopeus=nopeus
        self.kuljettu=kuljettu_matka
        self.tankin_koko = tankin_koko

    def tulosta_tiedot(self):
        print(f"Auton rekisteritununnus: {self.rekisteri}")
        print(f"Auton huippunopeus: {self.max_nopeus} km/h")
        print(f"Auton tämän hetkinen nopeus: {self.nopeus} km/h")
        print(f"Auton ajokilometrit: {self.kuljettu} km ")
        print(f"Auton bensatankin koko: {self.tankin_koko}  L")
        print("")

    def kulje(self, nopeus: int, tunnit: float):
        if nopeus <= self.max_nopeus:
            self.nopeus = nopeus
            self.kuljettu += nopeus * tunnit
        else:
            self.nopeus = self.max_nopeus
            self.kuljettu += self.nopeus * tunnit
        print(f"kuljettiin nopeudella: {self.nopeus} km/h {tunnit} tuntia")

class Sahko_auto(Auto):
    def __init__ (self,rekisteri_nro, huippu_nopeus, akku_kapasiteetti, nopeus=0, kuljettu_matka=0):
        super().__init__(rekisteri_nro, huippu_nopeus)
        self.nopeus=nopeus
        self.kuljettu=kuljettu_matka
        self.akku_cap=akku_kapasiteetti

    def tulosta_tiedot(self):
        print(f"Auton rekisteritununnus: {self.rekisteri}")
        print(f"Auton huippunopeus: {self.max_nopeus} km/h")
        print(f"Auton tämän hetkinen nopeus: {self.nopeus} km/h")
        print(f"Auton ajokilometrit: {self.kuljettu} km ")
        print(f"Auton Akkukapasiteetti: {self.akku_cap}  kW/h")
        print("")

    def kulje(self, nopeus: int, tunnit: float):
        if nopeus <= self.max_nopeus:
            self.nopeus = nopeus
            self.kuljettu += nopeus * tunnit
        else:
            self.nopeus = self.max_nopeus
            self.kuljettu += self.nopeus * tunnit
        print(f"kuljettiin nopeudella: {self.nopeus} km/h {tunnit} tuntia")

auto1=Sahko_auto("ABC-15", 180, 52.5)
auto2=Polttomoootri_auto("ACD-123", 165, 32.3)
auto1.kulje(nopeus=179, tunnit=3)
auto1.tulosta_tiedot()
auto2.kulje(nopeus=197, tunnit=3)
auto2.tulosta_tiedot()
