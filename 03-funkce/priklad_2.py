""" 
Napiš funkci totalcena, která vypočte cenu noci v hotelu. 
Funkce bude mít dva parametry - persons (typ int) a breakfast (typ bool). 
Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. 
Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.

Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. totalcena(3), totalcena(2, True).
"""

def totalcena(persons, breakfast=False):
  cenaPerPerson = 850
  if breakfast:
    cenaPerPerson += 125
  return cenaPerPerson * persons

print(totalcena(3))
print(totalcena(3, True))
