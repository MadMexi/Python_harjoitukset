# Esimerkkeja

# class Opiskelija:
#     nimi = "Tino"
#     aloitusVuosi = 2025
# a = Opiskelija()
# print(a.nimi)
# 
# b = Opiskelija()
# b.nimi = "Aarni"
# print(b.nimi)

# class Opiskelija:
#     def __init__(self,opiskelijanNimi,aloitusvuosi):
#         self.nimi = opiskelijanNimi
#         self.aloitusvuosi = aloitusvuosi
#     def tulosta(self):
#         print(self.nimi + " " + str(self.aloitusvuosi))
# 
# a = Opiskelija("Tino", 2025)
# print(a.tulosta())
# opiskelija =[
#     Opiskelija("Aarni",2016),
#     
# ]

# class OpettajaOlio():
#     def __init__(self,opettajanNimi):
#         self.nimi = opettajanNimi
#     def tiedot(self):
#         return self.nimi
# 
# opettajat = [
#     OpettajaOlio("Kari"),    
#     OpettajaOlio("Aarni")
# ]
# class KurssiOlio():
#     def __init__(self,kurssinNimi,opettajaLista):
#         self.kurssi = kurssinNimi
#         self.Opettajat = opettajaLista
#     def tiedot(self):
#         tulos = self.kurssi + ": "
#         for i in range(len(self.Opettajat)):
#             tulos += self.Opettajat[i].tiedot()
#             if i != len(self.Opettajat) - 1:
#                 tulos += ", "
#         return tulos
# kurssit = [
#     KurssiOlio("ohjelmointi", [opettajat[0],opettajat[1]]),
#     KurssiOlio("matematiikka", [opettajat[0]])
# ]
# 
# class OppilasOlio():
#     def __init__(self,oppilaanNimi,kurssiLista):
#         self.oppilas = oppilaanNimi
#         self.kurssit = kurssiLista
#     def TulostaTiedot(self):
#         tulos = self.oppilas + "\n"
#         for i in range(len(self.kurssit)):
#             tulos += "-" + self.kurssit[i].tiedot() + "\n"
#         return tulos
# oppilaat = [
# OppilasOlio("Tino", [kurssit[0], kurssit[1]]),
# OppilasOlio("Daniel", [kurssit[1]])
# ]
# 
# print(oppilaat[0].TulostaTiedot())





#Kaksi luokkaa, tiimi ja työntekija.
#Työntekijalla muuttujina tuntipalkka ja työtunnit. Työntekijalla myös funktio, joka palauttaa kokonaispalkan
#Tiimilla lista työntekijöista ja funktio, joka palauttaa tiimin jasenten kokonaispalkan.
#Lista tiimeista.
#Funktio kalleinTiimi(), joka palauttaa kalleimman tiimin indeksin.

class Tyontekija:
    def __init__(self, tuntipalkka, tyotunnit):
        self.tuntipalkka = tuntipalkka
        self.tyotunnit = tyotunnit

    def kokonaispalkka(self):    # työtunnit * tuntipalkka
        return self.tyotunnit * self.tuntipalkka
    
class Tiimi:
    def __init__(self, tyontekijat):
        self.Tyontekijat = tyontekijat 

    def tiimiPalkka(self):
        tulos = 0
        for i in range(len(self.Tyontekijat)):
            tulos += self.Tyontekijat[i].kokonaispalkka()
        return tulos
    
def kalleinTiimi(tiimilista):
    indexi = 0
    suurin = tiimilista[0].tiimiPalkka()
    for i in range(1, len(tiimilista)):
        if tiimilista[i].tiimiPalkka() > suurin:
            suurin = tiimilista[i].tiimiPalkka()
            indexi = i
    return indexi
        
        
        
Tiimit = [Tiimi([Tyontekija(13, 16), Tyontekija(10, 9), Tyontekija(15, 20)]),
          Tiimi([Tyontekija(12, 11), Tyontekija(11, 5), Tyontekija(18, 35)]),
          Tiimi([Tyontekija(12, 77), Tyontekija(11, 123), Tyontekija(18, 33)])]

print(kalleinTiimi(Tiimit))

