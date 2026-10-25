#Ohjelmointi tehtävä 9.3: Autot liikkuu ja kulkee

class Auto:
    def __init__(self,rekisteri_nro, huippu_nopeus:int, kuljettu_matka:int):
        self.rekisteri=rekisteri_nro
        self.max_nopeus=huippu_nopeus
        self.nopeus=0
        self.kuljettu=kuljettu_matka

    def kiihdyta(self, kiihdytys:int):
        if kiihdytys>0:        #<---------- ehtojen kanssa väännetty noin tunti tai 2
            self.nopeus+=kiihdytys
            #Auto kiihdyttää jos annettu kiihdytys on suurempi kuin 0
            print(f"nopeus +{kiihdytys}")

        if kiihdytys<0:
            #Auto jarruttaa jos kiihdytys on nollaa pienenpi
            self.nopeus+=kiihdytys
            print(f"nopeus {kiihdytys}")

        if self.max_nopeus<self.nopeus:
            #Ehto joka estää huippu nopeuden ylityksen
            self.nopeus=self.max_nopeus
            print("huippu nopeus saavutettu")

        if self.nopeus<=0:
            # Ehto joka pysäyttää auton ja estää nopeuden muutumisen negatiiviseksi
            self.nopeus=0
            #Nopeus muutetaan nollaksi vaikka jarrutuksen tulos olisi negatiivinen luku
            print("Auto pysähtyi")

    def kulje(self, nopeus:int, tunnit:float):
        if nopeus<=self.max_nopeus:
            self.nopeus=nopeus
            self.kuljettu += nopeus * tunnit
        else:
            self.nopeus=self.max_nopeus
            self.kuljettu += self.nopeus * tunnit


auto1=Auto("ABC-123",142, 2000)
print(f"Auton Rekisteri tunnus {auto1.rekisteri}, huippunopeus: {auto1.max_nopeus}km/h, kuljettumatka: {auto1.kuljettu}km ja tämän hetkinen nopeus: {auto1.nopeus}km/h")
Auto.kulje(auto1,60, 1.5)

print(f"Rekisterillä {auto1.rekisteri} varustetun auton tämän hetkinen nopeus: {auto1.nopeus}km/h ja kuljettu: matka {auto1.kuljettu}km")
