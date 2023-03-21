km = float(input("Quantos quilômetros deseja percorrer com o carro? \n "))
if km <= 50:
    print("Valor total do aluguel para quilômetros rodados %.2f reais" % (km*2.50))
elif km > 50 and km <= 100:
    print("Valor total do aluguel para quilômetros rodados é de %.2f reais" % (km*2.25+125))
elif km >= 150:
    print("Valor total do aluguel para quilômetros rodados %.2f reais" % (km*1.85+350))