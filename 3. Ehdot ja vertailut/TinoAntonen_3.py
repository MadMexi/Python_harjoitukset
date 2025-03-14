# 1. Tee ohjelma joka tarkistaa onko luku välillä 1-10 JA parillinen.
# luku = 1
# if luku <= 10 and luku >= 1 and luku % 2 == 0:
#     print ("luku on välillä ja parillinen")
# else:
#     print("luku ei ole välillä tai parillinen")
#     
# 2. Tee ohjelma joka tarkistaa onko luku negatiivinen TAI suurempi kuin 100.
# luku = 50
# if luku < 0:
#     print("luku on negatiivinen")
# if luku > 100:
#     print("luku on suurempi kuin sata")
# else:
#     print("luku ei ole negatiivinen eikä suurempi kuin sata")
        
# 3. Tee ohjelma joka tarkistaa onko luku pienempi kuin 5 TAI parillinen.
# luku = 52
# if luku < 5:
#     print ("luku on pienempi kuin 5")
# else:
#     print("luku on 5 tai suurempi")
# if luku % 2 == 0:
#     print("luku on parillinen")
# if luku % 2 == 1:
#     print("luku on pariton")

# 4. Tee ohjelma joka tarkistaa onko luku jaollinen sekä 3:lla ETTÄ 5:llä.
# luku = 15
# if luku % 3 == 0 and luku % 5 == 0:
#     print ("luku on jaollinen kolmella sekä viidellä")
# else:
#     print("luku ei ole kummallakaan jaollinen tai vain toisella")

# 5. Tee ohjelma joka tarkistaa onko annettu merkki vokaali (a,e,i,o,u,y,ä,ö,å) TAI numero.	EI TOIMI
# syöte = "9"
# vokaali = ["a","e","i","o","u","y","ä","ö","å"]
# laskuri = 0
# while laskuri < len(vokaali):
#     osoitin = vokaali[laskuri]
#     if osoitin == syöte:
#         print("merkki on kirjain ja kirjain on vokaali")
#     else:
#         print("merkki on kirjain mutta ei vokaali")
#     if type(syöte) == int:
#         print("merkki on numero")
#     else:
#         print("merkki ei ole numero")
#     laskuri += 1
    
# 6. Tee ohjelma joka tarkistaa onko luku välillä 10-20 TAI välillä 30-40.
# luku = 23
# if luku <= 20 and luku >= 10 or luku <= 40 and luku >= 30:
#     print("luku on 10-20 välillä tai 30-40 välillä")
# else:
#     print("luku ei ole 10-20 välillä tai 30-40 välillä")

# 7. Tee ohjelma joka tarkistaa onko vuosiluku karkausvuosi (jaollinen 4:llä JA (ei ole jaollinen 100:lla TAI on jaollinen 400:lla)).
# 
# vuosi = 2024
# if vuosi % 4 == 0 and vuosi % 100 != 0 or vuosi % 400 == 0:
#     print("vuosiluku on karkaus vuosi")
# else:
#     print("vuosiluku ei ole karkasvuosi")

# 8. Tee ohjelma joka tarkistaa ovatko KAIKKI kolme annettua lukua positiivisia.
# luku1 = 5
# luku2 = 10
# luku3 = 100
# 
# if luku1 >= 0 and luku2 >= 0 and luku3 >= 0:
#     print("kaikki luvut ovat positiivisia")
# else :
#     print("yksi tai useampi luku on negatiivinen")

# 9. Tee ohjelma joka tarkistaa onko jokin annetuista kolmesta luvusta negatiivinen.
# luku1 = -1
# luku2 = -6
# luku3 = -100
# 
# if luku1 >= 0 and luku2 >= 0 and luku3 >= 0:
#     print("kaikki luvut ovat positiivisia")
# if luku1 < 0:
#     print("ensimmäinen luku on negatiivinen")
# if luku2 < 0:
#     print("toinen luku on negatiivinen")
# if luku3 < 0:
#     print("kolmas luku on negatiivinen")
    
#  10. Tee ohjelma joka tarkistaa onko merkkijono tyhjä TAI sisältää vain välilyöntejä.
# a = ""
# if len(a) == 0 or a.isspace():
#     print("merkkijono sisältää pelkkiä välilyöntejä tai on kokonaan tyhjä")
# else:
#     print("merkkijono ei ole tyhjä")
    
# # 12. Tee ohjelma joka tarkistaa onko annettu merkki kirjain (a-z tai A-Z).
# a = "d"
# if a.islower():
#     print("merkki on pienikirjain")
# if a.isupper():
#     print("merkki on isokirjain")

# # 13. Tee ohjelma joka tarkistaa onko annettu käyttäjätunnus 3-10 merkkiä pitkä JA alkaa kirjaimella. ei toimi
# KT = "9orgos123"
# if len(KT) >= 3 and len(KT) <= 10 and not(KT[0] in "0123456789"):
#     print("käyttäjätunnus on 3-10 merkkiä pitkä ja alkaa kirjaimella")
# else:
#     print("jompikumpi tai kumpikaan ehto ei täyty")

# # 14. Tee ohjelma joka tarkistaa onko luku välillä -10 ja 10 (pois lukien rajat) JA onko se pariton.
# luku = 10
# if luku < 10 and luku > -10 and luku % 2 == 1:
#     print("luku on 10 ja -10 välillä ja on pariton")
# else:
#     print("luku ei ole 10 ja -10 välillä tai ole pariton")

# 15. Tee ohjelma joka tarkistaa löytyykö annetusta merkkijonosta kirjain 'a' TAI 'A' JA numero.

# x = "sko7i"
# if ("a" in x or "A" in x) and any(char.isdigit() for char in x):
#     print("merkkijonossa on a tai A ja numero")
# else:
#     print("merkkijonossa ei ole a:ta tai A:ta ja numeroa")

# Aarnin antama tehtävä variantti
# def onkoNumero(sana):
#     laskuri = 0
#     while laskuri < len(sana):
#         if sana[laskuri].isdigit(): 
#             return True
#         laskuri += 1
#     return False
# 
# x = "erryu5i"
# print(onkoNumero(x))

# Aarnin antama tehtävä variantti 
# def onkoNumero(sana):
#     for i in range(len(sana)):
#         if sana[i].isdigit():
#             return True
#     return False 
# 
# print(onkoNumero("ersdfgh6j"))

# 16. Tee ohjelma joka tarkistaa onko henkilö täysi-ikäinen (18 tai yli) JA onko hän opiskelija TAI eläkeläinen.
# ika = 17
# if ika >= 18:
#     print("Olet täysi-ikäinen")
#     if ika >= 63:
#         print("Olet eläkeläinen")
# elif ika < 18:
#     print("Olet opiskelija")

# 17. Tee ohjelma joka tarkistaa onko lämpötila pakkasen puolella (alle nollan) JA onko tuulen nopeus yli 5 m/s.
# lampotila = -1
# tuulenNopeus = 6
# if lampotila < 0 and tuulenNopeus > 5:
#     print("Lämpötila on pakkasen puolella ja tuule nopeus on yli 5 m/s")
# else:
#     print("Joko länpötila ei ole alle nollan tai tuulen nopeus yli 5 m/s")

# 18. Tee ohjelma joka tarkistaa onko kokonaisluku sellainen,
# että se on jaollinen 4:llä TAI (jaollinen 2:lla JA suurempi kuin 10).
# KL = 42
# if KL % 4 == 0 or KL % 2 == 0 and KL > 10:
#     print("Kokonaisluku on jaollinen neljällä tai jaollinen kahdella ja isompi kuin kymmenen")
# else:
#     print("Kokonaisluku ei ole jaollinen neljällä tai ei ole jaollinen kahdella ja isompi kuin kymmenen")

# BONUSTEHTÄVÄT
# 19. Tee ohjelma joka tarkistaa onko merkkijono vähintään 8 merkkiä pitkä JA sisältää sekä isoja ETTÄ pieniä kirjaimia.
# x = "asdHsdfghjkl"
# pieniLippu = 0
# isoLippu = 0
# def onkoPieni(sana):
#     global pieniLippu
#     for i in range(0,len(sana)):
#         if sana[i].isupper():
#             pieniLippu = 1
# def onkoIso(sana):
#     global isoLippu
#     for i in range(0,len(sana)):
#         if sana[i].islower():
#             isoLippu = 1
# if (len(x) >= 8):

#jos ei kayteta funktioita, niin voikoodin kirjoittaa nainkin
#     pieniLippu = 0
#     for i in range(0,len(sana)):
#         if sana[i].isupper():
#             pieniLippu = 1
            
#     onkoPieni(x)
#     onkoIso(x)
#     if isoLippu == 1 and pieniLippu == 1:
#         print("Merkkijonossa on vähintään 8 kirjainta ja sisältää isoja ja pieniä kirjaimia")
#     else:
#         print("Merkkijonossa ei ole vähintään kahdeksaa kirjainta tai sisällä isoja ja pieniä kirjaimia")
# else:
#     print("Merkkijonossa on vähemmän kuin kahdeksan merkkiä")



# 20. Tee ohjelma joka tarkistaa täyttääkö tuote ostoskoriin lisäämisen ehdot:
# (hinta alle 100€ TAI alennuksessa) JA (varastossa TAI ennakkotilattavissa).
# Ei kiitos

# 21. Tee ohjelma joka laskee positiivisten lukujen summan kunnes käyttäjä syöttää nollan.
# summa = None
# num1 = 1
# num2 = 1
# while num1 != 0 and num2 != 0:
#     num1 = int(input("Anna luku:"))
#     num2 = int(input("Anna luku:"))
#     summa = num1 + num2
#     print(summa)

# 22. Tee ohjelma joka tarkistaa onko luku parillinen.
# luku = 671
# if luku % 2 == 0:
#     print("luku on parillinen")
# else:
#     print("luku on pariton")





