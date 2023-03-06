class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel
    
    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if  (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"o valor {valor} passou o limite")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite


    @staticmethod
    def codigo_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
        

c = Conta(234, "polly", 1000, 2000)
c.codigo_banco()
c.saca(2100)
c.saca(30000)
c.extrato()
""" 
c.extrato()
c.depositar(12)
c.extrato()
c.sacar(100)
c.extrato()
c.depositar(2000)
c.extrato() """