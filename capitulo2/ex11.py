def div(r):
    n = 0
    for i in range(1, r+1):
        if r % i == 0:
            n += 1
    return n


def main():
    r = int(input("Coloque o valor de r: "))
    lista = []
    for i in range(1, r):
        di = div(i)
        is_hcn = True
        for j in range(1, i):          
            if div(j) > di:            
                is_hcn = False
                break
        if is_hcn:
            lista.append(i)

    print(lista)

main()