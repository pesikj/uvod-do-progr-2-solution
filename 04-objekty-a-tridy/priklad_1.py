"""
Uvažuj, že navrhuješ software pro zásilkovou společnost.

Vytvoř třídu Balik, která bude mít tři atributy - adresa, hmotnost a doruceno. 
První dva atributy nastav pomocí parametrů funkce __init__. Parametr doruceno nastav na začátku jako False.

Připoj ke třídě funkci doruc, která změní hodnotu parametru doruceno na True.

Přidej funkci getInfo, která vypíše adresu, hmotnost a informaci o tom, zda byl balík již doručen.

Zkus si vytvořit nějaké objekty ze třídy Balik a ověř, že vše funguje.
"""


class Balik:
  def doruc(self):
    self.doruceno = True
  def __str__(self):
    if self.doruceno:
      doruceno_text = "Balík byl doručen"
    else:
      doruceno_text = "Balík zatím nebyl doručen."
    return "Balík je na adresu {self.adresa} a váží {self.hmotnost}. {doruceno_text}"
  def __init__(self, adresa, hmotnost):
    self.adresa = adresa
    self.hmotnost = hmotnost
    self.doruceno = False

