# lista = ["Miisu","Pauli","Aarni","Pasi","Kari"]
#
# x = open("luvut.luv", "w")
# for i in range(len(lista)):
#     x.write(str(i) + ". " + str(lista[i] + "\n"))
# x.close()
# 
# x = open("luvut.luv", "r")
# print(x.read())

# Tehtävät
# OSA A)
# Kirjoita tiedostoon "luvut.luv" tietoa seuraavassa muodossa:
#  järjestysnumero, satunnaisluku väliltä 100 - 200 , sana "parillinen" tai "pariton" riippuen satunnaisluvun parillisuudesta ja rivinvaihto
# esim:
# """
# 1   34  parillinen
# 2   57  pariton
# 3   11  pariton
# """
# import random
# 
# lista = []
# 
# for i in range(100):
#     lista.append(random.randint(100,201))
# # print(lista)
# 
# x = open("luvut.luv", "w")
# for k in range(len(lista)):
#     if lista[k] % 2 == 0:
#         x.write(str(f"{k + 1} {lista[k]} parillinen\n"))
#     else:
#         x.write(str(f"{k + 1} {lista[k]} pariton\n"))
# x.close()
# 
# x = open("luvut.luv", "r")
# print(x.read())
# x.close()

#OSA B)
#Lataa tiedosto luvut.luv
#pura tiedot siten, että
# jos rivillä on sana "parillinen" rivin järjestysnumero ja satunnaisluku menevät parillinen taulukkoon
# jos rivillä on sana "pariton" rivin järjestysnumero ja satunnaisluku menevät pariton taulukkoon
#ylläolevan esimerkin mukaisesti parillinen-taulukko sisältää alkiot [1,34] ja pariton-taulukko sisältää alkiot [2,57,3,11]
#tulosta taulukot kahteen eri tekstitiedostoon parillinen.luv ja pariton.luv 

# parillinen = []
# pariton = []
# 
# x = open("luvut.luv", "r")
# for i in x:
#     s = i.split(" ")
#     if "parillinen" in i:
#         parillinen.append(s[0])
#         parillinen.append(s[1])
#     if "pariton" in i:
#         pariton.append(s[0])
#         pariton.append(s[1])
# x.close()
# 
# z = open("parillinen.luv", "w")
# for j in parillinen:
#     z.write(f"{j},")
# z.close()
# 
# c = open("pariton.luv", "w")
# for k in pariton:
#     c.write(f"{k},")
# c.close()
# 
# z = open("parillinen.luv", "r")
# print(z.read())
# z.close()
# 
# c = open("pariton.luv", "r")
# print(c.read())
# c.close()










