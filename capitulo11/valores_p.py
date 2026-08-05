import math
import time

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
        # Retorna None para indicar que não há p válido (é quadrado perfeito ou <= 1)
        return None

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
                return p

        p = next_prime(p)

def main():
    # 10 entradas selecionadas no intervalo entre 10 e 60. 
    # Foram omitidos propositalmente quadrados perfeitos (16, 25, 36, 49) 
    # para garantir que todas as entradas testadas possuam um valor 'p' correspondente.
    entradas = [10, 15, 20, 26, 30, 35, 42, 47, 50, 60]
    
    # Cabeçalho da tabela
    print(f"{'Entrada (a)':<15} | {'Saída (p)':<15} | {'Tempo de Execução (s)':<25}")
    print("-" * 60)
    
    for a in entradas:
        start_time = time.perf_counter()
        
        p = menor_p(a)
        
        end_time = time.perf_counter()
        duracao = end_time - start_time
        
        p_str = str(p) if p is not None else "Quadrado Perfeito"
        
        # Imprime a linha da tabela formatada
        print(f"{a:<15} | {p_str:<15} | {duracao:<25.6f}")

if __name__ == "__main__":
    main()