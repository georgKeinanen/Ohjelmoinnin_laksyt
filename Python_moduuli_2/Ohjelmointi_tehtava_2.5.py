#Ohjelmointi tehtävä 2.5: Keskiajan mittayksiköt

#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.

leiviska=float(input("Anna leiviskät: "))
naula=float(input("Anna naulat: "))
luoti=float(input("Anna luodit: "))

#mitta yksiköt nopeampaa testaamista varten :D

#leiviska=3
#naula=9
#luoti=13.5


leiviska*=20
naula+=leiviska
#kerrotaan leiviskät luvulla 20 ja lisätään ne nauloihin.
#eli muuetaan leiviskät nauloiksi
#leiviskä --> naula
naula*=32
luoti+=naula
#kerrotaan naulat luvulla 32 ja lisätään ne luoteihin.
#naulat --> luodit

luoti*=13.3
gram=luoti%1000
#tehdään luotien jakojäännöksellä luvulla 1000 grammat
kilo=(luoti-gram)/1000
#miinustetaan grammat luotien kokonaismäärästä ja jaetaan sitten luvulla 1000 niin saadan muutettu lopputulos kiloiksi


print("Massa nykymittojen mukaan:")
print(f"{int(kilo)} kilogrammaa ja {gram:.2f} grammaa.")