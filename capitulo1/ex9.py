import random

def mdc(a,b):
    if b > a:
        a, b = b, a

    while b != 0:
        resto = a % b
        a = b
        b = resto

    return a

def main():
    ntotal = int(input("Indique a quantidade de pares a serem testados: "))
    
    for i in range(10):
        cont = 0
        for i in range(ntotal):
            a = random.randint(1,100)
            b = random.randint(1,100)
            if mdc(a,b) == 1:
                cont += 1

        print(f"Pares coprimos encontrados: {cont} de {ntotal}")
        print(f"Porcentagem: {(cont/ntotal)*100:.2f}%")

main()