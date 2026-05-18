def odd(A, P, E, n):
    P = (A*P) % n
    E = (E - 1) // 2
    return (P, E)

def even(E):
    return E // 2

def subs(A, n):
    return (A*A) % n

def main():
    a, k, n = map(int, input("Digite os valores de a, k e n: ").split())
    A = a
    P = 1
    E = k

    while E != 0:
       if E % 2 == 0:
            E = even(E)
       else:
            P, E = odd(A, P, E, n)
       A = subs(A, n)

    print(f"{a}^{k} = {P} (mod {n})")

main()