from helper import onderstreep 

uitvoer = onderstreep("AANBIEDINGEN")
uitvoer.append("Aardbijenijs, emmertje van 5 liter: 5 euro")
uitvoer.append("Slagroom, spuitbus van  liter: 2 euro")

print()

for el in uitvoer:
    print(el)