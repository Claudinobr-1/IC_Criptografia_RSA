import math

def Etapa2(P, n, v):
    lista = []
    if P*P > n:
        for i in range(len(v)):
            if v[i] == 1:
                lista.append(2*(i+1)+1)
        print(lista)
    else:
        Etapa3(P, n, v)

def Etapa3(P, n, v):
    if v[((P-1)//2)-1] == 0:
        P += 2
        Etapa2(P, n, v)
    else:
        Etapa4(P, n, v)

def Etapa4(P, n, v):
    T = P*P
    while T <= n:
        v[((T-1)//2)-1] = 0
        T += 2*P
    P += 2
    Etapa2(P, n, v)

def main():
    n = int(input("Insira o valor de n:"))
    v = []
    for i in range((n-1)//2):
        v.append(1)
    P = 3
    
    Etapa2(P, n, v)

main()