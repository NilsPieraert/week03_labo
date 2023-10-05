# Vraag aan de gebruiker zijn naam, voornaam en geboortedatum (formaat: dd-mm-yyyy) op. Genereer 
# hiermee een paswoord door:
# - de eerste 3 karakters van de ingegeven familienaam (in kleine letters en zonder de eventuele 
# spaties mee te nemen)
# - de eerste 2 karakters van de voornaam (in hoofdletters en ook zonder spaties)
# - 4 cijfers (mmyy) uit de geboortedatum.
# Maak hiervoor een afzonderlijke functie ‘genereer_paswoord’. Welke parameters gebruik je, wat zal de 
# return waarde zijn?
naam = input ("Geef je naam op:> ")
voornaam = input ("Geef je voornaam op:> ")
geboortedatum = input ("Geef je geboortedatum op:> ")

def genereer_paswoord(naam:str, voornaam:str, geboortedatum:str)->str:
    wachtwoord = naam.strip()[:3].lower() + voornaam.strip().upper()[:2] + geboortedatum[3:5] + geboortedatum[8:]
    return f'{wachtwoord}'

print(genereer_paswoord(naam, voornaam, geboortedatum))



