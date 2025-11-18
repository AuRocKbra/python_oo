class Restaurante:
    restaurantes = []
    '''
        A função __init__ é o construtor da classe. Sendo obrigatório o uso da palavra reservada self ou this para referenciar que o construtor é da própria classe.
    '''
    def __init__(self,nome,categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    '''
        Rescritura do metodo str para retornar o nome do restaurante e a categoria
    '''
    def __str__(self):
        return f'{self._nome} - {self._categoria} - Ativo: {self._ativo}'

    '''
        Função de listagem de restaurantes
    '''
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | Ativo: {restaurante.ativo}')

    @property
    def ativo(self):
        return 'Sim' if self._ativo else 'Não'

    def alterar_status_restaurante(self):
        self._ativo = not self._ativo


restaurante_praca = Restaurante('Praça','Italiana')
restaurante_praca.alterar_status_restaurante()
restaurante_pizza = Restaurante('Pizza','Italiana')
Restaurante.listar_restaurantes()
