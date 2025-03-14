# 1)    Tulosta kymmenen kertaa sana ”Kissa”
# laskuri = 0
# while laskuri <= 10:
#     print("Kissa")
#     laskuri += 1
    
# 2)    Tulosta annettu sana kymmenen kertaa
# laskuri = 0
# x = input()
# while laskuri <= 10:
#     print(x)
#     laskuri += 1
    
# 3) Tulosta luvut 1,2,3....100    
# laskuri = 1
# while laskuri <= 100:
#     print(laskuri)
#     laskuri += 1
    
# 4) Tulosta  luvut 100....3,2,1 a)käyttäen laskuri+while rakennetta ja b) käyttäen for-range rakennetta 
# a)
# laskuri = 100
# while laskuri >= 1:
#     print(laskuri)
#     laskuri -= 1

# b)
# for x in range(100, 0, -1):
#     print(x)

# 5) Tulosta luvut väliltä x ja y välin ollessa z. Esim. alla x = 3, y= 13 ja z = 3
# >>> 3,6,9,12
# for x in range(3, 13, 3):
#     print(x)
    
# 6) Tulosta luvut väliltä x,y välin ollessa z, mikäli luku on suurempi kuin q, tulosta luku ja sana ”ISO”
# for x in range(2, 20, 4):
#     if x > 10:
#         print(x, "ISO")
#     else:
#         print(x)
        
# 7) Taulukossa on sanat ["Alma","Bill","Crubbe","Dirf","Embu"]. Tulosta taulukon alkiot ja jokaisen eteen järjestysnumero alkaen numerosta 1.    
# taulukko = ["Alma","Bill","Crubbe","Dirf","Embu"]
# laskuri = 0
# järjNum = 1
# while laskuri < len(taulukko):
#     osoitin = taulukko[laskuri]
#     print(str(järjNum) + "." + str(osoitin))
#     järjNum += 1
#     laskuri += 1
    
# 8) Taulukossa on alkiot [1,2,4, "Alma",10, 20, [12,23], "Bill","Crubbe",5,"Dirf","Embu"].
# Tulosta taulukon alkiot, jos se on stringi, eli sana. Jos se on numero, sitä ei tulosteta, vaan tulostetaan "On numero.".
# Käytä funktiota type(x), jossa x on muuttuja, jota tarkastellaan.   
# taulukko = [1,2,4, "Alma",10, 20, [12,23], "Bill","Crubbe",5,"Dirf","Embu"]
# laskuri = 0
# while laskuri < len(taulukko):
#     osoitin = taulukko[laskuri]
#     if type(osoitin) == int:
#         print("On numero")
#     elif type(osoitin) == str:
#         print(osoitin)
#     laskuri += 1    