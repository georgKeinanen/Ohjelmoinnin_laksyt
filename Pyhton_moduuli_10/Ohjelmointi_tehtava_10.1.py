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

hissi=Hissi(1, 10)
hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(3)
hissi.siirry_kerrokseen(10)
hissi.siirry_kerrokseen(-5)
hissi.siirry_kerrokseen(100)

