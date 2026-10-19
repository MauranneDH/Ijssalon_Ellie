from algemene_functies import mijn_functie_2
def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro!"

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal:.2f} euro, waarover {bedrag:.2f} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return [laagste, hoogste]

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gemiddelde_bedrag = totaal / aantal
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_bedrag:.2f} euro."

def meervoudig(invoer_lijst):
    kort = laag_en_hoog(invoer_lijst)
    return [kort[1], kort[0]]

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    korte_lijst = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return korte_lijst