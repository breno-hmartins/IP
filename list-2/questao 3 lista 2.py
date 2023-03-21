n1 = float(input("Informe o valor de n1: "))
n2 = float(input("Informe o valor de n2: "))
if n1 > n2:
    print("O quadrado do menor numero eh: %.1d" % (n2**2))
    print("A raiz quadrada do maior numero eh: %.2f" % pow(n1, 1/2))
elif n2 > n1:
    print("O quadrado do menor numero eh: %.1d" % (n1**2))
    print("A raiz quadrada do maior numero eh: %.2f" % pow(n2, 1/2))
else:
    print("Dois numeros iguais")