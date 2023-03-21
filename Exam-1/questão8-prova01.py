soma = 0
totalM = 0
totalF = 0
while True:
    idade = int(input("Digite a idade:  "))
    if (idade == -1 and idade == 0):
        break
    sexo = int(input("Digite o sexo [0] Masculino [1] Feminino:  "))
    if sexo == 0 and idade >= 14 and idade <= 30:
        totalM = totalM + 1
    if sexo == 1 and idade >= 30 and idade <= 45:
        totalF = totalF + 1
        soma += idade
        media = soma/totalF + 1
    print("O número total de pessoas do sexo masculino com idade entre 14-30 anos é de", totalM)
    print("A média da idade de mulheres que tem entre 30-45 anos é de:", media)