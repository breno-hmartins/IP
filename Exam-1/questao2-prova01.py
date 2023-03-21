a = int(input("Insira um número qualquer: "))
b = int(input("Insira um número qualquer: "))
c = int(input("Insira um número qualquer: "))
d = int(input("Insira um número qualquer: "))
e = int(input("Insira um número qualquer: "))
menor = a
if b < a and c and d and e:
    menor = b
if c < a and b and d and e:
    menor = c
if d < a and b and c and e:
    menor = d
if e < a and b and c and d:
    menor = e
maior = a
if b > a and c and d and e:
    maior = b
if c > a and b and d and e:
    maior = c
if d > a and b and c and e:
    maior = d
if e > a and b and c and d:
    maior = e
print("O maior valor inserido é {}".format(maior))
print("O menor valor inserido é {}".format(menor))