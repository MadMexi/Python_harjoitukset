# # 1) Tulosta luvut 3,6,9,12,15,18
# print("3,6,9,12,15,18")

# # 2) Tulosta luvut 200,190...0, jokaisen luvun edessa selitys seuraavasti:
# # Luku pienenee, se on nyt: 200
# # Luku pienenee, se on nyt: 190
# laskuri = 200
# while laskuri >= 0:
#     print("Luku pienenee, se on nyt:", laskuri)
#     laskuri -= 10

# #3) Tulosta isot aakkoset (A-Z) käyttäen chr-funktiota. Ei skandinaavisia merkkejä
# laskuri = 65
# while laskuri <= 90:
#     x = chr(laskuri)
#     print (x)
#     laskuri += 1

# #4) Sama, mutta tulosta ne vierekkäin käyttäen "end"-käskyä printissä
# laskuri = 65
# while laskuri <= 90:
#     x = chr(laskuri)
#     print (x,end=" ")
#     laskuri += 1

#5) Tulosta pienet aakkoset (a-z) samoin
# laskuri = 97
# while laskuri <= 122:
#     x = chr(laskuri)
#     print (x)
#     laskuri += 1

#6) Tulosta joka toinen iso aakkonen (A,C,E) erota ne pilkulla.
# laskuri = 65
# while laskuri <= 90:
#     x = chr(laskuri)
#     print (x, end=",")
#     laskuri += 2

#7) Tulosta kertotaulu 1 - 10 käyttäen kahta sisäkkäistä laskuri-while rakennetta.
#Käytä laskuri-muuttujanimen tilalla sanoja "kertoja" ja "kerrottava"
# kertoja = 1
# kerrottava = 1
# while kerrottava <= 10:
#     kertoja = 1 # nollataan kertoja
#     while kertoja <= 10:
#         print(str(kerrottava) + "*" + str(kertoja) + ":" + str(kerrottava * kertoja), end=" ")
#         kertoja += 1
#     kerrottava += 1
#     print("\n")

#8) Tulosta samankaltainen taulukko JAKOLASKUILLA,
#käytä tulostukseen ohjeessa e) esitettyä f-string muotoa!
# jakaja = 1
# jaettava = 1
# while jaettava <= 10:
#     jakaja = 1 # nollataan jakaja
#     while jakaja <= 10:
#         print(f"{jaettava} / {jakaja} : {jaettava / jakaja:.2f}",end=" ")
#         jakaja += 1
#     print("\n")
#     jaettava += 1















