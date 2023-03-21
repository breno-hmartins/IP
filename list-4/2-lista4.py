soma = 0
n = 0
while (n % 2 == 0):
    n = int(input("Insira um número par: "))
    if n % 2 == 0:
        soma += 1
    print("Foram inseridos", soma, "números pares!")
else:
    print("Este número não é par!")