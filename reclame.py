def aanbieding_1(smaak, prijs, korting):
    korting_bedrag = prijs * korting
    prijs_met_korting = prijs - korting_bedrag

    uitvoer = f"In de aanbieding: emmertje ijs (1 liter) in de smaak {smaak} van {prijs} voor {prijs_met_korting}"
    return uitvoer

print(aanbieding_1("Aarbei", 4, 0.1))






