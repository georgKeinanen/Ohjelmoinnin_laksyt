# Ohjelmointi_tehtava 6.4: listan alkioiden summa

def odds_remove(lista):
    for luku in lista[0:-1]:
        # jostain syystä for silmukka ei iteroi listaa kunolla
        # jos iteroida kopiota siitä joka on lista[0:-1]
        if luku % 2 != 0:
            # print(i)
            lista.remove(luku)

    return lista


lista = [2, 4, 3, 5, 8, 13, 23, 33, 3, 24]
print(odds_remove(lista))