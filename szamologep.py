def osszeadas():
    #adatbekérés
    print("-"*20)
    szam1 = int(input("Kérek egy számot: "))
    print("-" * 20)
    szam2 = int(input("Kérek egy másik számot: "))
    print("-" * 20)
    #számolás
    osszeg = szam1 + szam2
    #kiírás
    print("-" * 20)
    print(f"{szam1}+{szam2}={osszeg}")
    print("-" * 20)

def kivonas():
    #adatbekérés
    print("-"*20)
    szam1 = int(input("Kérek egy számot: "))
    print("-" * 20)
    szam2 = int(input("Kérek egy másik számot: "))
    print("-" * 20)
    #számolás
    osszeg = szam1 + szam2
    #kiírás
    print("-" * 20)
    print(f"{szam1}-{szam2}={osszeg}")
    print("-" * 20)

def szamologep():
    #adatbekérés
    szam1 = int(adatbekeres("Adj meg egy számot: "))
    muvjel = adatbekeres("Add meg a műveleti jelet: ")
    szam2 = int(adatbekeres("Adj meg még egy számot: "))

    #számolás
    szoveg = ""
    eredmeny = 0
    if muvjel == "+":
        eredmeny = szam1 + szam2
    elif muvjel == "-":
        eredmeny = szam1 - szam2
    elif muvjel == "*":
        eredmeny = szam1 * szam2
    elif muvjel == "/":
        eredmeny = szam1 / szam2
    else:
        szoveg = "nem éretlmezhető a művelet"

    #kiírás
    kiiras(szam1, muvjel, szam2, eredmeny, szoveg)

def adatbekeres(szoveg):
    print("-" * 20)
    kismacska = input(szoveg)
    return kismacska


def kiiras(szam1, muvjel, szam2, eredmeny, szoveg):
    print("-" * 20)
    if szoveg == "":
        print(f"{szam1}{muvjel}{szam2}={eredmeny}")
    else:
        print(szoveg)

    print("-" * 20)

