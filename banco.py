import contas
import pessoas


class Banco:
    """Classe para representar o banco"""

    def __init__(self,
                 agencias: list[int] | None = None,
                 clientes: list[pessoas.Pessoa] | None = None,
                 contas: list[contas.Conta] | None = None):
        """Inicializando os atributos"""

        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def checa_agencia(self, conta):
        """Checa se a agência existe no banco"""

        if conta.agencia in self.agencias:
            print('checa_agencia', True)
            return True
        print('checa_agencia', False)
        return False

    def checa_cliente(self, cliente):
        """Checa se o cliente existe no banco"""

        if cliente in self.clientes:
            print('checa_cliente', True)
            return True
        print('checa_cliente', False)
        return False

    def checa_conta(self, conta):
        """Checa se a conta existe no banco"""

        if conta in self.contas:
            print('checa_conta', True)
            return True
        print('checa_conta', False)
        return False

    def checa_conta_cliente(self, cliente, conta):
        """Checa se a conta informada é a mesma do cliente"""

        if conta is cliente.conta:
            print('checa_conta_cliente', True)
            return True
        print('checa_conta_cliente', False)
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        """Chama os métodos para autenticar os dados do cliente"""

        return self.checa_agencia(conta) and \
            self.checa_cliente(cliente) and \
            self.checa_conta(conta) and \
            self.checa_conta_cliente(cliente, conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':

    c1 = pessoas.Cliente('Luiz', 30)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Cliente('Maria', 18)
    cp1 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([112, 223, 222, 111])

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        print(c1.conta)
        print()
