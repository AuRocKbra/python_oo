class ClienteBanco:
    clientes_bancos = []
    def __init__(self, nome, cpf, telefone, email, apelido):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._email = email
        self._apelido = apelido
        ClienteBanco.clientes_bancos.append(self)

    @classmethod
    def listar_clientes(cls):
        for cliente in cls.clientes_bancos:
            print(f'Nome: {cliente._nome} - CPF: {cliente._cpf} - Telefone: {cliente._telefone} - Email: {cliente._email} - Apelido: {cliente._apelido}')

client1 = ClienteBanco('Goku','12345678911','(61) 99999-9999','goku@gmail.com','Kakaroto')
ClienteBanco.listar_clientes()