def teste_miller(n, b):
    q = n-1
    k = 0
    while q % 2 != 1:
        q /= 2
        k += 1
    
    i = 0
    r = (b**q) % n
    while i < k:
        if (i == 0 and r == 1) or (i >= 0 and r == n-1):
            return 1 # candidato à primo
        i += 1
        r = (r*r) % n
    return 0 # com certeza é composto

def menor_pseu(b):
    compostos = get_compostos(10000)
    for i in range(len(compostos)):
        if teste_miller(compostos[i], b) == 1:
            return compostos[i]
    
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
        b = int(input("Insira o valor da base b: "))
    except ValueError:
        print("Por favor, insira uma base b > 1")
        return
    
    print(menor_pseu(b))

if __name__ == "__main__":
    main()

    