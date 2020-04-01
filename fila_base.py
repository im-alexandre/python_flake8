class FilaBase:
    codigo = 0
    fila = []
    clientes_atendidos = []
    senha_atual = None

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1
