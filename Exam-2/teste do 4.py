def fatorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * fatorial(n - 1)

n=5
e=0
i=0

while(i!=n):
  e=e+1/fatorial(i)
  i=i+1

print(e)