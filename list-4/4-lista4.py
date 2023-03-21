n = 1
totalD = 0
totalF = 0
while ( n != 0):
    n = int(input("Insira um número: "))
    if n == 0:
        break
    if n >= 50 and n <= 200:
        totalD = totalD + 1
    else:
        totalF = totalF + 1
print("Dentro do intervalo de 50 a 200 estão", totalD,"números, e fora do interválo estão", totalF,"números!")