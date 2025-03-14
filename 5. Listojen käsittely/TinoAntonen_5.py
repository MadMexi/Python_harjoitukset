# 1. Yhdistä kaksi listaa
# Tehtävä: Kirjoita funktio, joka yhdistää kaksi listaa (alkiot peräkkäin) ja palauttaa uuden listan.
# def yhdista(lista1, lista2):
#     lista3 = []
#     
#     
#     osoitin1 = 0 #osoitin alustetaan nollaksi
#     while osoitin1 < len(lista1): #niin kauan kuin osoitin1 on pienempi kuin lista1
#         lista3.append(lista1[osoitin1]) #lisää lista kolmoseen lista ykkösestä kohta osoitin1
#         osoitin1 += 1 #kasvata osoitinta
#         
#     osoitin1 = 0 #osoitin alustetaan taas nollaksi
#     while osoitin1 < len(lista2): #niin kauan kuin osoitin1 on pienempi kuin lista2
#         lista3.append(lista2[osoitin1]) #lisää lisa kolmoseen lista kakkosesta kohta osoitin1
#         osoitin1 += 1 #kasvata osoitinta
#         
#     return lista3 #palauttaa lista kolmosen
#     
# lista1 = [1, 2, 3, 4, 5]
# lista2 = [10, 20, 30, 40, 50]
# tulos = yhdista(lista1, lista2)
# print(tulos)

# 2.Lomita listat
# Tehtävä: Lomita kaksi listaa vuorotellen.
# lista1 = [1, 2, 3, 4, 5]
# lista2 = [10, 20, 30, 40, 50,60,70]
# lista3 = []
# osoitin1 = 0
# 
# while osoitin1 < len(lista1):
#     lista3.append(lista1[osoitin1])
#     lista3.append(lista2[osoitin1])
#     osoitin1 += 1
#     
# print(lista3) #tulostetaan lista3
# lista3.append(lista2[osoitin1]) #lisätään lista kolmoseen lista kakkosesta osoitin1
# print(lista3) # tulostetaan lista3
# osoitin1 += 1 # kasvatetaan osoitinta että se liikkuu seuraavaan alkioon
# lista3.append(lista2[osoitin1]) #lisätään lista kolmoseen lista kakkosesta osoitin1
# print(lista3) # tulostetaan lista3

# 3.Laske keskiarvo
# Tehtävä: Laske listan lukujen keskiarvo.
# lista = [3, 5, 9, 13, 11, 25, 77]
# laskuri = 0
# summa = 0
# 
# while laskuri < len(lista):
#     osoitin = lista[laskuri]
#     summa += osoitin
#     laskuri += 1
#     
# keskiArvo = (summa / len(lista))
# print(f"{keskiArvo:.2f}")

# 4.Poista duplikaatit
# Tehtävä: Poista listasta kaikki toistuvat alkiot säilyttäen alkuperäisen järjestyksen.

# a) näin ei tehdä
# tarkistaja = 0
# lista = [1, 1, 2, 3, 3 ,3 , 4, 5, 5, 5, 5, 6, 6, 7, 7, 7]
# laskuri = 0
# 
# while tarkistaja < len(lista):
#     tarkistaja = lista[laskuri]
#     if tarkistaja == lista[laskuri - 1]:
#         lista.pop(tarkistaja)
#     elif tarkistaja != lista[laskuri - 1]:
#         tarkistaja += 1
#         laskuri += 1
# 
# print(lista)

# b)
# lista = [1, 1, 2, 3, 3 ,3, 4, 5, 5, 5, 5, 6, 6, 7, 7, 7]
# uniikit = []
# osoitin = 0
# while osoitin < len(lista):
#     alkio = lista[osoitin]
#     if alkio not in uniikit: #alkio ei ole uniikit listassa, niin se laitetaan uniikit listaan
#         uniikit.append(alkio)
#     osoitin += 1
# print(uniikit)    

# 5.Käännä lista
# Tehtävä: Käännä listan järjestys päinvastaiseksi. (tee oma funktio, EI pythonin reverse.)
# lista = [1, 2, 3, 4, 10, 6, 7]
# kaannetty = []
# laskuri = len(lista) - 1
# while laskuri >= 0:
#     kaannetty.append(lista[laskuri])  
#     laskuri -= 1
# print(kaannetty)

# 6.Suodata parilliset luvut
# Tehtävä: Palauta uusi lista, joka sisältää vain alkuperäisen listan parilliset luvut.
# lista = [1, 2, 90, 4, 5, 6, 78, 8, 69, 10, 11, 12, 13, 14]
# parilliset = []
# laskuri = 0
# while laskuri < len(lista):
#     if lista[laskuri] % 2 == 0:
#         parilliset.append(lista[laskuri])
#     laskuri += 1
# print(parilliset)

# 7.Etsi suurin ja pienin
# Tehtävä: Palauta listan suurin ja pienin arvo.
# Tee se ilman Pythonin max ja min funktiota.
# lista = [8, 11, 90, -54, 5, 6, 78, 105, 69, 10, 1599, 12, 13, 14]
# suurin = lista[0]
# pienin = lista[0]
# laskuri = 0
# 
# while laskuri < len(lista):
#     if suurin < lista[laskuri]:
#         suurin = lista[laskuri]
#     if pienin > lista[laskuri]:
#         pienin = lista[laskuri]
#     laskuri += 1
#     
# print(f"pienin arvo on: {pienin} ja suurin arvo on: {suurin}")

# 8.Jaa lista osiin
# Tehtävä: Jaa lista n kokoisiin osiin eli pienempiin listoihin.
# 
# def jakaja(munlista, jako):
#     tulosAlku = []
#     tulosLoppu = []
#     laskuri = 0
#     while laskuri < jako:
#         tulosAlku.append(munlista[laskuri])
#         laskuri += 1
#     while laskuri < len(munlista):
#         tulosLoppu.append(munlista[laskuri])
#         laskuri += 1
#     return (tulosAlku, tulosLoppu)
# 
# tulos = jakaja([8, 11, 90,54, 5, 6],3)
# print(tulos)

# 9.Poista alkiot ehdon mukaan
# Tehtävä: Poista listasta kaikki negatiiviset luvut.
# lista = [8, -11, 90, -54, 5, 6, 78, -105, -69, 10, 1599, 12, -13, -14]
# posLuvut = []
# laskuri = 0
# while laskuri < len(lista):
#     if lista[laskuri] > 0:
#         posLuvut.append(lista[laskuri])
#     laskuri += 1
#   
# print(posLuvut)

# 10.Laske esiintymät
# Tehtävä: Laske kunkin alkion esiintymiskerrat listassa.
# lista = ['a','a','a','b','b','b','c','c','a','d','d','b','c']
# tulos_lista = []
# 
# for i in range(len(lista)): # käy listan läpi alkioittain
#     for j in range(len(tulos_lista)): # käy tulos_listan läpi alkioittain
#         if tulos_lista[j][0] == lista[i]: # jos tulos_listan j indexin alkion 0 indexin arvo on sama kuin listan i indexin arvo
#             tulos_lista[j][1] += 1 # lisätään tulos_listan j indexin alkio 0:aan yksi lisää että alkio siirtyy yhden oikealle
#             break # j looppi katkaistaan
#         elif j == len(tulos_lista) - 1: # muuten jos j on yhtäsuuri kuin tulos_listan pituus - 1 eli viimeinen alkio
#             tulos_lista.append([lista[i],1]) # tulos_listaan lisätään listan i indexin arvoon yksi lisää 
#     if len(tulos_lista) == 0: # jos tulos_listan pituus on yhtä kuin 0 alkiota eli jos lista on tyhjä
#         tulos_lista.append([lista[i],1]) # tulos_listaan lisätään listan i indexin arvo
# print(tulos_lista)

# helpompi ymmärtää

# alkiot = ['a','a','a','b','c','c']
#  
#  
# tulos = []
# for alkio in alkiot:
#     if alkio not in tulos:
#         tulos.append(alkio)
#  
# print(tulos) #a,b,c
#  
# #toinen rundi
# maarat = []
# laskuri = 0
# for atomi in tulos:
#     laskija = 0
#     for alkio in alkiot:
#         if atomi == alkio:
#             laskija +=1
#     maarat.append(laskija)
# print(maarat)

# 11.Kierrätä lista
# Tehtävä: Siirrä listan alkioita n paikkaa oikealle.
# #lisää uuden alkion listan alkuun ja pudottaa päädystä aina viimeisen alkion
# def ringbuf(lista,uusialkio):
#     tulos = []
#     tulos.append(uusialkio)
#     laskuri = 0
#     while laskuri < len(lista)- 1:
#         tulos.append(lista[laskuri])
#         laskuri += 1
#     return tulos
# 
# # siirtää viimeisen alkion listan ensimmäiseksi alkioksi ja tällä tavalla kierrättää listaa
# def siirtoOik(lista):
#     tulos = []
#     viim_alkio = lista[-1]
#     tulos.append(viim_alkio)
#     laskuri = 0
#     while laskuri < len(lista)- 1:
#         tulos.append(lista[laskuri])
#         laskuri += 1
#     return tulos
#     
# x = siirtoOik([1, 2, 9, 6, 2, 7, 2, 3, 7, 7, 4, 1, 3, 10])
# print(x)
# x = siirtoOik(x)
# print(x)
# x = siirtoOik(x)
# print(x)
# 
# y = ringbuf(x,"kissa")
# print(y)
# y = ringbuf(y,"koira")
# print(y)
# y = ringbuf(y,"marsu")
# print(y)

# 12.Etsi toiseksi suurin
# Tehtävä: Palauta listan toiseksi suurin arvo.
# def tois_suurin(lista):
#     laskuri = 0
#     suuret = [lista[0] ,lista[1]]
#     if suuret[0] < suuret[1]:
#         suuret[0], suuret[1] = suuret[1], suuret[0]
#     for i in range(2,len(lista)):
#         if lista[i] > suuret[0]:
#             suuret[1] = suuret[0] 
#             suuret[0] = lista[i]
#         elif lista[i] > suuret[1]:
#             suuret[1] = lista[i]
#     return suuret[1]
# print(tois_suurin([2,6,8,4,9]))

# 13.Etsi sarjat
# Tehtävä: Etsi listasta peräkkäiset samat alkiot
# (jos samaa alkiota on kolme tai enemman ja tulosta esiintymän alkukohta

# lista = [2,5,9,9,9,4,6,6,3,3,3,3]
# tulos = []
# i = 0
# while i < (len(lista) - 2):
#     laskuri = 1
#     for k in range(i + 1, len(lista)):
#         if lista[i] == lista[k]:
#             laskuri += 1
#         if lista[i] != lista[k] or k == len(lista) - 1:
#             if laskuri >= 3:
#                 tulos.append(i)
#             i += laskuri
#             break
#     i += 1
# print(tulos)

# 14.Alilistoihin jaottelu  
# tee näistä alilistoja seuraavasti:
# [["Mersu",100],["Lada",200]......
# autot = ["Mersu",100,"Lada",200,"Toyota",300,"Jeep",342]
# tulos = []
# for i in range(0 ,len(autot), 2):
#     alilista = []
#     alilista.append(autot[i])
#     alilista.append(autot[i + 1])
#     tulos.append(alilista)
# print(tulos)

# 15.Eräänä päivänä tiedontallentaja oli huolimaton ja laittoi liikaa lukuja  
# Poista ylimääräiset luvut!
# autot = ["Mersu",100,3,4,"Lada",200, 200,"Toyota",300,"Jeep",560,654,342]
# autot = [555,"Mersu",100,3,400,"BMW",400,"Lada",200, 201,"Toyota",300, 826,"Jeep",560,654,342] #oma testi
# tutki mitä tyyppiä elementti on, esim. onko luku kokonaisluku ja putsaa lista sen avulla
# ylimaaraisia lukuja voi olla missä vain!
 
# if type(123) == int:
#     print("luku")
# if type("123") == str:
#     print("text")

# puhd = []
# laskuri = 0
# while laskuri < len(autot):
#     if type(autot[laskuri]) == str:
#         if type(autot[laskuri + 1]) == int:
#             puhd.append(autot[laskuri])
#             laskuri += 1
#     elif type(autot[laskuri]) == int:
#         if type(autot[laskuri - 1]) == str:
#             puhd.append(autot[laskuri])
#         laskuri += 1
#     
# print(puhd)







#Aarnin bonarit

#1.
#Kirjoita ohjelma, joka tulostaa, että onko muuttuja int vai string
# muuttuja1 = 1
# #Tulosta tässä
# if type(muuttuja1) == str:
#     print("muuttuja on string")
# if type(muuttuja1) == int:
#     print("muuttuja on int")
#     
# muuttuja2 = "1"
# #Tulosta tässä
# if type(muuttuja2) == str:
#     print("muuttuja on string")
# if type(muuttuja2) == int:
#     print("muuttuja on int")

#2.
#Tulosta joka ikisen elementin tyyppi listasta luvut. Joko int tai string
# luvut = [12123,6,8,9,5,"23123","Aarni on paras", 444]
# 
# for i in range(len(luvut)):
#     if type(luvut[i]) == int:
#         print("int")
#     if type(luvut[i]) == str:
#         print("string")

#3.
#Lajittele listan elementit listoihin numerot ja tekstit, perustuen niiden datatyyppiin.
# elementit = [12123,6,8,9,5,"23123","Aarni on paras", 444]
# numerot = []
# tekstit = []
# 
# for i in range(len(elementit)):
#     if type(elementit[i]) == int:
#         numerot.append(elementit[i])
#     if type(elementit[i]) == str:
#         tekstit.append(elementit[i])
# print(numerot)
# print(tekstit)











