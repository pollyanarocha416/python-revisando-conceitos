

def criar_conta(num, titular, saldo, limite):
    conta = {"num": num, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def depositar(conta, valor):
    conta["saldo"] += valor
    print

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))

nova_conta = criar_conta(123, "polly", 100, 100)
depositar(nova_conta, 200.0)
extrato(nova_conta)