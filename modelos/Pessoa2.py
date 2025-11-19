class Pessoa:
    def __init__(self, nome, idade,profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self._saudacao = f'Olá {self.profissao}'

    def __str__(self):
        return f'{self.nome} - {self.idade} - {self.profissao}'

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        return self._saudacao

pessoa1 = Pessoa("Augusto", 20,"Programador")
pessoa2 = Pessoa("Maria", 25,"Programadora")
print(pessoa1)
print(pessoa2)
pessoa1.aniversario()
print(pessoa1)
print(pessoa2.saudacao)
