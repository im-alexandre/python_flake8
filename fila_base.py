import abc
from typing import List

from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass=abc.ABCMeta):
    codigo = TAMANHO_PADRAO_MINIMO
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    @abc.abstractmethod
    def chama_cliente(self, caixa: int):
        ...

    def insere_cliente(self):
        self.fila.append(self.senha_atual)

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()
