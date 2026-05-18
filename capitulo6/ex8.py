def compara(A, E, n):
    """Calcula (A^E) % n usando exponenciação modular rápida."""
    P = 1
    A = A % n
    while E > 0:
        if E % 2 == 1:
            P = (P * A) % n
        A = (A * A) % n
        E = E // 2
    return P

def get_compostos(n):
    """Retorna uma lista de números ímpares compostos até n usando o Crivo."""
    v = [1] * ((n // 2) + 1)
    limite = int(n**0.5)
    for p in range(3, limite + 1, 2):
        if v[p // 2] == 1:
            # Marca múltiplos de p como compostos (0)
            for i in range(p * p, n + 1, 2 * p):
                v[i // 2] = 0
    
    compostos = []
    for i in range(3, n + 1, 2):
        if v[i // 2] == 0: # Se foi marcado como composto
            compostos.append(i)
    return compostos

def main():
    try:
        r = int(input("Insira o limite superior (r): "))
    except ValueError:
        print("Por favor, insira um número inteiro.")
        return

    # 1. Gera apenas os ímpares compostos
    lista_compostos = get_compostos(r)
    pseu = []

    # 2. Testa se o composto se comporta como primo (Pseudoprimo)
    # Condição: a^(n-1) % n == 1
    for n in lista_compostos:
        if compara(2, n - 1, n) == 1 and compara(3, n - 1, n) == 1:
            pseu.append(n)

    print(f"Números ímpares compostos que passam no teste (bases 2 e 3) até {r}:")
    print(pseu)

if __name__ == "__main__":
    main()