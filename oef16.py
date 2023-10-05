# Maak een functie ‘genereer_paswoord_bis’ met als parameters minimum_lengte en maximum_lengte. 
# De functie genereert een willekeurig paswoord bestaande uit een combinatie van kleine en 
# hoofdletters, én waarvan de lengte van het genereerde paswoord tussen beide grenzen valt.
# Tip: maak gebruik van string.ascii_letters uit de klasse string

import random

minimumlengte = input(int("Geef de Minimumlengte van je wavhtwoord op:> "))
maximumlengte = input(int("Geef de maximumlengte van je wavhtwoord op:> "))

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
i = 0

lengte = random.randint(minimumlengte, maximumlengte)

while i < lengte:
    letter = random.randint(minimumlengte, maximumlengte)

