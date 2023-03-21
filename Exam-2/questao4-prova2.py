def e():
    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            n = n*(n-1)
        return n
    soma = 1/fatorial(0)+1/fatorial(1)+1/fatorial(2)+1/fatorial(3)+1/fatorial(4)+1/fatorial(5)
    print(soma)
e()