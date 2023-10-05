# Oef 15
# Vraag aan de gebruiker zijn/haar howest-e-mailadres op. Haal hieruit de naam & voornaam en print 
# deze af. Voor de eenvoud gaan we ervan uit dat de voornaam uit één deel bestaat. Zorg ervoor dat de 
# eerste letter van de naam & voornaam met een hoofdletter afgeprint wordt

email = input ("Geef je HoWest eailadres op op:> ")

apenstaartje = email.find( "@" )
naam = email[:apenstaartje]
punt = naam.find(".")
print(f"Je familie naam is {naam[punt:][1:]}")
print(f"Je voornaam naam is {naam[:punt]}")

