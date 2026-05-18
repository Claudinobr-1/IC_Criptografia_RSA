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
            print("Teste inconclusivo")
            return
        i += 1
        r = (r*r) % n
    print("n é composto")
    

def main():
    n = int(input("Insira um inteiro ímpar n: "))
    b = int(input("Insira o valor da base 1 < b < n-1: "))

    teste_miller(n, b)

if __name__ == "__main__":
    main()