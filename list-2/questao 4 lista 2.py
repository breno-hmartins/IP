x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
if (x != 0 and y != 0):
    if x > 0 and y > 0:
        print("A coordenada faz parte do primeiro quadrante!")
    elif x < 0 and y > 0:
        print("A coordenada faz parte do segundo quadrante!")
    elif x and y < 0:
        print("A coordenada faz parte do terceiro quadrante!")
    else:
        print("A coordenada faz parte do quarto quadrante")
else:
    print("erro, X e/ou Y não pode ser zero")