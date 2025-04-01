#Tiedostotehtävä 1)

# Tee funktio, joka: Tulosta tiedostoon kymmenentuhatta kappaletta satunnaislukuja väliltä 1 - 1000.
# Jokaisella rivillä tulee olla tasan kymmene lukua pilkuilla erotettuna (eli csv-tiedostona (comma separated values).
# Tallenna tämä tiedosto nimellä luvut.csv (ja sulje tiedosto)
# 
# Tee toinen funktio, joka avaa luvut.csv tiedoston, lataa arvot taulukkoon ja laskee niiden keskiarvon.

def satunnaisNum():
    import random
    kahva = open("luvut.csv", "w")
    for i in range(1,10001):
        kahva.write(f"{random.randint(1,1001)},")
        if i % 10 == 0:
            kahva.write("\n")
    kahva.close()
    
    kahva = open("luvut.csv", "r")
#     print(kahva.read())
    kahva.close()  

x = satunnaisNum()

numerot = []

def keskiarvo():
    tulos = 0
    kahva = open("luvut.csv", "r")
    numerot = kahva.readlines()
    kahva.close()
    maara = 0
    
    for i in range(len(numerot)):
        jono = numerot[i].split(",")
        for j in range(len(jono) - 1):
            tulos += int(jono[j])

    tulos /= 10000
    return tulos

y = keskiarvo()
print(y)









