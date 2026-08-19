#Ohjelmointi tehtävä 3.4: karkaus vuosi

vuosi=int(input("Anna vuosiluku: "))


if vuosi%4==0:
    #jos vuosi on jaollinen luvulla 4 se pääsee testavaski

    if vuosi%100==0 and vuosi%400==0:
        #Vuosiluku joka on jaollinen luvulla 100 on myös oltava jaollinen luvulla 400
        print(f"Antamasi vuosi ({vuosi}) on karkausvuosi.")

    elif vuosi%100==0 and vuosi%400!=0:
        #Jos vuosiluku on jaollinen luvulla 100 mutta ei jaollinen luvulla 400...
        #ohjelma ilmoittaa että antamasi vuosi eil ole karkausvuosi.
        #esim. vuosiluku 100 joka on jaollinen luvulla 4 ja 100 mutta ei ole jaollinen luvulla 400

        print(f"Antamasi vuosi ({vuosi}) ei ole karkausvuosi.")


    else:
        #jos Vuosiluku on jaollinen luvulla 4 mutta ei jaollinen luvulla 100 niin päädytään tänne
        print(f"Antamasi vuosi ({vuosi}) on karkausvuosi.")

else:
    #Jos taas vuosiluku ei ole jaollinen luvulla 4, niin päädymme tänne
    #Täällä ei vuodet karkaa
    print(f"Antamasi vuosi ({vuosi}) ei ole karkausvuosi.")