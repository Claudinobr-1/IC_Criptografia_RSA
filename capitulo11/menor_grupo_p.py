import math
from collections import Counter

def is_prime(n: int) -> bool:
    # Verifica se n é primo (otimizado mod 6)
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Testa apenas números da forma 6k ± 1
    limit = math.isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def next_prime(n: int) -> int:
    # Retorna o menor primo estritamente maior que n
    if n < 2:
        return 2
    
    # Garante que começamos em um número ímpar > n
    candidate = n + 1 if n % 2 == 0 else n + 2
    
    while not is_prime(candidate):
        candidate += 2
        
    return candidate

def eh_inteiro(n):
    return isinstance(n, int) or (isinstance(n, float) and n.is_integer())

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

def verifica_fatores(a, p):
    fatores = Counter(fatora(p - 1))

    for i, j in fatores.items():
        if exp_binaria(a, (p - 1) // i, p) == 1:
            return 0

    return 1

def menor_p(a):
    if eh_inteiro(math.sqrt(a)) or a <= 1:
        print(f"{a} não é raiz primitiva de nenhum p > 3")
        return
    
    else:
        p = next_prime(a)
        while True:
            control = 1
            etapa1 = verifica_fatores(a, p)
            if etapa1 == 1:
                for g in range(2, a, 1):
                    if verifica_fatores(g, p) == 1:
                        control = 0

            if etapa1 == 1 and control == 1:
                print(f"{a} é a menor raiz primitiva para o grupo p modulo {p}")
                return

            p = next_prime(p)


def main():
    a = int(input("Insira um número inteiro positivo a: "))
    menor_p(a)

if __name__ == "__main__":
    main()