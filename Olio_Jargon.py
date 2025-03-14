# class Talo:
#     def __init__(self):
#         self.kissat = []
#         
# class Kissa:
#     def __init__(self):
#         self.nimi = "eioleviela"
#         self.poikaset = [] #tyhjä aluksi
#         #täytetään viidellä poikasella
#         self.koti = 0
#         self.nalka = 0
#     def aantely(self):
#         print("Miau!")
#     def syonti(ruoka):
#         self.nalka -= ruoka.paino
#         
# class Hiiri:
#     def __init__(self):
#         self.paino = 100
# 
# munkoti = Talo()
# munkissa = Kissa()
# munkissa.nimi = "Miisu"
# munkissa.koti = munkoti
# munkoti.kissat.append(munkissa)
# peltohiiri = Hiiri()
# munkissa.syonti(peltohiiri)
# 
# for n in range(5):
#     poikanen = Kissa() #kaikki poikaset on eri olioita
#     munkissa.poikaset.append(poikanen)


# class Peli:
#     #luokan ominaisuus tulee tähän, joka on kaikilla olioilla sama
#     laatikon_materiaali = "Pahvi"
#     def __init__(self):
#         self.rahat = 1000 # ominaisuuksia/attribuutteja
#     def siirto(self):
#         print("Heitetään noppaa!")
#     
# monopoli = Peli()
# print(monopoli.rahat)
# monopoli.siirto()


# class Teline:
#     def __init__(self):
#         self.paperit = []
#         #täytä paperit-luokan lista
#         for p in range(10):
#             paperi = Paperi()
#             self.paperit.append(paperi)
#     # toiminnallisuus joka antaa paperit ja varoittaa vähyydestä
#     def anna_paperi(self):
#         if len(self.paperit) > 5:
#             annettava_paperi = self.paperit.pop() # pop palauttaa poistamansa!
#         else:
#             annettava_paperi = "EI OLE" #huono ratkaisu
#             print("PIIP!")
#         return annettava_paperi
# class Paperi:
#     def __init__(self):
#         self.kuivuus = 1
# 
# 
# class Ihminen:
#     def __init__(self):
#         pass
# 
# luokanteline = Teline()
# for n in range(10):
#     ykspaperi = luokanteline.anna_paperi()
#     print(ykspaperi)


# käytä olioissa
# self.kurssin_oppilaat_srt = sorted(self.kurssin_oppilaat, key=lambda oppilas: oppilas.arvosana, reverse=True)



import turtle
 
pekka = turtle.Turtle()
pekka.penup() #nostaa kynan, ei jälkeä
pekka.pendown() #laskee kynan, eli jälkeä jää
 
#esimerkiksi P tehdaan nain
pekka.left(90)
pekka.forward(100)
pekka.right(90)
pekka.fd(50)
pekka.right(90)
pekka.fd(50)
pekka.right(90)
pekka.fd(50)
 
#KIRJOITA NIMESI turtlella
#TEE alkuperäisestä turtlesta aliluokka, jolle teet seuraavanlaisen metodin:
#kayta ohjaukseen taulukkoa seuraavasti
#[pendown/penup,eteenpain,vasen/oikea,kulma]
#["pd","v",90,100,"pd,"r",90,50,  #yllaolevat rivit 7-10
 
#TEE FUNKTIO, jolla annetaan ylläolevaa muotoa oleva taulukko ja se piirtää turtlella nimesi
 
class OmaTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Kutsutaan Turtle-luokan alustajaa
    
    def piirranimi(self, nimitaulukko):
         #KOODAA TAMA
 
pekka = OmaTurtle() #Pekka on kilpikonna






























