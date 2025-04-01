# def numSum(luvut):
#     summa = 0
#     luvut = str(luvut)
#     for i in range(len(luvut)):
#         summa += int(luvut[i])
#     return summa
# print(numSum(12345678965466578909807654329))


#Palauta totuus arvo perustuen siihen, että onko luku jaollinen yhdeksällä.
#Laske luvun numeroiden summaa, kunnes luku on 9 tai alle.
#Jos luku on 9, niin se on jaollinen yhdeksällä.
def jaol9(luvut):
    summa = 0
    luvut = str(luvut)
    for i in range(len(luvut)):
        summa += int(luvut[i])
    if summa % 9 == 0:
        return True
    else:
        return False
print(jaol9(874561464165789098076543254213112))














