def receber_num():
    while True:
        try:
            num1 = float(input('Informe um número:'))
            return num1
        except Exception as err:
            print(f'Informe número!\n{err}')

def dividir(num1, num2):
    try:
        divisao = num1/num2
    except ZeroDivisionError as err:
        print(f'Não pode dividir por zero\n{err}')
        
        
num1 = receber_num()
num2 = receber_num()
dividir(num1, num2)