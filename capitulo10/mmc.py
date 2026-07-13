def mdc(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
        if r == 0:
            break
    return b

def mmc(a, b): # O menor número que a e b dividem simultaneamente
    print(f"O mmc entre {a} e {b} é {(a * b) // mdc(a, b)}")

def main():
    a, b = map(int, input("Digite os valores de a e b: ").split())
    mmc(a, b)

if __name__ == "__main__":
    main()