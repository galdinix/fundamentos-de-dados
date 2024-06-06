class NumeroNegativoException(Exception):
    pass

def filtra_positivos(lista_numeros):
    lista_positivos = []
    try:
        for numero in lista_numeros:
            if numero < 0:
                raise NumeroNegativoException() 
            lista_positivos.append(numero) 
    finally: 
        return lista_positivos  
          
numeros = [10, 15, -3, 7, 22]  
lista_positivos = filtra_positivos(numeros) 
print("Lista de números positivos:", lista_positivos) 
