
# import random module
import random
gok = 25
i = 0
r1 = random.randint(1, 20)
while gok != r1:
    i += 1
    gok = int(input ("Doe een gokje tussen 1 en 20:> "))
    if gok > r1 :
        print("Getal te hoog")
    elif gok < r1 :
        print("Getal te laag")
    

print(f"Proficiat. Gevonden! \n \t U gokte= {i} maal")
