"""
Zkus pro našeho nakladatele vytvořit software s využitím tříd a objektů. 
Vytvoř tedy třídu Kniha, která reprezentuje knihu. Každá kniha bude mít atributy nazev, 
pocet_stran a cena. Hodnoty nastav ve funkci __init__.

Přidej knize funkci getInfo, která vypíše informace o knize v nějakém pěkném formátu.
Občas se stane, že se kniha moc neprodává a knihkupec se snaží nalákat kupující slevou. 
Přidej funkci sleva, která bude mít jeden parametr - velikost slevy v procentech. 
Funkce sníží cenu knihy o dané procento.
"""

class Kniha:
  def sleva(self, sleva_v_procentech):
    self.cena *= (1 - sleva_v_procentech/100)
  def __str__(self):
    print(f"Název knihy: {self.nazev}. Počet stran: {self.pocet_stran}. Cena: {self.cena}")
  def __init__(self, nazev, pocet_stran, cena):
    self.nazev = nazev
    self.pocet_stran = pocet_stran
    self.cena = cena

kniha = Kniha("Noc, která mě zabila", 590, 499)
print(kniha)
kniha.sleva(10)
print(kniha)
