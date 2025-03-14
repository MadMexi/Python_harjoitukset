# a = 12
# b = 23
# sana = "kissa"
# tulos = a + b
# print ("Tulos:",tulos)
# 
# #len palauttaa taulukon pituuden
# #append lisää tauluun yhden solun
# taulu = [12,23,34,45,"kissa"]
# tt = [[1,2,3,4],[10,20,30,40]]
# 
# #ehdot
# if a == b:
#     print("a on b")
# if a != b:
#     print("a ei ole b!")
# if a < b:
#     print("a on pienempi kuin b")
# if a > b:
#     print("a on suurempi kuin b")
#     
# #ehtojen yhdist. and, or , not , in
# a,b,c,d = 10,20,30,40
# if a < b and c < d:
#     print(a pienmpi b ja c pienempi d)
# 
# #in ja not in liittyy taulukoihin
# suurpedot = ["kettu","susi","ahma","karhu"]
# #onko mäyrä suurpeto
# if "mäyrä" in suupedot:
#     print("Mäyrä on suurpeto")
# if "mäyrä" not in suupedot:
#     print("Mäyrä ei ole suurpeto")
#     
# huone = "pimeä" #"valoisa"
# lampo = "lämmin" #"kylmä"
# 
# if huone == "pimeä":
#     if lampo =="lämmin":
#         print("huone on pimeä ja lämmin")
#     
# if huone == "valoisa":
#     if lampo == "lämmin"
#     print("huone on valoisa ja lämmin")
#     if lampo == "kylmä":
#         print("huone on valoisa ja kylmä")
#     #lämpö on lämmin
#     #lämpö on kylmä
    
# #while

# laskuri = 0
# while laskuri < 10:
#     print("laskurin arvo",laskuri)
#     laskuri = laskuri + 1
#     
# #tee laskuri while joka tulostaa luvut 3,6,9,12,15
# laskuri = 3
# while laskuri <= 15:
#     print(laskuri)
#     laskuri = laskuri + 3
    
# taulu = [10, 20, 30 ,40 ,50 ,60 ,70]    
# #taulukon läpikäynti
# 
# laskuri = 0
# while laskuri < len(taulu):
#     print("taulun arvo paikassa:", laskuri, "on:",taulu[laskuri])
#     laskuri = laskuri + 1

# laskuri = 0
# while laskuri < 30:
#     print(laskuri,"jakojäännös 2:lla on: ", laskuri % 2)
#     laskuri += 1

#valitse taulukosta kaikki luvut jotka ovat pienempiä kuin 10 ja laita ne uuteen tauluun
# taulu = [34, 45, 78, 90,1,3,2,5,47,10,9]
# uusi = []
# isot = []
# uudetIsot = []
# laskuri = 0
# while laskuri < len(taulu):
#     #kuinka valitaan ehto
#     kokeilu_luku = taulu[laskuri]
#     if kokeilu_luku < 10:
#         uusi.append(kokeilu_luku)
#     if kokeilu_luku >= 10:
#         isot.append(kokeilu_luku)
#     if kokeilu_luku > 40:
#         uudetIsot.append(kokeilu_luku)
#     
#     laskuri += 1

#tee 2 listaa ja laita annetusta taulusta niihin parittomat ja parilliset luvut

# taulu = [34, 45, 78, 90, 1, 3, 2, 5, 47, 10, 9]
# parittomat = []
# parilliset = []
# laskuri = 0
# while laskuri < len(taulu):
#     kokeilu_luku = taulu[laskuri]
#     if kokeilu_luku % 2 == 0:
#         parilliset.append(kokeilu_luku)
#     if kokeilu_luku % 2 == 1:
#         parittomat.append(kokeilu_luku)
#     laskuri += 1

# #kaksi eri taulukkoa kissat ja niiden painot, ne ovat samanmittaiset ja yhdistä ne
# 
# kissat = ["Matti", "Teppo", "seppo", "Heikki", "Timppa"]
# painot = [4,3,2,7,8]
# yhd = []
# laskuri = 0
# while laskuri < 5: 
#     osoitin = kissat[laskuri]   
#     yhd.append(osoitin)
#     osoitin = painot[laskuri]
#     yhd.append(osoitin)
#     laskuri += 1
     
# def sanaprintti(sana,toinensana):
#     print(sana,toinensana)
# sanaprintti("Thonny on", "paras")

# def summa(a,b):
#     tulos = a + b
#     return tulos
# def erotus(c,d):
#     tulos = a - b
#     return tulos
# def kerto(a,b):
#     tulos = a * b
#     return tulos
# def jako(a,b):
#     tulos = a // b #/ jakaa liukuluvuilla // jakaa kokonais luvuilla
#     return tulos
# 
# def tupleihme():
#     return 100,"Miisu",40
# 
# ihmetulos = tupleihme()
# print(ihmetulos)

# munlista = [10, 20, 30, 40]
# def listatulostaja(jokulista): #jokulista muuttuja on funktion sisäinen
#     print(jokulista)
# listatulostaja(munlista)

# # tee funktio joka palauttaa annetusta listasta listana ne luvut jotka ovat alle ylärajan
# def pienet(lukulista,raja):
#     tulos = []
#     laskuri = 0
#     while laskuri < len(lukulista):
#         kokeilualkio = lukulista[laskuri]
#         if kokeilualkio < raja:
#             tulos.append(kokeilualkio)
#         laskuri += 1
#     return tulos

# #tee sama mutta vain ylä ja alarajalla ja palauttaa tuplena kaksi listaa alarajasta alaspäin ja alarajasta ylöspäin
# def pienet(lukulista,alaraja,ylaraja):
#     pienettulos = []
#     isottulos = []
#     laskuri = 0
#     while laskuri < len(lukulista):
#         kokeilualkio = lukulista[laskuri]
#         if kokeilualkio < alaraja:
#             pienettulos.append(kokeilualkio)
#         if kokeilualkio > ylaraja:
#             isottulos.append(kokeilualkio)
#         laskuri += 1
#     return pienettulos,isottulos
# tulosjotain = pienet([1,2,3,4,10,6,25,63],3,11)
# print(tulosjotain)

# #tee sama ilman raja-arvoja kahdella listalla mihin menee parilliset ja parittomat luvut 
# def erittely(lukulista):
#     parittomat = []
#     parilliset = []
#     laskuri = 0
#     while laskuri < len(lukulista):
#         kokeilualkio = lukulista[laskuri]
#         if kokeilualkio % 2 == 0:
#             parilliset.append(kokeilualkio)
#         if kokeilualkio % 2 == 1:
#             parittomat.append(kokeilualkio)
#         laskuri += 1
#     return parittomat,parilliset
# jotain = erittely([1,2,3,45,4,5,65,63,85,41])
# print(jotain)

# #erottele data tyypin perusteella kahteen listaan
# def lista (myyntilista):
#     autot = []
#     hinnat = []
#     laskuri = 0
#     while laskuri < len(myyntilista):
#         osoitin = myyntilista[laskuri]
#         if type(osoitin) == str:
#             autot.append(osoitin)
#         if type(osoitin) == int:
#             hinnat.append(osoitin)
#         laskuri += 1
#     return autot,hinnat
# jotain = ["audi",100,"bmw",200,"dacia",400,"ford",500]
# print(lista(jotain))

#sinulla on kissoja Miisu, Jere, Lumipallo, Zorro, Santtu, Maija
#laita niille järjestyksessä rusetit (Sininen, Punainen, Vihreä)
#yhdistä rusetti ja kissa
#käytä jakojäännöstä koska rusetteja on kolme
#
# kissat = ["Miisu","Jere","Lumipallo","Zorro","Santtu","Maija"]
# rusetit = ["Sininen","Punainen","Vihreä"]

# def hienotkatit():
#     yhd = []
#     laskuri = 0
#     while laskuri < len(kissat):
#         pari = []
#         osoitin = kissat[laskuri]
#         rosoitin = rusetit[laskuri % len(rusetit)]
#         pari = [osoitin,rosoitin]
#         yhd.append(pari)
#         laskuri += 1
#     return yhd
# 
# tulos = hienotkatit()
# print(tulos)
# 
# x =0
# while x < 20:
#     print("x:",x, " x % 3:",x % 3, " kissat_taulukosta:",kissat[x % 3],"rusetin väri: ",rusetit [x % 3])
#     x += 1 


# import random
# random.seed(0)
# satluku = ranndom.randint(1,10)

# #funktio, joka reagoi globaaliin tilaan/statukseen/lippuun
# def tilaprintti():
#     if glippu == 0:
#         print("Tilanne vakaa nolla")
#     if glippu == 1:
#         print("Tilanne hutera, yksi")
# glippu = 0
# tilaprintti()
# glippu = 1
# tilaprintti()

#Tuntitehtävä "PUTSAA LISTA"
#listassa pitäisi olla vuorotellen auton merkki ja hinta ["Audi",200,"BMW",300,"Dacia",500]
#virheen vuoksi listassa on välillä liikaa numeroita
#["Audi",200,200,200,"BMW",300,300,300,300,"Dacia",400,400]
#tee funktio, joka palauttaa putsatun listan
#kayta apuna  pythonin type-funktiota, joka palauttaa alkion tyypin
# type(100) # <class 'int'>

# def putsaalista(autot):
#     putsattu = []
#     laskuri = 0
#     while laskuri < len(autot):
#         osoitin = autot[laskuri]
#         if type(osoitin) == str:
#             putsattu.append(osoitin)
#         if type(osoitin) == int and type(putsattu[len(putsattu) - 1]) == str:
#             putsattu.append(osoitin)
#         laskuri += 1       
#     return putsattu
# tulos = ["Audi",200,200,200,"BMW",300,300,300,300,"Dacia",400,400]
# print(putsaalista(tulos))
            
# min max skeida           
# munlista = [-1,20,30,40,50,60,70]
# 
# def isoin(annettu_lista):
#     isoinluku = annettu_lista[0]
#     indexi = 1
#     while indexi < len(annettu_lista):
#         if annettu_lista[indexi] > isoinluku: # jos nykyinen pakka listalla on suurempi kuin isoinluku
#             isoinluku = annettu_lista[indexi] # numero siirretään muuttujaan
#         indexi += 1
#     return isoinluku
# 
# isoinluku = isoin(munlista)
# print(isoinluku)

# joku funktio homma
# def kokeilu(annettu_lista)
#     summa = 0
#     for alkio in annettu_lista:
#         summa = summa + alkio
#     return summa

# rivin jako
# rivi = "kissa,10,20,30"
# 
# taulukko = rivi.split (",")
# print(taulukko)
# rivi = 1 120 parillinen"
# if "parillinen" in rivi:

#huomaamme, että rivi on parillinen
# tämän jälkeen voi taulukossa muuttaa numerot numeroiksi int(luku) komennolla
    
    
    