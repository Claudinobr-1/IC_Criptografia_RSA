def simplifica(A, E, n): # simplificação módulo por expansão binária
    P = 1
    while E != 0:
        if E % 2 != 0:
            P = (A * P) % n
            E = (E - 1) // 2
        else:
            E //= 2
        A = (A * A) % n
    
    return P

def verifica(p): # essa função verifica o limite utilizando r
    r = 0
    limite_r = ((2 ** (p // 2)) - 1) // (2 * p)

    while r <= limite_r:
        q = r * 2 * p + 1
        
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