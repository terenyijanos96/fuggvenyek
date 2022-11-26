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
    szam1 = float(adatbekeres("Adj meg egy számot: "))
    muvjel = adatbekeres("Add meg a műveleti jelet: ")
    szam2 = float(adatbekeres("Adj meg még egy számot: "))

    #számolás
    szoveg = ""
    eredmeny = 0
    match muvjel:
        case "+": eredmeny = osszead(szam1, szam2)
        case "-": eredmeny = kivon(szam1, szam2)
        case "*": eredmeny = szoroz(szam1, szam2)
        case "/": eredmeny = oszt(szam1, szam2)
        case _: szoveg = "nem éretlmezhető a művelet"

    #kiírás
    kiiras(szam1, muvjel, szam2, eredmeny, szoveg)

"""paraméter adás"""
def adatbekeres(szoveg):
    print("-" * 20)
    kismacska = input(szoveg)  # a tanárnő adta meg kismacskának xd
    return kismacska


def kiiras(szam1, muvjel, szam2, eredmeny, szoveg):
    print("-" * 20)
    if szoveg == "":
        print(f"{szam1}{muvjel}{szam2}={eredmeny}")
    else:
        print(szoveg)

    print("-" * 20)


def osszead(a, b):
    return a + b


def kivon(a, b):
    return a - b


def szoroz(a, b):
    return a * b


def oszt(a, b):
    return a / b

