import time

a = 2
b = 4
z = 3
def Zivoty():
    z = z-1
    if z == 0:
        print("Stratil si posledný život")
        Vypnutie()
    else:
        print("Stratil si jeden život")

def Vypisanie():
    print("""Vyber si príklady na:
    1.Sčítanie
    2.Očítanie
    3.Násobenie
    4.Delenie
    """)


def Prvý_príklad():

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
chleba = int(input("Ktorú funckiu si vyberáš?(napíš číslo): "))
if chleba == 1:
    Prvý_príklad()
else:
    exit()


#Ivanova mama je tlsta