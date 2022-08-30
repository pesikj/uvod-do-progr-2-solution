"""
Gustav je vášnivým čtenářem detektive z našeho nakladatelství a navíc si zapisuje knihy, které přečetl. Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.

- Napiš program, který spočte celkový počet stran, které Gustav přečetl.
- Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.

Knihas = [
    {"nazev": "Vražda s příliš mnoha notami", "pocet_stran": 450, "rating": 5},
    {"nazev": "Vražda podle knihy", "pocet_stran": 524, "rating": 9},
    {"nazev": "Past", "pocet_stran": 390, "rating": 4},
    {"nazev": "Popel popelu", "pocet_stran": 411, "rating": 10},
    {"nazev": "Noc, která mě zabila", "pocet_stran": 159, "rating": 7},
    {"nazev": "Vražda, kouř a stíny", "pocet_stran": 258, "rating": 6},
    {"nazev": "Zločinný steh", "pocet_stran": 542, "rating": 8},
    {"nazev": "Zkus mě chytit", "pocet_stran": 247, "rating": 7},
    {"nazev": "Vrah zavolá v deset", "pocet_stran": 396, "rating": 6},
]
"""

Knihas = [
    {"nazev": "Vražda s příliš mnoha notami", "pocet_stran": 450, "rating": 5},
    {"nazev": "Vražda podle knihy", "pocet_stran": 524, "rating": 9},
    {"nazev": "Past", "pocet_stran": 390, "rating": 4},
    {"nazev": "Popel popelu", "pocet_stran": 411, "rating": 10},
    {"nazev": "Noc, která mě zabila", "pocet_stran": 159, "rating": 7},
    {"nazev": "Vražda, kouř a stíny", "pocet_stran": 258, "rating": 6},
    {"nazev": "Zločinný steh", "pocet_stran": 542, "rating": 8},
    {"nazev": "Zkus mě chytit", "pocet_stran": 247, "rating": 7},
    {"nazev": "Vrah zavolá v deset", "pocet_stran": 396, "rating": 6},
]

totalpocet_stran = 0
for Kniha in Knihas:
  totalpocet_stran += Kniha["pocet_stran"]
print(f"Gustav celkem přečetl {totalpocet_stran} stran.")

print("Knihy, které hodnocení 8 a více:")
for Kniha in Knihas:
  if Kniha["rating"] >= 8:
    print(Kniha["nazev"])