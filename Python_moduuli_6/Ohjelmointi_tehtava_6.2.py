#Ohjelmointi_tehtävä_6.2: Erillaisten noppien max silmäluku
#D21 saatu suorituksen ekalle riville yli 10 yrityksen jälkeen

def noppa(tahkot):
    from random import randint
    pip_count=randint(1,tahkot)
    #pip_count eli suomeksi silmäluku
    return pip_count

tahkot=int(input("Anna noppasi tahkojen määrä: "))
while True:
    pip_count=(noppa(tahkot))
    print(pip_count)
    if pip_count==tahkot:
        break