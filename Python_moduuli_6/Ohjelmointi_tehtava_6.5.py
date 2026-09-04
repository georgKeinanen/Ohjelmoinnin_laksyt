# Ohjelmointi_tehtava 6.4: listan alkioiden summa

def odds_remove(lista):
    parilliset = []
    print(f"Alkuperäinen: {lista}")
    for luku in lista[0:len(lista)]:

        # jostain syystä for silmukka ei iteroi listaa kunolla
        # jos iteroida kopiota siitä joka on lista[0:-1]
        if luku % 2 == 0:
            parilliset.append(luku)

    return f"Parittomat luvut postettu: {parilliset}"


lista = [2, 4, 3, 5, 8, 13, 23, 33, 3, 24]
print(odds_remove(lista))