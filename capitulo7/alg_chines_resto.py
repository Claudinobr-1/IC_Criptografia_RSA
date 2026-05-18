def inverso(Ni, modulo):
    for i in range(1, modulo):
        if (Ni * i) % modulo == 1:
            return i
    return 1

def tcr(valores):
    inc = len(valores)
    partes = 0
    
    N_total = 1
    for v in valores:
        N_total *= v[1]

    for i in range(inc):
        ai = valores[i][0]
        ni = valores[i][1]

        Ni = N_total // ni
        yi = inverso(Ni, ni)

        partes += ai * Ni * yi

    resultado = partes % N_total
    print(f"x = {resultado} mod({N_total})")

def main():
    valores = []
    e = int(input("Insira a quantidade de congruências do sistema: "))
    for i in range(e):
        print(f"Insira o valor do resto e do módulo da congruência {i+1}:")
        valores.append(list(map(int, input().split())))

    tcr(valores)
    
main()
