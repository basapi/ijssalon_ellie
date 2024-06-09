import csv
from presentatie import presenteer
from helper import onderstreep, som

inkomsten = {
    "Aardbeijen-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-ijs-totaal" : 750
}

totaal_inkomsten = som(inkomsten)
print(f"De totale inkomsten zijn: {totaal_inkomsten}")

print(presenteer(inkomsten,totaal_inkomsten))

with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])