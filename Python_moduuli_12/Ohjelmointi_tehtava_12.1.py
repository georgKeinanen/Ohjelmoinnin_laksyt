#Ohjelmointi tehtävä 12.1: Chuck Norris vitsit
#Chuck Norris once loaned the dinosaurs' money. They never paid him back.
import requests

vitsi=requests.get("https://api.chucknorris.io/jokes/random")
json_vastaus = vitsi.json()
print(json_vastaus["value"])
#print(json_vastaus)