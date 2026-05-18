def mdc(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
        if r == 0:
            break
    return b

def mdc_ext(a, b, c):
    if c % mdc(a, b) != 0:
        print("Não existem soluções para essa equação")
    else:
        old_r, r = a, b
        old_s, s = 1, 0  # Coeficientes para 'a'
        old_t, t = 0, 1  # Coeficientes para 'b'

        while r != 0:
            quociente = old_r // r
            old_r, r = r, old_r - quociente * r
            old_s, s = s, old_s - quociente * s
            old_t, t = t, old_t - quociente * t

        # old_r: MDC(a,b)
        # old_s: x (coeficiente de a)
        # old_t: y (coeficiente de b)
        print(f"x = {old_s} e y = {old_t}")

def main():
    a, b, c = map(int, input("Insira os valores de a, b e c: ").split())
    mdc_ext(a, b, c)

main()
