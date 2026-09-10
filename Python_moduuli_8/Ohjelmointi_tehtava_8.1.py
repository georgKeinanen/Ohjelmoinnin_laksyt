#Ohjelmointi tehtävä 8.1: Icao_koodilla lentokentän etsiminen
#Helsinki Vantaan lentoasema ei ole Helsingissä vaikka tietokannasssa näin lukee
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Rotting_dir?1984',
         autocommit=True
         )
#Kyselyn määritys
icao_koodi = input("Anna lentokentän ICAO koodi: ")
query = f"select name, municipality from airport where ident='{icao_koodi}';"
DBkursori= yhteys.cursor()
#Kyselyn suoritus
DBkursori.execute(query)

#Tuloksen haku
tulos=DBkursori.fetchall()
print(tulos)

