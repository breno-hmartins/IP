for i in range(0,5):
    nome = input("Informe o nome: ")
    salario = float(input("Informe o salário: "))
    if salario <= 600:
        print(nome, "esta isento de pagar a taxa")
    elif salario > 600 and salario <= 1500:
        imp = salario*0.1
        print("O valor da aliquota é de ",imp)
    elif salario > 1500:
        imp2 = salario*0.15
        print("O valor da aliquota é de ",imp2)