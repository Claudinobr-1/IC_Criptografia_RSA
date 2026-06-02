def simplifica(A, E, n):
    P = 1
    while E != 0:
        if E % 2 != 0:
            P = (A * P) % n
            E = (E - 1) // 2
        else:
            E //= 2
        A = (A * A) % n
    
    return P

def verifica(p): # essa versão da função compara o valor q <= 2 ** (p // 2)
    r = 0
    q = 1
    limite_q = 2 ** (p // 2)

    while True:
        q = r * 2 * p + 1
        if q > limite_q:
            break
        
        if simplifica(2, p, q) == 1:
            print(f"O menor fator primo de M({p}) é {q}")
            return
        r += 1

    print(f"M({p}) é primo")

def main():
    p = int(input("Insira um número primo p: "))
    verifica(p)

if __name__ == "__main__":
    main()