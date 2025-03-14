# 1.Tee funktio "summa" joka tulostaa kahden luvun summan.

# def summa(num1,num2):
#     tulo = int(num1) + int(num2)
#     return tulo
# 
# x = summa(input(),input())
# print(x)

# 2.Tee funktio "alkiot", jolle annetaan luvut a ja b. se palauttaa listana numerot a:sta b:hen. EI TOIMI
# x = int(input("anna luku1:"))
# y = int(input("anna luku2:"))
# def alkiot(luku1,luku2):
#     laskuri = luku1
#     while laskuri <= luku2:
#         print(laskuri)
#         laskuri += 1
#     return laskuri
# alkiot(x,y)

# 3.Tee funktio "etsi"
# parametreina etsittava luku ja lista joka palauttaa etsittavan luvun indeksin, jos luku on listassa.

# def etsi(luku,lista):
#     laskuri = 0
#     while laskuri < len(lista):
#         if luku not in lista:
#             print("luku ei ole listassa")
#             break
#         if luku in lista:
#             if luku != lista[laskuri]:
#                 laskuri += 1
#             if luku == lista[laskuri]:
#                 print("löytyi!")
#                 break 
#     return laskuri
# 
# def etsix(luku,lista):
#     laskuri = 0
#     tulos = 99999
#     while laskuri < len(lista):
#         testattava = lista[laskuri]
#         if luku == testattava:
#             tulos = laskuri
#         laskuri += 1
#     return tulos
# x = etsix(200, [8, 4, 6, 5, 89, 2, 36, 3, 64, 7, 4])
# print(f"luvun indexi on: ",x)

# 4) Tee funktio, joka PALAUTTAA kaksi lukua yhteenlaskettuna

# def summa(luku1,luku2):
#     return (luku1 + luku2)
# x = summa(5,15)
# print(x)

# 5) Tee funktio, joka laskee annetut luvut yhteen (vaikka kuinka monta, &nbsp; pilkuilla erotettuna)
# Käytä args* -rakennetta

# def arg_summa(*luvut):
#     tulos = 0
#     for x in luvut:
#         tulos += x
#     return tulos
# 
# print(arg_summa(1, 2, 3, 10, 55, 22))

# 6) Tee nelilaskin, jolle annetaan luvut ja niihin kohdistuva operaatio(summa, erotus,tulo,jako)
# Anna operaatio stringinä "+", "-" tai "summa", "erotus"
# Jokaista operaatiota varten tee funktio, jota kutsutaan (vrt. tehtävä 1)
# Edellisen laskun arvo jää muistiin
# def summa(luku1,luku2):
#     return(luku1 + luku2)
# def erotus(luku1,luku2):
#     return(luku1 - luku2)
# def tulo(luku1,luku2):
#     return(luku1 * luku2)
# def jako(luku1,luku2):
#     return(luku1 / luku2)
#     
# def nelilaskin(luku1,luku2,operaatio):
#     tulos = 999
#     if operaatio == summa:
#         tulos = summa(luku1,luku2)
#     if operaatio == erotus:
#         tulos = erotus(luku1,luku2)
#     if operaatio == tulo:
#         tulos = tulo(luku1,luku2)
#     if operaatio == jako:
#         tulos = jako(luku1,luku2)
#     return tulos
# 
# def nelilaskinx(luku1,luku2,operaatio):
#     tulos = 999
#     tulos = operaatio(luku1,luku2)
#     return tulos
# 
# x = nelilaskinx(10,2,tulo)
# print(x)

# 7). Tee funktio, joka palauttaa annetun listan lopusta alkuun.
# Et voi käyttää Pythonin sisäänrakennettua Reverse-funktiota
# def kaanto(lista):
#     kaanto_lista = []
#     laskuri = len(lista) - 1
#     while laskuri >= 0:
#         kaanto_lista.append(lista[laskuri])
#         laskuri -= 1
#     return kaanto_lista
#     
# x = kaanto([55, 20, 25, 233, 3, 34, 73, 85, 5, 7, 5, 4, 5, 258])
# print(x)

# 8) Tee funktio, joka palauttaa listana sille annetusta listasta valitun palan
# eli kohdasta "alku" alkaen "monta" palaa. Jos lista loppuu ennenkuin "monta" tulee tayteen
# palautetaan se, mikä pystytään.




uusipala = pala([2,4,56,78,9,6,4,3,6,8,9,], 3,4) # [78,9,6,4]
print(uusipala)











