from abc import ABC, abstractmethod


class Conta(ABC):
    """Classe abstrata para as subclasses"""

    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        """Inicializando os atributos"""

        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float: ...
    """Método abstrato para sacar da conta"""

    def depositar(self, valor: float) -> float:
        """Depositar valor na conta"""

        self.saldo += valor
        self.detalhes(f'DEPÓSITO: {valor}')
        return self.saldo

    def detalhes(self, msg='') -> None:
        """Imprime na tela uma mensagem"""

        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('-' * 35)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    """SubClasse conta Poupança"""

    def sacar(self, valor: float) -> float:
        """Método para sacar da conta"""

        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE: {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado!')
        self.detalhes(f'(SAQUE NEGADO: {valor})')
        return self.saldo


class ContaCorrente(Conta):
    """SubClasse conta Corrente"""

    def __init__(self, agencia: int, conta: int,
                 saldo: float = 0, limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        """Método para sacar da conta"""

        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE: {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado!')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO: {valor})')
        return self.saldo

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, '\
            f'{self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222, )
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    print('*' * 35)
    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(98)
    cc1.sacar(1)
