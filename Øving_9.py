import datetime
from datetime import datetime
starttidspunkt = datetime


 #d)
class Avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet_min):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet_min = varighet_min


#e)
    def __str__(self):
        return f"Avtalen: {self.tittel} -- Lokasjon: {self.sted} -- Starter: {self.starttidspunkt} -- Varighet: {self.varighet_min} minutter"

#f)

def nyavtale():
    while True:
        try:
            tittel = input("Avtale tittel: ")
            sted = input("lokasjon: ")
            starttidspunkt = datetime.fromisoformat(input("Dato i format: YYYY-MM-DD"))
            varighet_min = int(input("Møte varigeht i min: "))
            break
        except ValueError:
            print("Varighet skal oppgis som et positivt heltall, og dato må være i formatet (YYYY-MM-DD)")
        except KeyboardInterrupt:
            return None

    avtale1 = Avtale(tittel, sted, starttidspunkt, varighet_min)
    return avtale1

#g)
avtaleListe = list()
a1 = Avtale("a1", "stavanger", datetime.fromisoformat("2000-04-02"),30)
a2 = Avtale("a2", "bergen", datetime.fromisoformat("2001-04-02"), 20)
a3 = Avtale("a3", "randomplass", datetime.fromisoformat("2002-04-02"), 20)
avtaleListe.append(a1)
avtaleListe.append(a2)
avtaleListe.append(a3)

liste1 = list()
def listeAvtale(liste, overskrift=""):

    j = 0
    print(overskrift)
    for avtalene in liste:

        print(j, ":", avtalene)
        j = j + 1


#print(*liste1, sep="\n")   #kan printe ut sånn istedet for forloop.

#h)
def lagretilfil(liste=list):
    with open("avtale.txt", "w") as fil1:
        fil1.write("Avtalebok \n")

        for objekter in avtaleListe:
            fil1.write(f"{objekter.tittel}; {objekter.sted};{objekter.starttidspunkt}; {objekter.varighet_min}\n")

lagretilfil(avtaleListe)

#i)
def lesefrafil():
    liste = list()
    with open("avtale.txt", "r") as fil1:
        for linje in fil1:
            ord = linje.strip("\n").split(";")
            liste.append(ord)
            print(liste)

#j)

def sammeDatoAdder(liste):
    listeSammeDato = list()
    dato = datetime.fromisoformat(input("Hvilken dato leter du etter YYYY-MM-DD: "))

    for avtalene in liste:
        if dato == avtalene.starttidspunkt:
            listeSammeDato.append(avtalene)
    return listeSammeDato


#k)
def sammeNavnAvtaler(liste):
    listeSammeNavn = list()
    avtalenavn = input("Hvilken avtaler leter du etter?")

    for avtalene in liste:
        index = avtalene.tittel.find(avtalenavn)
        if index != -1:
            listeSammeNavn.append(avtalene)
    return listeSammeNavn

#l)
def menysystem():
    while True:
        valg = int(input("velg nummer: 1=lese inn avtaler fra fil. 2 = skrive avtalene til fil. 3 = skrive inn en ny avtale. 4 = skrive ut alle avtalene. 5 = avslutt"))
        if valg == 1:
            lesefrafil()
        if valg == 2:
            lagretilfil(nyavtale())
        if valg == 3:
            avtale_temp = nyavtale()
            if avtale_temp:
                avtaleListe.append(avtale_temp)
        if valg == 4:
            for index, avtale in enumerate(avtaleListe):
                print(f"Avtale nr. {index}: {avtale}")

        if valg == 5:
            break
menysystem()

#m)
def slettemeny():
    listeAvtale(avtaleListe, "slette avtale")
    sletteindex = int(input("indeks til avtalen du vil slette: "))
    del avtaleListe[sletteindex]
slettemeny()

def redigeringsmeny():
    i = int(input("velg index til avtalen du vil redigere: "))
    changeAvtale = avtaleListe[i]
    print(changeAvtale)
    changeAvtale.tittel = input("skriv inn en ny tittel: ")
    changeAvtale.sted = input("Skriv ny lokasjon: ")
    starttidspunktny = datetime.fromisoformat(input("Dato i format: YYYY-MM-DD"))
    changeAvtale.starttidspunkt = starttidspunktny
    changeAvtale.varighet_min = int(input("ny varighet: "))
