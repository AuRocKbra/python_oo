from modelos.Restaurante import Restaurante #Forma de importação de uma class
"""
Declaração dos objetos
"""
restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_praca.receber_avaliacao('Luiz', 5.0)
restaurante_praca.receber_avaliacao('Maria', 4.0)
restaurante_praca.receber_avaliacao('Alice',10)

"""
Arquivo principal do projeto
"""
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()