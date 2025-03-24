# 1) Tee funktio, joka tulostaa kymmenen kertaa sanan "Kissa"

# def kissa(kertaa):
#     laskuri = 0
#     while laskuri < kertaa:
#         print("Kissa")
#         laskuri += 1
# x = kissa(10)

# 2) Tee funktio, joka tulostaa argumenttina annetun sanan kymmenen kertaa

# def tulosta(sana):
#     for x in range(10):
#         print(sana)
# x = tulosta("korppi")

# 3) Tee funktio, joka tulostaa luvut 1,2,3....100

# def luvut1():
#     for i in range(1,101):
#         print(i)
# x = luvut1()

# 4) Tee funktio, joka tulostaa luvut 100....3,2,1

# def luvut2():
#     laskuri = 100
#     while laskuri > 0:
#         print(laskuri)
#         laskuri -= 1
# x = luvut2()

# 5) Tee funktio, joka tulostaa luvut väliltä x,y välin ollessa z. Funktion kutsu esim. valiLuvut(3,13,3)

# def valiLuvut1 (alku,loppu,hyppy):
#     for i in range(alku,loppu,hyppy):
#         print(i)
# x = valiLuvut1(1,100,4)

# 6) Tee funktio, joka tulostaa luvut väliltä x,y välin ollessa z, mikäli luku on suurempi kuin q, tulosta sana ”ISO”

# def valiLuvut2 (alku,loppu,hyppy,iso):
#     for i in range(alku,loppu,hyppy):
#         if i >= iso:
#             print("ISO")
#         else:
#             print(i)
# x = valiLuvut2(1,100,4,60)


# 7) Taulukossa on sanat ["Alma","Bill","Crubbe","Dirf","Embu"]. Tee funktio, joka tulostaa taulukon alkiot ja jokaisen eteen järjestysnumero alkaen numerosta 1.

# def jarjNum(lista):
#     for i in range(len(lista)):
#         print(f"{i + 1} {lista[i]}")
# x = jarjNum(["Alma","Bill","Crubbe","Dirf","Embu"])

# 8) Taulukossa on alkiot [1,2,4, "Alma",10, 20, [12,23], "Bill","Crubbe",5,"Dirf","Embu"].
# Tee funktio, joka tulostaa taulukon alkiot, jos se on stringi, eli sana. Jos se on numero, sitä ei tulosteta, vaan tulostetaan "On numero.".
# Käytä funktiota typeof(x), jossa x on muuttuja, jota tarkastellaan.

def tulostus(lista)
