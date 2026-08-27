# Ohjelmointi tehtävä 4.2: Tuumat senteiksi
# Tuumasta toimeen
while True:
    tuuma = float(input("Montako tuumaa muutentaan senttimetreiksi: "))
    if tuuma < 0:
        break

    print(f"{tuuma} ---> {tuuma * 2.54} cm")

# Lisätty koska miksi ei
# Viesti siitä että ohjelma lopetettu
print("kiitos käynnistä ja tervetuloa uudelleen")