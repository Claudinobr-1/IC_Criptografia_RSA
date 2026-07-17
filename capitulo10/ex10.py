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

def teste_pepin(n):
    modulo = (2 ** (2 ** n)) + 1
    valor = exp_binaria(5, 2 ** ((2 ** n) - 1), modulo)

    if valor == modulo - 1:
        print(f"F({n}) é primo")
    else:
        print(f"F({n}) é composto")

def main():
    n = int(input("Insira o valor do expoente n do número de Fermat: "))
    teste_pepin(n)

if __name__ == "__main__":
    main()