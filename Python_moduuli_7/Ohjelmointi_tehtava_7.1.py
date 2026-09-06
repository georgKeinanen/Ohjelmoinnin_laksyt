#Ohjelmointi tehtävä 7.1: Vuodenajat
#En tiedä miten määrittää järkevällä tavalla joulukuuta ekaksi talvi kuukaudeksi
vuodenajat=("talvi","kevät","kesä","syksy")
kuukaus_nro=int(input("Anna kuukauden numero: "))

if kuukaus_nro in (1,2,3):
  print(vuodenajat[0])

elif kuukaus_nro in (4,5,6):
  print(vuodenajat[1])

elif kuukaus_nro in (7,8,9):
  print(vuodenajat[2])

elif kuukaus_nro in (10,11,12):
  print(vuodenajat[3])

else:
  print("Virheelinen kuukausi numero")