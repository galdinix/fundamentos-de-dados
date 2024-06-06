def dividir():
    try:
        n1 = float(input('Informe um número:'))
        n2 = float(input('Informe um número:'))
        result = n1 / n2
        print(f'resultado da divisao: {result}')
    except ValueError as ex:
        print(f'Erro de tipo! {ex}')
        dividir()
    except ZeroDivisionError as ex:
        print(f'Erro ao dividir por 0')
        dividir()

dividir()