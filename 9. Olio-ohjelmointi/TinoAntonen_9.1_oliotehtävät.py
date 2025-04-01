# Harjoitus 1: Perus olio ja lista
# Luo luokka Henkilo, jolla on attribuutit nimi ja ika. Luo sen jälkeen lista, johon lisäät kolme Henkilo-oliota.

# class Henkilo:
#     def __init__(self,henkilonNimi,henkilonIka):
#         self.nimi = henkilonNimi
#         self.ika = henkilonIka
# lista = []
# lista.append(Henkilo("Tino", 28))
# lista.append(Henkilo("Jukka", 55))
# lista.append(Henkilo("Kimmo", 90))
# print(lista)
        
# Harjoitus 2: Olioiden suodatus listassa
# Luo luokka Tuote, jolla on attribuutit nimi ja hinta.
# Luo lista Tuote-olioista ja kirjoita funktio, joka palauttaa listan kaikista tuotteista, joiden hinta on alle 10 euroa.

# class Tuote:
#     def __init__(self, tuotteenNimi,tuotteenHinta):
#         self.nimi = tuotteenNimi
#         self.hinta = tuotteenHinta
#         
# tuoteOliot = [Tuote("Juusto", 5), Tuote("Maito", 11), Tuote("Peruna", 2), Tuote("Korppu", 9), Tuote("Jauheliha", 10)]
# tulos = []
# def alle10():
#     for i in range(len(tuoteOliot)):
#         if tuoteOliot[i].hinta < 10:
#             tulos.append(tuoteOliot[i].nimi)
#     return tulos    
# print(alle10())

# Harjoitus 3: Metodit ja oliot
# Luo luokka Kirja, jolla on attribuutit kirjailija, nimi ja sivumaara.
# Lisää luokkaan metodi onkoPaksu, joka palauttaa True, jos kirjan sivumäärä on yli 300.
# Luo lista Kirja-olioista ja tulosta ne, jotka ovat paksuja.
# kirja1 (100), Matti 
# class Kirja:
#     def __init__(self, kirjailija, kirjanNimi, sivumaara):
#         self.kirjailija = kirjailija
#         self.nimi =kirjanNimi
#         self.sivumaara = sivumaara
#     def onkoPaksu(self):
#         if self.sivumaara > 300:
#             return True
#         return False
#     
# kirjat = [Kirja("Matti", "kirja1", 100), Kirja("Pentti", "kirja2", 340), Kirja("Jokke", "kirja3", 870), Kirja("Tomi", "kirja4", 290), Kirja("Esko", "kirja5", 303)]
# #kirjat[0].onkoPaksu()
# for i in range(len(kirjat)):
#     if kirjat[i].onkoPaksu():
#         print(F"{kirjat[i].nimi} ({kirjat[i].sivumaara}), {kirjat[i].kirjailija}")

# Harjoitus 4: Monimutkaisemmat  listat
# Luo luokka Oppilas, jolla on attribuutit nimi ja arvosanat (lista numeroita).
# Luo lista Oppilas-olioista ja kirjoita funktio, joka laskee ja palauttaa jokaisen oppilaan keskiarvon.

# class Oppilas:
#     nimi = "oppilas"
#     def __init__(self, oppilasNimi, arvosanat):
#         self.nimi = oppilasNimi
#         self.arvosanat = arvosanat
#         
#     def olioKeskiarvo(self):
#         summa = 0
#         for i in range(len(self.arvosanat)):
#             summa += self.arvosanat[i]
#         return summa / len(self.arvosanat)
# 
#         
# oppilaat = [Oppilas("Matti", [2,3,5,1]), Oppilas("Lauri", [5,2,3,3]), Oppilas("Kimmo", [1,1,2,3])]
# 
# for k in range(len(oppilaat)):
#     print(oppilaat[k].nimi +" "+ str(oppilaat[k].olioKeskiarvo()))
#     
# opiskelija = Oppilas("Tino", [2,3,4])
# print(opiskelija.nimi)
# print(opiskelija.arvosanat)
# print(opiskelija.olioKeskiarvo())

# Harjoitus 5: Yksilöllisyys listassa
# Luo luokka Auto, jolla on attribuutit rekisterinumero ja merkki.
# Varmista, että et lisää listalle kahta autoa, joilla on sama rekisterinumero.

class Auto:
    def __init__(self, rekisterinumero, merkki):
        self.rekisterinumero
        self.merkki
autolista = [Auto(313, Ruf), Auto(385, Mercury), Auto(962, Saleen), Auto(149, Holden)]

# Harjoitus 6: Olioiden järjestäminen listassa
# Luo luokka Opiskelija, jolla on attribuutit nimi ja opintopisteet.
# Luo lista Opiskelija-olioista ja järjestä se opintopisteiden mukaan laskevassa järjestyksessä.


class Opiskelija:
    def __init__(self, opiskelijanNimi,opintopisteet):
        self.nimi = opiskelijanNimi
        self.opintopisteet = opintopisteet
        
pistemaara = [Opiskelija("Heikki", 100), Opiskelija("Lassi", 350), Opiskelija("Antti", 203), Opiskelija("Veikko", 25)]    
    
    
    
    
    
    
    