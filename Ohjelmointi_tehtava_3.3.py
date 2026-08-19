# Ohjelmointi tehtava 3.3: Hemoglobiini arvot

biolog_gender = input("Anna biologinen sukupuolesi: ")
hemogoblin = float(input("Anna hemoglobiini arvosi: "))
# hemoglobiini arvon nimi on "hemogoblin" koska sanasta hemoglobiini tulee mieleen sana goblin.

if biolog_gender == "mies":


    # Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
    if hemogoblin >= 134 and hemogoblin <= 195:

        print("Hemoglobiin arvosi on normaali.")
        print(f"Hemoglobiini arvosi: {hemogoblin} g/l")

    elif hemogoblin > 195:
        print(f"Hemoglobiini arvosi on korkea.")
        print(f"Hemoglobiini arvosi: {hemogoblin} g/l")

    else:
        print("Hemoglobiini arvosi on alhainen.")
        print(f"Hemoglobiini arvosi: {hemogoblin} g/l")



elif biolog_gender== "nainen":
    # Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.

    # Samoista syistä tästäkin ehtolauseesta löytyy metodi lower

    if hemogoblin >= 117 and hemogoblin <= 175:
        print("Hemoglobiin arvosi on normaali.")
        print(f"Hemoglobiini arvosi: {hemogoblin} g/l")

    elif hemogoblin > 175:
        print(f"Hemoglobiini arvosi on korkea.")
        print(f"Hemoglobiini arvosi: {hemogoblin} g/l")

    else:
        print("Hemoglobiini arvosi on alhainen.")
        print(f"Hemoglobiini arvosi: {hemogoblin} g/l")

# _______Y/_____
# |---------------------/
# |..0|...0.........../
# |...|.............-
# |...|......./----
# |...|......|
# |...|_..../
# |......../
# /-----\.|
# ______/.|
# |....../
# ------/


# Hemogoblin