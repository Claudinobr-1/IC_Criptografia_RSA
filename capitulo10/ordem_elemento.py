from collections import Counter

def exp_binaria(A, E, n):
    P = 1
    while E != 0:
        if E % 2 != 0:
            P = (A * P) % n
            E = (E - 1) // 2
        else:
            E //= 2
        A = (A * A) % n
    
    return P

def fatora(p):
    fatores = []

    while p % 2 == 0:
        fatores.append(2)
        p //= 2

    fator = 3
    while fator * fator <= p:
        while p % fator == 0:
            fatores.append(fator)
            p //= fator
        fator += 2

    if p > 1:
        fatores.append(p)

    return fatores

def ordem_elemento(p, a): #Método das potências
    k = 1
    fatores = Counter(fatora(p-1))

    for i, j in fatores.items():
        for w in range(j, -1, -1):
            if exp_binaria(a, (p - 1) // (i ** w), p) == 1:
                k *= i ** (j - w)
                break

    print(f"A ordem de {a} é igual a {k}")

def main():
    p = int(input("Insira um número primo p: "))
    a = int(input("Digite um elemento a pertencente a U(p): "))
    ordem_elemento(p, a)    

if __name__ == "__main__":
    main()