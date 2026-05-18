import itertools

# 1. Gerar primos até 1000
def get_primos(limite):
    primos = []
    v = [True] * (limite + 1)
    for p in range(2, limite + 1):
        if v[p]:
            primos.append(p)
            for i in range(p * p, limite + 1, p):
                v[i] = False
    return primos

# 2. Testar se a combinação forma um número de Carmichael
def eh_carmichael(fatores):
    # n = produto dos fatores
    # Para cada p em fatores, precisamos que (n-1) % (p-1) == 0
    # Ou seja: n % (p-1) == 1
    for p_i in fatores:
        modulo = p_i - 1
        n_mod = 1
        for f in fatores:
            n_mod = (n_mod * f) % modulo
        
        if n_mod != 1:
            return False
    return True

# 3. Execução para d primos
def resolver(d, lista_primos):
    print(f"\nBuscando números de Carmichael com d={d}...")
    # O itertools.combinations evita pegar o mesmo primo duas vezes
    # e evita permutações repetidas (ex: 3,11,17 é o mesmo que 17,3,11)
    count = 0
    for combo in itertools.combinations(lista_primos, d):
        if eh_carmichael(combo):
            print(f"Fatores: {combo}")
            count += 1
    if count == 0: print("Nenhum encontrado.")

def main():
    try:
        d = int(input("Insira o valor de d: "))
    except ValueError:
        print("Por favor, insira o valor de um número inteiro")
        return
    
    primos = get_primos(1000)
    resolver(d, primos)

if __name__ == "__main__":
    main()