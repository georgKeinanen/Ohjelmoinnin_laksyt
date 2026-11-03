#Ohjelmointi tehtävä 13.1: Alkuluvun tarkastaminen taustapalvelulla

from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):

    jaollisuus = []
    for jakaja in range(1, int(luku) + 1):
        if int(luku) % jakaja == 0:
            jaollisuus.append(jakaja)
            # Tallentaa listaan luvut joilla antamasi luku on jaollinen...

    if len(jaollisuus) == 2 or len(jaollisuus) == 1:
        vastaus = {
            "Number": luku,
            "Isprime": True
        }
        return vastaus
    else:
        vastaus = {
            "Number": luku,
            "Isprime": False
        }
        return vastaus
app.run(use_reloader=True, host='127.0.0.1', port=3000)
