# Ohjelmointi_tehtava 7.3: Lentoasemoiden hakeminen ja lisääminen

# Muistuttaa SQL:ästä

airports = {}
while True:
    action = int(input("(1) Uusi lentoasema (2) Hae lentoasemia (3) Lopeta: "))

    if action == 1:
        airport_id = input("Anna lentoaseman ICAO-koodi: ")
        airport = input("Anna lentoaseman nimi: ")

        airports[airport_id] = airport
        # print(airports)

    elif action == 2:
        airport_id = input("Anna etsittävän lentoaseman ICAO-koodi: ")
        if airport_id in airports:
            print(airports[airport_id])

        else:
            print("Hakemaasi lentoasemaa ei löytynyt :(")

    else:
        print("Kiitos käynnistä ja tervetuloa uudelleen")
        break