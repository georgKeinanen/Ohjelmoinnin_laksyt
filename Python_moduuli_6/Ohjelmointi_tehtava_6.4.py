#Ohjelmointi_tehtava 6.4: listan alkioiden summa

def summa_lista(lista):
    alkio_sum=0
    for luku in lista:
        #print(luku)
        alkio_sum+=luku

    return f"Listassa olevien lukujen summa: {alkio_sum}"

lista=[2,3,8,13,23]
print(summa_lista(lista))