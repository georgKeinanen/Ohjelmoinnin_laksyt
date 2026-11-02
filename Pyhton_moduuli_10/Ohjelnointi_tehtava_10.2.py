#Ohjelmointi tehtävä 
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.ylin=ylin_kerros
        self.alin=alin_kerros
        self.kerros=alin_kerros

    def kerros_ylös(self):
        self.kerros+=1
        print(f"YLÖS ^ {self.kerros}")

    def kerros_alas(self):
        self.kerros-=1
        print(f"ALAS v {self.kerros}")

    def siirry_kerrokseen(self, kerros):
        print(f"Siirytään kerrokseen {kerros}")
        while self.kerros<kerros and self.kerros< self.ylin:
            self.kerros_ylös()
        while self.kerros>kerros and self.kerros>self.alin:
            self.kerros_alas()

class Talo:
    def __init__(self, ylin, alin,hissien_määrä):
        self.hissien_määrä=hissien_määrä
        self.ylin=ylin
        self.alin=alin
        self.hissit=[]

    def aja_hissiä(self, hissi_nro, kerros):
