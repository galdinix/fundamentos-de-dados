import random

# Função para realizar a busca binária
def busca_binaria(array, alvo):
    inicio = 0
    fim = len(array) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        # Se o elemento do meio for o alvo, retornamos o índice
        if array[meio] == alvo:
            return meio

        # Se o alvo for menor que o elemento do meio, procuramos na metade esquerda do array
        elif alvo < array[meio]:
            fim = meio - 1

        # Se o alvo for maior que o elemento do meio, procuramos na metade direita do array
        else:
            inicio = meio + 1

    # Se o alvo não estiver no array, retornamos -1
    return -1

# Criar um array ordenado de 1000 números inteiros
array = sorted(random.sample(range(1, 11), 10))

# Gerar um número aleatório para buscar no array
alvo = random.choice(array)

# Executar a busca binária
indice = busca_binaria(array, alvo)

# Imprimir o resultado
if indice != -1:
    print(f'O alvo {alvo} foi encontrado no índice {indice}.')
else:
    print(f'O alvo {alvo} não foi encontrado no array.')


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        print(i)
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

array = [12, 11, 13, 5, 6]
insertion_sort(array)
print("Array ordenado usando Insertion Sort:")
print(array)
