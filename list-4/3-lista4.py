soma = 0
n = 0
totalP = 0
while (n % 2 == 0):
    n = int(input("Insira um número par: "))
    if n % 2 == 0:
        totalP = totalP + 1
        soma += n
        media = soma/totalP
        print("A média dos número inseridos é de", media)
else:
    print("Este número não é par!")