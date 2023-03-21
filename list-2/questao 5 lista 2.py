sexo = int(input("Informe o sexo do doador (0=M e 1=F): "))
if sexo != 1 and sexo != 0:
    print("Por favor, selecione um número que seja 0, caso você se identifique como mulher ou 1, caso se identifique como homem!")
idade = int(input("Informe a idade: "))
if idade < 16:
    print("Pessoas menores de 16 anos, não são permitidas fazer a doação de sangue!")
elif (idade >= 60) :
    resp1 = int(input("Já fez doação de sangue antes de completar 60 anos? (0=Sim e 1=Não): "))
    if resp1 == 1:
        print("Não é possível doar. \nPois nunca havia feito uma doação antes dos 60 anos inclompletos!")
peso = int(input("Informe o seu peso: "))
if sexo == 0 and peso < 60:
    print("Não é possível doar. \nO Senhor possui um peso abaixo da média requerida para realizar a doação!")
elif sexo == 1 and peso < 50:
    print("Não é possível doar. \nA Senhora possui um peso abaixo da média requerida para realizar a doação!")
elif sexo == 1 and peso > 50:
    doente = int(input("A doadora está com febre? (0=Sim e 1=Não): "))
    if doente == 0:
        print("Não é possível doar. \nA doadora está doente!")
    else:
        gravida = int(input("A doadora está gravida? (0=Sim e 1=Não): "))
        if gravida == 0:
            print("Não é possível doar. \nA doadora está grávida!")
        elif gravida == 1:
            meses = int(input("Fez algum parto nos útimos 12 meses? (0=Sim e 1=Não): "))
            if meses == 0:
                print("Não é possível doar. \nPois ocorreu um parto a menos de 12 meses e ainda está amamentando a crinaça!")
            elif meses == 1:
                print("A senhora pode fazer a doação de sangue!")
elif sexo == 0 and peso > 60:
    doente = int(input("O doador está com febre? (0=Sim e 1=Não): "))
    if doente == 0:
        print("Não é possível doar. \nO doador está doente!")
    else:
        print("O Senhor pode fazer a doação de sangue!")