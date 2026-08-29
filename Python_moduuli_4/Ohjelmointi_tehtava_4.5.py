# Ohjelmointi tehthava 4.5: käyttäjätunnus ja salasana

while True:
    username = input("anna käyttäjätunnus: ")
    password = input("anna salasana: ")

    if username == "python" and password == "rules":
        print("Tervetuloa")
        break

    else:
        print("Pääsy evätty")