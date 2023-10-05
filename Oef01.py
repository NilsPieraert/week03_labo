# Oef 01
# Print de som van de eerste 100 getallen. Gebruik een for-lus.


end = 100
sum = 0 
index = 1

while index <= end:
    sum = sum + index
    index += 1

print(f"De som van de eerste {end} getallen is : {sum}.\n")