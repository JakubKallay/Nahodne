import time

a = 2
b = 4
z = 3
def Zivoty():
    r = z - 2
    if r == 1:
        print("Stratil si 1. život")
    else:
        print("Ztratil si posledný život")
        Vypnutie()
def Vypisanie():
    print("""Vyber si príklady na:
    1.Sčítanie
    2.Očítanie
    3.Násobenie
    4.Delenie
    """)
def Vyber_funkcie():
    x = int(input("Ktorú funckiu si vyberáš?(napíš číslo): "))
def Prvý_príklad():
    z = 3
    while True:
        print(a,"+",b)
        y = float(input("Aký je výsledok?: "))
        if y == a+b:
            pokracovanie = input("Správne, chceš ďalší príklad?(áno/nie): ")
            if pokracovanie == "áno":
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



Vypisanie()
Vyber_funkcie()
Prvý_príklad()


#Ivanova mama je tlsta