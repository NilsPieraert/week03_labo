# totaal_aantal_fruit = 0
# totaal_aantal_groenten = 0
# totaal_aantal_drank = 0
# totaal_kost_fruit = 0
# totaal_kost_groenten = 0
# totaal_kost_drank = 0
# i=0

# aantal = input(int("Geef het aantal producten op dat u wenst in te voeren :> "))


# while i < aantal :
#     categorie = input(int("Wat is de categorie? [G = Groenten, F = Fruit, D = Drank] :> "))
#     kostprijs = input(float("Wat is de kostprijs van dit product :> "))
#     if categorie.upper() == "D":
#         totaal_aantal_drank = totaal_aantal_drank + 1
#         totaal_kost_drank = totaal_kost_drank + kostprijs
#     elif categorie.upper() == "F":
#         totaal_aantal_fruit = totaal_aantal_fruit + 1
#         totaal_kost_fruit = totaal_kost_fruit + kostprijs

#     elif categorie.upper() == "G":
#         totaal_aantal_groenten = totaal_aantal_groenten + 1
#         totaal_kost_groenten = totaal_kost_groenten + kostprijs

#     else:
#         print("Foute invoer")

totaal_fruit = 0
totaal_groenten = 0
totaal_drank = 0
aantal_fruit = 0
aantal_groenten = 0
aantal_drank = 0


aantal =int(input("Geef het aantal producten op dat u wenst in te voeren :> "))


for i in range(aantal):
    categorie = input("Wat is de categorie? [G = Groenten, F = Fruit, D = Drank] :> ")
    kost_product = float(input("Wat is de kostprijs van dit product :> "))
    if categorie.upper() == "G":
        aantal_groenten = aantal_groenten + 1
        totaal_groenten = totaal_groenten + kost_product
    elif categorie.upper() == "D":
        aantal_drank = aantal_drank + 1
        totaal_drank = totaal_drank + kost_product
    elif categorie.upper() == "F":
        aantal_fruit = aantal_fruit + 1
        totaal_fruit = totaal_fruit + kost_product
    else:
        print("Foute invoer")
    
def geef_ticket_per_categorie(categorienaam:str, totaal: int, aantal_producten:int )->str:
    gemiddelde = totaal / aantal_producten
    deel1 = f"Er zitten {aantal_producten} in {categorienaam}"
    deel2 = f"De gemiddelde prijs per product is : {gemiddelde}"
    deel3 = f"De totale kost van deze categorie is $: {totaal}"
    return deel1 + "\n" + deel2 + "\n" + deel3

print(geef_ticket_per_categorie("Groente", totaal_groenten , aantal_groenten))
print(geef_ticket_per_categorie("Fruit", totaal_fruit , aantal_fruit))
print(geef_ticket_per_categorie("Drank", totaal_drank , aantal_drank))

  