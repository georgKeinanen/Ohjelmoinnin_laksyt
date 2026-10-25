#Ohjelmointi tehtävä 9.2: Auton kiihdytys ja jarrutus

class Auto:
    def __init__(self,rekisteri_nro, huippu_nopeus:int):
        self.rekisteri=rekisteri_nro
        self.max_nopeus=huippu_nopeus
        self.nopeus=0
        self.kuljettu=0

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


auto1=Auto("ABC-123",142)
auto=auto1

print(f"Auton Rekisteri tunnus {auto.rekisteri}, huippu nopeus: {auto1.max_nopeus}km/h, kuljettumatka: {auto.kuljettu}km ja tämän hetkinen nopeus: {auto1.nopeus}km/h")
auto1.kiihdyta(30)
print(f"Rekisterillä {auto.rekisteri} varustetun auton tämän hetkinen nopeus: {auto.nopeus}km/h / {auto.max_nopeus}km/h")
auto1.kiihdyta(70)
print(f"Rekisterillä {auto.rekisteri} varustetun auton tämän hetkinen nopeus: {auto.nopeus}km/h / {auto.max_nopeus}km/h")
auto1.kiihdyta(50)
print(f"Rekisterillä {auto.rekisteri} varustetun auton tämän hetkinen nopeus: {auto.nopeus}km/h / {auto.max_nopeus}km/h")
auto1.kiihdyta(-200)
print(f"Rekisterillä {auto.rekisteri} varustetun auton tämän hetkinen nopeus: {auto.nopeus}km/h / {auto.max_nopeus}km/h")