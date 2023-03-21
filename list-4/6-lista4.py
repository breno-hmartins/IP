chico = 1.50
juca = 1.10
ano = 0
while ( chico >= juca):
    chico += 0.02
    juca += 0.03
    ano += 1
print("Ao decorrer dos anos Chico possuirá %.2f metros, enquanto Juca terá %.2f metros." % (chico, juca))
print("Serão necessários", ano,"anos para que Juca se torne maior que Chico!")