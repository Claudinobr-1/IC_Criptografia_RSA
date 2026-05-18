from collections import Counter

def totiente(fatores):
    # Organiza os fatores primos de acordo com sua multiplicidade
    contagem = Counter(fatores)
    phi = 1

    for p, k in contagem.items(): # items() organiza em um lista de tuplas
        phi *= (p ** (k - 1)) * (p - 1)

    return phi

def fatora(k):  #Gera lista dos fatores de K
    fatores = []

    while k % 2 == 0:
        fatores.append(2)
        k //= 2

    fator = 3
    while fator * fator <= k:
        while k % fator == 0:
            fatores.append(fator)
            k //= fator
        fator += 2

    if k > 1:
        fatores.append(k)

    return fatores

def main():
    k = int(input("Insira o valor de K: "))
    phi = totiente(fatora(k))
    print(f"O valor de phi de K é igual a {phi}")

if __name__ == "__main__":
    main()

# A função Phi basicamente busca responder à pergunta:
# Dado um número n, quantos números de 0 a n - 1 são
# cooprimos a n (mdc(a, n) = 1)?