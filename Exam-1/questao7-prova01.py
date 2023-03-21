while True:
    numero=int(input("fatorial de: "))
    resultado= 1
    for i in range(1,numero+1):
        resultado*= i
    print ("O fatorial é:", resultado)
    if numero < 1:
        print("O programa não aceita número menores que 1")
        break