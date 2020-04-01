from fila_base import FilaBase


class FilaNormal(FilaBase):

    def gerasenhaatual(self) -> None:
        self.senhaatual = f'NM{self.codigo}'

    def atualizafila(self) -> None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhaatual)

    def chamacliente(self, caixa) -> str:
        clienteatual = self.fila.pop(0)
        self.clintesatendidos.append(clienteatual)
        return f'Cliente atual: {clienteatual}, dirija-se ao caixa {caixa}'
