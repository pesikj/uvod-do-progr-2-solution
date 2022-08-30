"""
Pokračuj ve své práci pro zásilkovou společnost. Společnost nově doručuje i cenné balíky, 
které mají zadanou určitou hodnotu.

Vytvoř třídu ValuablePackage, která dědí od třídy Package. ValuablePackage má navíc atribut value, 
ostatní atributy dědí od třídy Package.
Atribut value nastav pomocí funkce __init__. Ostatní parametry předej funkci __init__ třídy Package.
Vytvoř si alespoň jeden objekt a zkus volání jeho funkcí.
"""

class Package:
  def doruc(self):
    self.doruceno = True
  def getInfo(self):
    if self.doruceno:
      doruceno_text = "Balík byl doručen"
    else:
      doruceno_text = "Balík zatím nebyl doručen."
    print(f"Balík je na adresu {self.adresa} a váží {self.hmotnost}. {doruceno_text}")
  def __init__(self, adresa, hmotnost):
    self.adresa = adresa
    self.hmotnost = hmotnost
    self.doruceno = False

class ValuablePackage(Package):
  def __init__(self, adresa, hmotnost, value):
    super().__init__(adresa, hmotnost)
    self.value = value

valuablePackage = ValuablePackage("Plzeňská 123, Praha", 2, 10000)
valuablePackage.getInfo()
valuablePackage.doruc()
valuablePackage.getInfo()
