tiedosto_kahva = open("teksti.tek","w")
#huomaa, että tiedostonimen jatke on vapaavalintainen
for n in range(5):
    tiedosto_kahva.write("Koira\n")
    tiedosto_kahva.write(str(n) + "\n") #tulostetaan myos numero
 
#kirjoitetaan Kissa omalle rivilleen
#samalla tavalla kirjoitetaan muut rivit
tiedosto_kahva.close()
 
#LUKEMINEN JA KÄSITTELY!
tiedosto_kahva = open("teksti.tek","r")
#rivit = tiedosto_kahva.readlines() #kukin rivi on oma taulukon alkio
#rivit = tiedosto_kahva.read() #kaikki rivit yhteen stringgiin
#toistorakenteella, kunnes loppuu
#tama on ehka selkein
 
tulosrivit = [] 
for rivi in tiedosto_kahva: #LUKEE RIVIT YKSIKERRALLAAN TIEDOSTOSTA
    siistirivi = rivi.rstrip()
    tulosrivit.append(siistirivi)
    #print(siistirivi)
    
print(tulosrivit)