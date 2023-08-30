menu = """

[s] Sacar
[d] Depositar
[e] Extrato
[x] Sair

"""

saldo = 0
LIMITE = 500
extrato = []
saques = 0
LIMITE_SAQUES = 3

def sacar(saldo_atual, valor):
    saldo_atual -= valor
    return saldo_atual, f"R${valor} foi sacado, R${saldo_atual} disponível."

def depositar(saldo_atual, valor):
    saldo_atual += valor
    return saldo_atual, f"R${valor} foram depositados, novo saldo: {saldo_atual}"




while True:
    opcao = input(menu)

    if opcao == "s":
        print("Digite o valor a ser sacado:")
        valor = float(input())

        if 0 < valor < LIMITE and valor <= saldo and saques < LIMITE_SAQUES:
            saldo, mensagem = sacar(saldo, valor)
            saques += 1
            extrato.append(f"R${valor:.2f} sacado")
            print(mensagem)

        else:
            print("Operação inválida")
            continue

    if opcao == "d":
        print("Digite o valor a ser depositado:")
        valor = float(input())

        if valor > 0:
            saldo, mensagem = depositar(saldo, valor)
            extrato.append(f"R${valor:.2f} depositado")

        else:
            print("Operação inválida")

    if opcao == "e":
        print("EXTRATO".center(20, "#"))

        for elements in extrato:
            print(elements)

        print(f"Saldo atual: R${saldo:.2f}")

        print("EXTRATO".center(20, "#"))

    if opcao == "x":
        break
