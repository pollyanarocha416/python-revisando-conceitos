from typing import Union
from fila_normal import fila_normal
from fila_prioritaria import FilaPrioritaria
from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila) -> Union[fila_normal, FilaPrioritaria]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return fila_normal()
        elif tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo de fila não existe')
