def anos():
    a = int(input("Quantos anos você tem? \n"))
    ano = a*365
    return ano
def meses():
    m = int(input("E quantos meses de um ano incompleto? \n"))
    mes = m*30
    return mes
def dias():
    d = int(input("E quantos dias de um mês incompleto? \n"))
    return d
def principal():
    resultado = anos()+meses()+dias()
    print("Você possui totais", resultado,"dias vividos!")
principal()