#Ohjelmointi tehtävä 8.2: Lentokenttien tyyppien lukumäärä

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
maakoodi = input("Anna maakoodi: ")
sql = f"select type, count(*) from airport where iso_country='{maakoodi}' group by type;;"
DBkursori= yhteys.cursor()
#Kyselyn suoritus
DBkursori.execute(sql)

#Tuloksen haku
tulos=DBkursori.fetchall()
for rivi in tulos:
    print(rivi)

