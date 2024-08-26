import time
import os

menu = """
[d] Depositar
[s] Sacar
[t] Transferir
[e] Extrato
[q] Sair

=> Escolha: """

saldo = 0
limite = 500
extrato = []
numero_saque = 0
LIMITE_SAQUE = 3

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    opcao = input(menu).lower()
    limpar_tela()

    if opcao == 'd':
        valor = float(input('Valor do depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato.append(('Depósito', valor))
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print('Valor inválido para depósito.')
    
    elif opcao == 's':
        valor = float(input('Valor do saque: '))
        excedeu_saldo = valor > saldo 
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print('Saldo insuficiente.')
        elif excedeu_limite:
            print('Limite de saque excedido.')
        elif excedeu_saque:
            print('Limite de saques diários excedido.')
        else:
            saldo -= valor
            numero_saque += 1
            extrato.append(('Saque', valor))
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    elif opcao == 't':
        valor = float(input('Valor da transferência: '))
        excedeu_saldo = valor > saldo 
        
        if excedeu_saldo:
            print('Saldo insuficiente para transferência.')
        else:
            saldo -= valor
            extrato.append(('Transferência', valor))
            print(f"Transferência de R$ {valor:.2f} realizada com sucesso.")

    elif opcao == 'e':
        print("Extrato:")
        if extrato:
            for operacao, valor in extrato:
                print(f"{operacao}: R$ {valor:.2f}")
        else:
            print("Não foram realizadas operações.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")

    elif opcao == 'q':
        print('Saindo...')
        break
    
    else:
        print("Opção inválida. Tente novamente.")
    
    time.sleep(2)
    limpar_tela()
