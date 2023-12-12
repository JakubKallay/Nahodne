import random
import time
z = 3
def Vypisanie():
    print("""Vyber si príklady na:
    1.Sčítanie
    2.Odčítanie
    3.Násobenie
    4.Delenie
    """)

def Zivoty():
    global z
    z= z-1
    if z >= 1:
        time.sleep(0.7)
        print("Nesprávne, stratil si 1 život")
    else:
        time.sleep(0.7)
        print("Nesprávne, strácaš posledný život")
        Vypnutie()
def Prvý_príklad():
    while True:
        a = random.randint(1,1000)
        b = random.randint(1,1000)
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

def Druhý_príklad():
    while True:
        a = random.randint(1,1000)
        b = random.randint(1,1000)
        print(a,"-",b)
        y = float(input("Aký je výsledok?: "))
        if y == a-b:
            pokracovanie = input("Správne, chceš ďalší príklad?(áno/nie): ")
            if pokracovanie == "áno":
                continue
            else:
                Vypnutie()
        else:
            Zivoty()

def Tretí_príklad():

    while True:
        a = random.randint(1,30)
        b = random.randint(1,30)
        print(a,"*",b)
        y = float(input("Aký je výsledok?: "))
        if y == a*b:
            pokracovanie = input("Správne, chceš ďalší príklad?(áno/nie): ")
            if pokracovanie == "áno":
                continue
            else:
                Vypnutie()
        else:
            Zivoty()

def Štvrtý_príklad():
    while True:
        a = random.randint(1,1000)
        b = random.randint(1,30)
        print(a,"/",b)
        y = float(input("Aký je výsledok?: "))
        if y == a/b:
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


chleba = int(input("Ktorú funckiu si vyberáš?(napíš číslo): "))
if chleba == 1:
    Prvý_príklad()
if chleba == 2:
    Druhý_príklad()
if chleba == 3:
    Tretí_príklad()
if chleba == 4:
    Štvrtý_príklad()


