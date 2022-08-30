"""
Naše firma se rozhodla zaměstnávat i pracovníky na částečné úvazky, 
pro které bude vytvořena zvláštní třída. Vytvoř novou třídu Brigadnik, 
která bude dědit od třídy Zamestnanec a bude mít navíc atribut uvazek (float), 
který reprezentuje velikost úvazku oproti plnému. 
Přidej informaci o úvazku k výpisu informací do funkce getInfo.
"""

class Zamestnanec:
  def cerpej_dovolenou(self, pocet_hodin):
    if self.dovolena >= pocet_hodin:
      self.dovolena -= pocet_hodin
      return f"Užij si to."
    else:
      return f"Bohužel už máš nárok jen na {self.dovolena} dní."
  def __str__(self):
    return f"{self.jmeno} pracuje na pozici {self.pozice}."
  def __init__(self, jmeno, pozice):
    self.jmeno = jmeno
    self.pozice = pozice
    self.dovolena = 25

class Brigadnik(Zamestnanec):
  def __str__(self):
    return f"{super().getInfo()} Má úvazek {self.uvazek}."
  def __init__(self, jmeno, pozice, uvazek):
    super().__init__(jmeno, pozice)
    self.uvazek = uvazek

brigadnik = Brigadnik("Jan Dvořák", "asistent", 0.5)
print(brigadnik)
