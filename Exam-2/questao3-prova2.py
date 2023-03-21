def x():
    x1 = int(input("Informe a cordenada de X1: "))
    x2 = int(input("Informe a cordenada de X2: "))
    sub = x2-x1
    quad = sub**2
    return quad
def y():
    y1 = int(input("Informe a cordenada de Y1: "))
    y2 = int(input("Informe a cordenada de Y2: "))
    sub = y2-y1
    quad = sub**2
    return quad
def principal():
    soma = x()+y()
    raiz = soma**0.5
    print("O valor da distância entre os dois pontos é aproximadamente de", raiz)
principal()