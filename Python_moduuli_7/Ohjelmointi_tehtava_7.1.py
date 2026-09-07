#Ohjelmointi tehtävä 7.1: Vuodenajat
#En tiedä miten määrittää järkevällä tavalla joulukuuta ekaksi talvi kuukaudeksi
vuodenajat=("talvi","kevät","kesä","syksy")
kuukaus_nro=int(input("Anna kuukauden numero: "))

if kuukaus_nro in (12,1,2):
  print(vuodenajat[0])

elif kuukaus_nro in (3,4,5):
  print(vuodenajat[1])

elif kuukaus_nro in (6,7,8):
  print(vuodenajat[2])

elif kuukaus_nro in (9,10,11):
  print(vuodenajat[3])

else:
  print("Virheelinen kuukausi numero")