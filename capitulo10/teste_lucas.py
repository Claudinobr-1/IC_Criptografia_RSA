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

def teste_lucas(b, n):
    fatores = Counter(fatora(n - 1))

    if exp_binaria(b, n - 1, n) == 1:
        for i, j in fatores.items():
            if exp_binaria(b, (n - 1) // i, n) == 1:
                print(f"{n} é composto")
                return
            
        print(f"{n} é primo")
    
    else:
        print(f"{n} é composto")

def main():
    b, n = map(int, input("Insira o valor da base b e do módulo n: ").split())
    teste_lucas(b, n)


if __name__ == "__main__":
    main()