#Ohjelmointi tehtävä 3.1: Kuhan pyyntimitta
kuha_long=float(input("Anna kuhan pituus: "))
if kuha_long<37:
    print("Saamasi kuha on ala mittainen. Laske se takasin veteen heti nyt VÄLITTOMÄSTI!!!!! >:O")
    print(f"Saamasi kuhan pyyntimitasta puuttuu {37-kuha_long}")

else:
    print("kuhan pyyntimitta on riitävä, voit syödä sen :D")
