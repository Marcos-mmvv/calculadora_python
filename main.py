# Calculadora Simples

while True:

    x = str(input('Informe o primeiro número: ')).replace(',' , '.')
    y = str(input('Informe o segundo número: ')).replace(',' , '.')

    x = float(x)
    y = float(y)

    print('Escolha a operação desejada: \n')
    print('"+" para somar.')
    print('"-" para subtrair.')
    print('"*" para multiplicar')
    print('"/" para dividir.')
    print('"%" para encontrar o resto da divisão.')
    
    op = input('Operação desejada: ')

    match op:
        case '+':
            print(f'A soma é: {x + y}.')
        case '-':
            print(f'A subtração é: {x - y}.')
        case '*':
            print(f'A multiplicação é: {x * y}.')
        case '/':
            print(f'A divisão é: {x / y:.2f}.')
        case '%':
            print(f'O resto da divisão  é: {x % y:.2f}.')
        case _:
            print('Operação inválida')
            continue

    # Perguntar para o usuário se ele deseja continuar

    continuar = input('Continuar calculando? (s/n) ')

    # Verifica a opção do usuário
    
    if continuar == "s":
        continue
    elif continuar == "n":
        break
    else:
        print('Opção digitada inválida. \nCalculadora reiniciada.')
        continue







