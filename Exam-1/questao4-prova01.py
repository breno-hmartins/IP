dia = int(input('Insira um dia: '))
mes = int(input('Insira um mês: '))
ano = int(input('Insira um ano: '))
valida = False
if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
    if(dia<=31):
        valida = True
elif(mes==4 or mes==6 or mes==9 or mes==11):
        if(dia<=30):
            valida = True
if(valida):
    print('Data está válida')
else:
    print('Data está inválida')