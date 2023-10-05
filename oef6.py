# Vraag aan de gebruiker volgende 2 getallen op:
# - een startwaarde
# - een stopwaarde
# Print een lijst van alle getallen tussen de twee opgegeven grenzen (grenzen inclusief) die deelbaar door 
# 7 maar geen veelvoud van 5 zijn

start = int(input ("Geef een startwaarde op:> "))
stop = int(input ("Geef een stopwaarde op:> "))

getal = start

for i in range(start, stop+1):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
