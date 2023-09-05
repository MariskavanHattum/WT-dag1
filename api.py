print('Start api uitlees applicatie')

import requests

paginaresults = requests.get('https://catfact.ninja/facts')
print (paginaresults)

feitjes = paginaresults.json() # lees de json file uit, omzetten naar data die we kunnen weergeven
print("Feitje is dat " + feitjes["data"][0]["fact"]) # de 0 geeft je eerste feitje, fact geeft aan dat je alleen de fact string wil, niet de length