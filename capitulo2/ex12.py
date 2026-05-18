import math

def eh_inteiro(n):
    return isinstance(n, int) or (isinstance(n, float) and n.is_integer())

def fermat(n):
    x = math.ceil(math.sqrt(n))
    if n == x**2:
        return (x, x)
    
    while x < ((n + 1)/2):
        y = math.sqrt(x**2 - n)
        if eh_inteiro(y):
            return (x + y, x - y)
        x += 1

    return 0

def main():
    n = int(input("Insira o valor de n: "))
    valor = fermat(n)
    if isinstance(valor, tuple):
        if valor[0] == valor[1]:
            print(f"{n} é um quadrado perfeito, cuja raiz é {valor[0]}")
        else:
            print(f"Dois dos fatores de {n} são {valor[0]} e {valor[1]}")
    else:
        print(f"{n} é um número primo")
    
main()
