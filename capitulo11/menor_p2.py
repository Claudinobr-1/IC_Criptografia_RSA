import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    limit = math.isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def next_prime(n: int) -> int:
    if n < 2:
        return 2
    candidate = n + 1 if n % 2 == 0 else n + 2
    while not is_prime(candidate):
        candidate += 2
    return candidate

def fatores_primos_unicos(p: int) -> list[int]:
    fatores = []
    
    if p % 2 == 0:
        fatores.append(2)
        while p % 2 == 0:
            p //= 2

    fator = 3
    while fator * fator <= p:
        if p % fator == 0:
            fatores.append(fator)
            while p % fator == 0:
                p //= fator
        fator += 2

    if p > 1:
        fatores.append(p)

    return fatores

def eh_raiz_primitiva(g: int, p: int, fatores_p_menos_1: list[int]) -> bool:
    p_menos_1 = p - 1
    for q in fatores_p_menos_1:
        if pow(g, p_menos_1 // q, p) == 1:
            return False
    return True

def menor_p(a: int):
    raiz = math.isqrt(a)
    if a <= 1 or raiz * raiz == a:
        print(f"{a} não é raiz primitiva de nenhum p > 3 (é quadrado perfeito ou <= 1)")
        return

    p = next_prime(a)
    while True:
        # 1. Fatora p - 1 apenas UMA vez para este primo p
        fatores = fatores_primos_unicos(p - 1)
        
        # 2. Testa 'a' primeiro!
        if eh_raiz_primitiva(a, p, fatores):
            # 3. Só testa se existe g < a menor se 'a' já passou no teste
            control = True
            for g in range(2, a):
                if eh_raiz_primitiva(g, p, fatores):
                    control = False
                    break # Interrompe imediatamente ao achar uma raiz menor

            if control:
                print(f"{a} é a menor raiz primitiva para o grupo modulo {p}")
                return

        p = next_prime(p)

def main():
    a = int(input("Insira um número inteiro positivo a: "))
    menor_p(a)

if __name__ == "__main__":
    main()