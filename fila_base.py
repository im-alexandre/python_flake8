import abc


class FilaBase(metaclass=abc.ABCMeta):
    codigo = 0
    fila = []
    clientes_atendidos = []
    senha_atual = None

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    @abc.abstractmethod
    def chama_cliente(self):
        ...

    def insere_cliente(self):
        self.fila.append(self.senha_atual)

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()
