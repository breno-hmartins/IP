def horas():
    h = int(input("Infome as horas: "))
    conv1 = h*3600
    return conv1
def minutos():
    m = int(input("Infome os minutos: "))
    conv2 = m*60
    return conv2
def segundos():
    s = int(input("Infome os segundos: "))
    return s
def principal():
    resultado = horas()+minutos()+segundos()
    print("A soma de todos os valores convertidos em segundos é de: ",resultado)
principal()
