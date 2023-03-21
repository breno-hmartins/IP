pares = 0
for x in range (20):
    n = int(input("Digite um número: "))
    if (n%2) == 0:
        pares = pares + 1
print(pares, "números pares")
print((20 - pares), "números ímpares")