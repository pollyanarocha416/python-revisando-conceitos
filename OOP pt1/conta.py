class Conta:
    # self sabe o endereco
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def __str__(self) -> str:
        print(f"Conta titular: {self.__titular}, conta: {self.__numero}, saldo atual: {self.__saldo}, seu limite: {self.__limite}")



# testando
c = Conta(123, "Polly", 1000, 1000)
c.__str__()
c.sacar(32)
c.extrato()
""" 
c.extrato()
c.depositar(12)
c.extrato()
c.sacar(100)
c.extrato()
c.depositar(2000)
c.extrato() """