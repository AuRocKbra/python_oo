class ContaBancaria:
    def __init__(self,titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Titular: {self._titular} - Saldo: {self._saldo} - Ativo: {self._ativo}'

    def ativar_conta(self):
        self._ativo = True

conta1 = ContaBancaria("Augusto", 100)
conta2 = ContaBancaria("Maria", 200)
print(conta1)
print(conta2)
conta1.ativar_conta()
print(conta1)
