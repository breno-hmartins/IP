a1 = int(input("Qual o valor do primeiro ângulo interno? \n"))
a2 = int(input("Qual o valor do segundo ângulo interno? \n"))
a3 = int(input("Qual o valor do terceiro ângulo interno? \n"))
if a1 + a2 + a3 > 180:
    print("Ângulo invalido, pois a soma de todos os ângulos internos de um triângulo é de 180°")
elif a1 and a2 == a3:
    print("É um triângulo equilátero!")
elif a1 == a2 != a3 or a3 == a2 != a1 or a1 == a3 != a2:
    print("É um triângulo isóceles!")
elif a1 == 90 or a2 == 90 or a3 == 90:
    print("É um triângulo retângulo!")
else:
    print("É um triângulo escaleno!")