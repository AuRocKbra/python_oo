from modelos.Avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    '''
        A função __init__ é o construtor da classe. Sendo obrigatório o uso da palavra reservada self ou this para referenciar que o construtor é da própria classe.
    '''
    def __init__(self,nome,categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacoes = []
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
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.resultado_avaliacoes).ljust(25)} | Ativo: {restaurante.ativo} ')

    @property
    def ativo(self):
        return 'Sim' if self._ativo else 'Não'

    def alterar_status_restaurante(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, nome, nota):
        nota_ajustada = 5 if nota > 5 else 0 if nota < 0 else nota
        avaliacao = Avaliacao(nome, nota_ajustada)
        self._avaliacoes.append(avaliacao)

    """
    Função que calcula a média das notas dos restaurantes. 
    A função é marcada como propriedade da classe Restaurante, para permitir que seja acessada pela instancia da classe como um atributo.
    """
    @property
    def resultado_avaliacoes(self):
        if not self._avaliacoes:
            return '-'
        return round(sum(avalicao._nota for avalicao in self._avaliacoes) / len(self._avaliacoes),1)