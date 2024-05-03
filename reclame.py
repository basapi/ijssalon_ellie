def aanbieding_1(smaak, prijs, korting):
    korting_bedrag = prijs * korting
    prijs_met_korting = prijs - korting_bedrag

    uitvoer = f"In de aanbieding: emmertje ijs (1 liter) in de smaak {smaak} van {prijs} voor {prijs_met_korting}"
    return uitvoer

print(aanbieding_1("Aarbei", 4, 0.1))

def inkomsten_totaal(inkomsten):
    totaal = sum(inkomsten)
    return totaal

de_inkomsten = [220, 430, 125, 160, 205 ,90, 345]

print(f"{inkomsten_totaal(de_inkomsten)}")



def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    totaal_met_btw = totaal + btw_bedrag
    return f"Het totaal van alle inkomsten van deze week is {totaal_met_btw} euro, waarover {btw_bedrag} euro btw betaald moet worden."
   
    
    

inkomsten = [220, 430, 125, 160, 205 ,90, 345]
btw = 0.09 
print(inkomsten_totaal(inkomsten, btw))


def laag_en_hoog(mijn_lijst):
    hoog = max(mijn_lijst)
    laag = min(mijn_lijst)
    return hoog,laag

mijn_lijst = [220, 430, 125, 160, 205 ,90, 345]

print(laag_en_hoog(mijn_lijst))



def gemiddelde(mijn_lijst):
    totale_inkomsten = sum(mijn_lijst)
    gemiddelde = totale_inkomsten / len(mijn_lijst)
    return gemiddelde

mijn_lijst = [220, 430, 125, 160, 205 ,90, 345]

gemiddelde = gemiddelde(mijn_lijst)

print(gemiddelde)

def gemiddelde(mijn_lijst):
    totale_inkomsten = sum(mijn_lijst)
    gemiddelde = totale_inkomsten / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."

mijn_lijst = [220, 430, 125, 160, 205 ,90, 345]

gemiddelde = gemiddelde(mijn_lijst)

print(gemiddelde)

def hoog_en_laag(invoer_lijst):
    hoogste_waarde = max(invoer_lijst)
    laagste_waarde = min(invoer_lijst)
    return [hoogste_waarde, laagste_waarde]

def meervoudig(invoer_lijst):
    return hoog_en_laag(invoer_lijst)

print(meervoudig([10,5,3,2,1,2,9]))

from algemene_functies import mijn_functie_2    

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    return mijn_functie_2(korte_lijst)











