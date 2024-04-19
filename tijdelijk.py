


Prijzen = {
    "Aardbei":3,
    "Vanille":4,
    "Chocolade":5
}

Aanbieding = Prijzen["Aardbei"] * 0.8

print(Prijzen)

reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts $ {Aanbieding}")
print(reclame_tekst)

reclame_tekst2 = reclame_tekst[:63]
print(reclame_tekst2)

reclame_tekst3 = reclame_tekst2
print(reclame_tekst3.upper())

reclame_tekst4 = reclame_tekst3 
print(reclame_tekst4.split(" "))

for el in reclame_tekst4:
 print(el)

print(reclame_tekst4.lower())

for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())