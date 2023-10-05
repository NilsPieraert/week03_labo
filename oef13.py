woord1 = input ("Geef je eerste woord op:> ")
woord2 = input ("Geef je tweede woord op:> ")

def swap(woord1:str, woord2:str)->str:
    new_woord1 = woord2[:2] + woord1[2:]
    new_woord2 = woord1[:2] + woord2[2:]
    return f'{new_woord1}  {new_woord2}'

print(swap(woord1, woord2))