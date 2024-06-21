print('\nBem vindo(a)! Selecione uma opção abaixo:')
menu = '''
    [1] Depósitos
    [2] Saques
    [3] Extrato
    [4] Sair
    
Digite a operação desejada: 
'''

saldo = 0
limite = 500
extrato = ' '
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == '1':
        print('\nDepósitos')
        valor = float(input('Digite o valor de depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print('A operação falhou! O valor informado é inválido.')

    elif opcao == '2':
        print('\nSaques')
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Falha na operação! Saldo insuficiente.')

        elif excedeu_limite:
            print('Falha na operação! O valor do saque excede o limite diário.')

        elif excedeu_saques:
            print('Falha na operação! Número máximo de saques excedido.')

        elif valor > 0:
            saldo -= valor # Decrementa o valor do saldo
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1 # Incrementa a variável para contabilizar a partir do número de saque anterior

        else:
            print('Falha na operação! O valor informado é inválido.')


    elif opcao == '3':
        print('=*' * 5 + 'Extrato' + '=*' * 5)
        print('Não foram realizadas movimentações.' if not extrato else extrato) # A condição ternária exibe o valor, caso tenha sido realizada alguma operação
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('=*' * 10)


    elif opcao == '4':
        break

    else:
        print('Operação inválida! Por favor, selecione somente uma das opções existentes.')




