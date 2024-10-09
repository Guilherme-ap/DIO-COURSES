import time
import os

menu = """
[c] Criar Usuário
[n] Criar Nova Conta
[l] Listar Contas
[d] Depositar
[s] Sacar
[t] Transferir
[e] Extrato
[q] Sair

=> Escolha: """

usuarios = {}
contas = []
saldo_inicial = 0
limite = 500
LIMITE_SAQUE = 3

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    if cpf in usuarios:
        print("Usuário já cadastrado.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (rua, número - bairro - cidade/sigla estado): ")
    usuarios[cpf] = {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}
    print(f"Usuário {nome} criado com sucesso!")

def criar_conta():
    cpf = input("Informe o CPF do titular da conta: ")
    if cpf not in usuarios:
        print("Usuário não encontrado. Crie um usuário antes de abrir uma conta.")
        return

    numero_conta = len(contas) + 1
    contas.append({"numero_conta": numero_conta, "cpf": cpf, "saldo": saldo_inicial, "extrato": [], "numero_saque": 0})
    print(f"Conta {numero_conta} criada com sucesso para o usuário {usuarios[cpf]['nome']}.")

def listar_contas():
    if not contas:
        print("Nenhuma conta foi criada.")
    else:
        for conta in contas:
            print(f"Conta {conta['numero_conta']} - Titular: {usuarios[conta['cpf']]['nome']} - Saldo: R$ {conta['saldo']:.2f}")

def encontrar_conta(numero_conta):
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            return conta
    return None

def depositar():
    numero_conta = int(input("Informe o número da conta: "))
    conta = encontrar_conta(numero_conta)
    
    if not conta:
        print("Conta não encontrada.")
        return

    valor = float(input("Valor do depósito: "))
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"].append(('Depósito', valor))
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido para depósito.")

def sacar():
    numero_conta = int(input("Informe o número da conta: "))
    conta = encontrar_conta(numero_conta)
    
    if not conta:
        print("Conta não encontrada.")
        return

    valor = float(input("Valor do saque: "))
    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > limite
    excedeu_saque = conta["numero_saque"] >= LIMITE_SAQUE

    if excedeu_saldo:
        print("Saldo insuficiente.")
    elif excedeu_limite:
        print("Limite de saque excedido.")
    elif excedeu_saque:
        print("Limite de saques diários excedido.")
    else:
        conta["saldo"] -= valor
        conta["numero_saque"] += 1
        conta["extrato"].append(('Saque', valor))
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

def transferir():
    numero_conta_origem = int(input("Informe o número da conta de origem: "))
    conta_origem = encontrar_conta(numero_conta_origem)
    
    if not conta_origem:
        print("Conta de origem não encontrada.")
        return

    numero_conta_destino = int(input("Informe o número da conta de destino: "))
    conta_destino = encontrar_conta(numero_conta_destino)
    
    if not conta_destino:
        print("Conta de destino não encontrada.")
        return

    valor = float(input("Valor da transferência: "))
    if valor > conta_origem["saldo"]:
        print("Saldo insuficiente para transferência.")
    else:
        conta_origem["saldo"] -= valor
        conta_destino["saldo"] += valor
        conta_origem["extrato"].append(('Transferência enviada', valor))
        conta_destino["extrato"].append(('Transferência recebida', valor))
        print(f"Transferência de R$ {valor:.2f} realizada com sucesso.")

def exibir_extrato():
    numero_conta = int(input("Informe o número da conta: "))
    conta = encontrar_conta(numero_conta)
    
    if not conta:
        print("Conta não encontrada.")
        return

    print("Extrato:")
    if conta["extrato"]:
        for operacao, valor in conta["extrato"]:
            print(f"{operacao}: R$ {valor:.2f}")
    else:
        print("Não foram realizadas operações.")
    print(f"\nSaldo atual: R$ {conta['saldo']:.2f}")

# Loop principal
while True:
    opcao = input(menu).lower()
    limpar_tela()

    if opcao == 'c':
        criar_usuario()

    elif opcao == 'n':
        criar_conta()

    elif opcao == 'l':
        listar_contas()

    elif opcao == 'd':
        depositar()

    elif opcao == 's':
        sacar()

    elif opcao == 't':
        transferir()

    elif opcao == 'e':
        exibir_extrato()

    elif opcao == 'q':
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")

    time.sleep(2)
    limpar_tela()
