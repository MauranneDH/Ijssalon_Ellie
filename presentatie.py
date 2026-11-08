def presenteer(inkomsten, totaal):
        for naam, bedrag in inkomsten.items():
            print(f"{naam} : {bedrag} euro")

        print("=" * 25)
        print(f"totaal : {totaal} euro") 
    