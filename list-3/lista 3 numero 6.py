for i in range (0,1) :
    n1 = int(input("Informe o valor do expoente desejado: "))
    if n1 <= 1:
        print("Por favor informe um número que seja maior que 1 e que seja inteiro!")
    else:
        n2 = int(input("Informe o valor do número a ser elevado ao expoente escolhido: "))
        if n2 < 2:
            print("Por favor informe um número que seja maior que 2 e que seja inteiro!")
        else:
            potencia = n1**n2
            print("O resultado é", potencia)