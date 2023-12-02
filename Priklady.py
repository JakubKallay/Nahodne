import time
z = 3
def Vypisanie():
    print("""Vyber si príklady na:
    1.Sčítanie
    2.Očítanie
    3.Násobenie
    4.Delenie
    """)
def Vyber_funkcie():
    x = input("Ktorú funckiu si vyberáš?(napíš číslo): ")
def prvý_príklad():
    while True:
        print(a,"+",b)
        y = float(input("Aký je výsledok?: "))
        if y == a+b:
            y = print("Správne, chceš ďalší príklad?(áno/nie): ")
            if z == "áno":
                continue
            else:
                Vypnutie()
        else:
            Zivoty()
def Vypnutie():
    print("Kalkulačka sa vypne za 3")
    time.sleep(0.7)
    print("                       2")
    time.sleep(0.7)
    print("                       1")
    time.sleep(0.7)
    exit()

def Zivoty():
    z = z - 1
    if z > 0:
        print("Stratil si 1. život")
    else:
        print("Ztratil si posledný život")
        Vypnutie()
