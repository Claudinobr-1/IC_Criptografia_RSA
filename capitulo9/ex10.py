def fermat(p):
    r = exp_binaria(2, 32, p)
    n = valor_n(p)
    i = 5

    while i < n:
        if r == p - 1:
            print(f"{p} divide F({i})")    
            return
        
        r = (r * r) % p
        i += 1
    
    print(f"Não existe algum F(m) que p divida")

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

def valor_n(p):
    n = 0
    p -= 1

    while p % 2 == 0:
        n += 1
        p //= 2

    return n

def main():
    p = int(input("Insira um número primo p: "))
    fermat(p)
    
if __name__ == "__main__":
    main()