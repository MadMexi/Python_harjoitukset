def kertotaulu(x,y):
    for k in range(1, y + 1):
        rivi = ""
        for i in range(1,x + 1):
            rivi += str(i * k) + " "
        print(rivi)
kertotaulu(10,10)










