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
        self.extrato()
    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        self.extrato()

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite
    def set_limite(self, limite):
        self.__limite = limite

    def __str__(self) -> str:
        print(f"Conta titular: {self.__titular}, conta: {self.__numero}, saldo atual: {self.__saldo}, seu limite: {self.__limite}")


        

# testando

c = Conta(321, "Marco", 100.0, 1000.0)

cp = Conta(123, "Polly", 100.0, 1000)
cp.__str__()
c.__str__()
""" cp.transferir(100.0, cp, c) 
pra nao fazer isso é so add self, envez de origem"""
cp.transferir(100, c)


cp.set_limite(2000)
c.get_limite()
cp.extrato()

""" 
c.extrato()
c.depositar(12)
c.extrato()
c.sacar(100)
c.extrato()
c.depositar(2000)
c.extrato() """