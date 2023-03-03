class Conta:
    # self sabe o endereco
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ...")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def __str__(self) -> str:
        print(f"Conta titular: {self.titular}, conta: {self.numero}, saldo atual: {self.saldo}, seu limite: {self.limite}")



# testando
c = Conta(123, "Polly", 1000, 1000)
c.__str__()
c.depositar(300)
c.extrato()
""" 
c.extrato()
c.depositar(12)
c.extrato()
c.sacar(100)
c.extrato()
c.depositar(2000)
c.extrato() """