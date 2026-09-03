#Ohjelmointi tehtävä 6.3: Gallonat litroiksi...
#Lyhyesti sanottuna gallons 2 liters :D

def gallons2liters(gallonat):
    litra=gallonat*3.785
    return litra

while True:
    gallonat=float(input("Anna gallonat, negatiivinen luku lopettaa: "))
    litra=gallons2liters(gallonat)
    if gallonat<0:
        print("Kiitos käynnistä ja tervetuloa uudelleen :D")
        break
    print(f"antamasi gallonat ({gallonat} gal) litroina on {litra} l" )