import math

def crivo_otimizado(n):
    if n < 3:
        return [2] if n == 2 else []

    # 'v' armazena apenas os ímpares. 
    # O índice 'i' representa o número: 2i + 3
    # Ex: i=0 -> 3, i=1 -> 5, i=2 -> 7...
    tamanho = (n - 3) // 2 + 1
    v = bytearray([1]) * tamanho 
    
    limite = int(math.sqrt(n))
    p = 3
    
    # Substitui a Etapa 2, 3 e 4 por um loop controlado
    while p <= limite:
        # Etapa 3: Verificar se P é primo (se v[indice] == 1)
        idx_p = (p - 3) // 2
        if v[idx_p] == 1:
            # Etapa 4: Marcar múltiplos de P começando de P*P
            # O pulo é de 2*P para garantir que só cairemos em ímpares
            inicio_multiplo = (p * p - 3) // 2
            passo = p
            
            # Preenchimento em massa (fatiamento de lista é extremamente veloz em Python)
            v[inicio_multiplo : tamanho : passo] = bytearray([0]) * len(range(inicio_multiplo, tamanho, passo))
        
        p += 2
    
    # Gerar a lista final
    lista_primos = [2]
    for i in range(tamanho):
        if v[i] == 1:
            lista_primos.append(2 * i + 3)
            
    return lista_primos

def main():
    try:
        n = int(input("Insira o valor de n: "))
        primos = crivo_otimizado(n)
        print(f"Encontrados {len(primos)} números primos.")
        if n < 100: # Evita poluir o terminal com listas gigantes
            print(primos)
    except ValueError:
        print("Entrada inválida.")

if __name__ == "__main__":
    main()