# Vraag aan de gebruiker volgende 3 getallen op:
# - een startwaarde
# - een positieve stapgrootte
# - het gewenste aantal af te printen getallen
# Schrijf een functie ‘print_lijst_getallen’ die deze 3 getallen als parameter binnen krijgt. De functie print 
# een lijst, met het gewenste aantal getallen, af waarbij het eerste getal gelijk is aan de startwaarde en de 
# getallen met de stapgrootte vergroten.De functie heeft geen return waarde. Het afprinten gebeurt IN de 
# functie.


start = int(input ("Geef een startwaarde op:> "))
step = int(input ("Geef een stapwaarde op:> "))
aantal = int(input ("Geef een aantal op:> "))

def print_lijst_getallen(start:int, step:int, aantal:int) ->None:
    stop = start + step*aantal
    for i in range(start, stop, step):
        print(i)

print_lijst_getallen(start, step, aantal)