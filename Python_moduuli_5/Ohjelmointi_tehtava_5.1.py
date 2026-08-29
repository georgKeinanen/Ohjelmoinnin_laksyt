#Ohjelmointi tehtava 5.1: silmälukujen summa

from random import randint

dice_count=int(input("Anna noppien määrä: "))

pip_counts=0
#Tulee sananasta pip count eli silmäluku

for i in range(0,dice_count):
    dice=randint(1,6)
    #print(dice)

    pip_counts+=(dice)
print(pip_counts)