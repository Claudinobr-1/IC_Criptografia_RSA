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

def main():
    a, k, n = map(int, input("Digite os valores de a, k e n: ").split())
    P = simplifica(a, k, n)

    print(f"{a}^{k} = {P} (mod {n})")

if __name__ == "__main__":
    main()
