# Ohjelmointi tehtävä: 5.2: 5 suurinta lukua laskevassa järjestyksesä
luvut = []
while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    luvut.append(int(luku))

if len(luvut) > 5:
    print(sorted(luvut, reverse=True)[0:5])

else:
    print(sorted(luvut, reverse=True))