# Ohjelmointi tehtävä 7.2: Nimet epäjärjestettynä

nimi_lista = []
while "" not in nimi_lista:
    nimi = input("Anna nimi: ")

    if nimi in nimi_lista:
        print("Aiemmin syötetty nimi")

    elif nimi not in nimi_lista and nimi != "":
        print("Uusi nimi")

    nimi_lista.append(nimi)

nimi_lista.remove("")

for nimi in set(nimi_lista):
    print(nimi)