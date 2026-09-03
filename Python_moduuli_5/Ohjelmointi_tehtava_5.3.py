#Ohjemointi tehtävä 5.3: Alkuluku:
#kaiken luvun alkujuuri
#Alkuluku tässä tehtävässä on jaollinen vain luvula 1 tai itsellään.

luku=int(input("Anna luku: "))
jaollisuus=[]
for jakaja in range(1,luku+1):
    if luku%jakaja==0:
        jaollisuus.append(jakaja)
        #Tallentaa listaan luvut joilla antamasi luku on jaollinen...

if len(jaollisuus)==2 or len(jaollisuus)==1:

    print(f"Antamasi luku on alkuluku. Antamasi luku: {luku}")

else:
    print(f"Antamasi luku ei ole alkuluku. Antamasi luku: {luku}")