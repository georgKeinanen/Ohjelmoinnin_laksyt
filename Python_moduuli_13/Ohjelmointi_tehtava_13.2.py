#Ohjelmointi tehtävä 13.2: Lentoasema tietojen haku taustapalvelun avulla
#Linkki tasuta palveluun jos sitä ei ole jo avattu :]
#http://127.0.0.1:3000/kentt%C3%A4/EFHK

from flask import Flask, request
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Rotting_dir?1984',
    autocommit=False
)

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def kenttä(icao):
    DBkursori = yhteys.cursor()
    sql_kysely=f"select name, municipality from airport where ident='{icao}';"
    DBkursori.execute(sql_kysely)
    tulos=DBkursori.fetchall()

    if len(tulos)==0:
        vastaus = {
            "status": 400,
            "teksti": "Etsimääsi ICAO-koodia ei ole olemassa"
        }
        return str(vastaus)
    else:

        vastaus = {
        "ICAO": icao,
        "Name": tulos[0][0],
        "Municipality": tulos[0][1]
        }
        return str(vastaus)

app.run(use_reloader=True, host='127.0.0.1', port=3000)

#                        _____
#                       |  ___|
#             .-----_```` |_____
#      ____.--|        ___     |
#     |    | |        |___|    |____
#     | ___| `-----                 |
#_____||___|__   _|            ____ |  <----- This tree is not my creation, it just grows here...
#|       ||__| _|_|          /|    |*
#|       |____|     .--------```|`|`
#|            |____ |--._____.--* |
#|                 |___||_| _.-   |
#|                __|   ___/      |
#|               |    _/          |
#|             _/    (._          |
#|            /_-_-_-_-_\         |
#|____                        ____|
#     |_______________________|
#Well there was an ICAO-code here
