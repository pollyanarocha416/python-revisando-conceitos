from fila_base import FilaBase


class fila_normal(FilaBase):
    def gerasenhaatual(self) -> None:
        self.senha_atual = f'NM{self.codigo}'

    def atualizafila(self) -> None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senha_atual)

    def chamacliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}'
