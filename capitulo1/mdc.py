def mdc(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
        if r == 0:
            break
    return b

def main():
    a, b = map(int, input("Digite os valores de a e b: ").split())
    print(f"O mdc de {a} e {b} é {mdc(a, b)}")

main()
