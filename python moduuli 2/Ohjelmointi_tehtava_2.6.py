#Ohjelmointi tehtävä 2.6: Ovikoodit

from random import sample
#Tuodaan random moduulista funktio sample jolla saadaan haluttu määrä satunnais lukuja listasta

lista1=["0","1","2","3","4","5","6","7","8","9"]
lista2=["1","2","3","4","5","6"]


ovikoodi1="".join(sample(lista1,3))
ovikoodi2="".join(sample(lista2,4))
#liitetään sample listastasta tyhjään merkkijonoon join metodilla
#Näin saadaan luotua ovikoodit

print(ovikoodi1)
print(ovikoodi2)