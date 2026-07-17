def teste_wilson(n):
    v_final = 1
    for i in range(2, n, 1):
        v_final *= i
        v_final = v_final % n

    if v_final == n - 1:
        print(f"{n} é primo")
    else:
        print(f"{n} não é primo")
    
def main():
    n = int(input("Insira o valor de n: "))
    teste_wilson(n)

if __name__ == "__main__":
    main()