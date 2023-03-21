a = int(input("Insira um número qualquer: "))
b = int(input("Insira um número qualquer: "))
c = int(input("Insira um número qualquer: "))
d = int(input("Insira um número qualquer: "))
e = int(input("Insira um número qualquer: "))
maior2 = a
if b > a and c and d and b < e or b > a and c and e and b < d or b > a and d and e and b < c:
    maior2 = b
if c > a and b and d and c < e or c > a and b and e and c < d or c > a and d and e and c < b:
    maior2 = c
if d > a and b and c and d < e or d > a and b and e and d < c or d > a and c and e and d < b:
    maior2 = d
if e > b and c and d and e < a or e > c and d and a and e < b or e > a and b and c and e < d:
    maior2 = e
menor2 = a
if b < a and c and d and b > e or b < a and c and e and b > d or b < a and d and e and b > c:
    menor2 = b
if c < a and b and d and c > e or c < a and b and e and c > d or c < a and d and e and c > b:
    menor2 = c
if d < a and b and c and d > e or d < a and b and e and d > c or d < a and c and e and d > b:
    menor2 = d
if e < b and c and d and e > a or e < c and d and a and e > b or e < a and b and c and e > d:
    menor2 = e
print("O quadrado do segundo maior valor inserido é {}".format(maior2**2))
print("O quadrado do segundo menor valor inserido é {}".format(menor2**2))