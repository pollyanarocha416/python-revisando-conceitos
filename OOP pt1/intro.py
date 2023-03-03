

def criar_conta(num, titular, saldo, limite):
    conta = {"num": num, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def depositar(conta, valor):
     conta["saldo"] += valor


def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))

