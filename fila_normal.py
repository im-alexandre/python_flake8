from fila_base import FilaBase


class FilaNormal(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senhaatual = f'NM{self.codigo}'

    def chama_cliente(self, caixa) -> str:
        clienteatual = self.fila.pop(0)
        self.clintesatendidos.append(clienteatual)
        return f'Cliente atual: {clienteatual}, dirija-se ao caixa {caixa}'
