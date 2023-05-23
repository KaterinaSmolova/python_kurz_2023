class Auto:
    def __init__(self, registracni_znacka, znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.znacka = znacka
        self.dostupne = True
    
    def pujc_auto(self):
        self.dostupne = False

    def __str__(self):
        if self.dostupne:
            dostupneText = "Potvrzuji zapůjčení vozidla"
        else:
            dostupneText = "Vozidlo není k dispozici"

        auto1 = Auto("4A2 3020", "Peugeot", "Cabrio", "47534" ) 
        auto2 = Auto("1P3 4747", "Škoda", "Octavia", "41253")

    def get_info(self):
        return(self.registracni_znacka, self.typ_vozidla)




znacka = input("Jakou značku vozu si chcete půjčit?")

