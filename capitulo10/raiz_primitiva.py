import random
from collections import Counter

def mdc(a, b):
    r = a % b

    while r != 0:
        a = b
        b = r
        r = a % b
        if r == 0:
            break

    return b

def mmc(a, b):
    return (a * b) // mdc(a, b)

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

def fatora(p):
    fatores = []

    while p % 2 == 0:
        fatores.append(2)
        p //= 2

    fator = 3
    while fator * fator <= p:
        while p % fator == 0:
            fatores.append(fator)
            p //= fator
        fator += 2

    if p > 1:
        fatores.append(p)

    return fatores

def ordem_elemento(p, a): #Método das potências
    k = 1
    fatores = Counter(fatora(p-1))

    for i, j in fatores.items():
        for w in range(j, -1, -1):
            if exp_binaria(a, (p - 1) // (i ** w), p) == 1:
                k *= i ** (j - w)
                break

    return k

def multiplicidade(x, o):
    count = 0
    while x % o == 0:
        count += 1
        x //= o
    
    return count

def raiz_primitiva(p): # método de Gauss
    a = 2
    fatores = Counter(fatora(p - 1))

    while True:
        k = ordem_elemento(p, a)
        if k == p - 1:
            return a
        
        while True: # encontra um valor de b que não seja uma potência de a mod p
            b = random.randint(2, p - 1)

            if exp_binaria(b, k, p) != 1:
                break

        r = ordem_elemento(p, b)
        u_exp = 1
        v_exp = 1

        for i, j in fatores.items():
            alpha = multiplicidade(i, k)
            beta = multiplicidade(i, r)

            if alpha > beta:
                v_exp *= i ** beta
            else:
                u_exp *= i ** alpha

        comp_a = exp_binaria(a, u_exp, p)
        comp_b = exp_binaria(b, v_exp, p)

        a = (comp_a * comp_b) % p
        
def main():
    p = int(input("Insira o valor de p: "))
    print(f"O valor da raiz primitiva de U({p}) é {raiz_primitiva(p)}")

if __name__ == "__main__":
    main()