#Ohjelmointi_tehtävä_6.1: koita saada silmäluku 6

def noppa():
    from random import randint
    pip_count=randint(1,6)
    #pip_count eli suomeksi silmäluku
    return pip_count

while True:
    pip_count=(noppa())
    print(pip_count)
    if pip_count==6:
        break
        
