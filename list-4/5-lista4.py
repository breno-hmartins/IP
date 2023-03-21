n = 1
totalM = 0
totalF = 0
while ( n == 0 or n == 1):
    n = int(input("Informe (0 - Masculino e 1 - Feminino): "))
    if n == 0:
        totalM = totalM + 1
    elif n == 1:
        totalF = totalF + 1
    else:
        break
    print(totalM,"são do sexo masculino, e", totalF,"são do sexo feminino.")