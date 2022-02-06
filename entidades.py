from datetime import datetime

"""
    Python 3.10
    Classes para simular as funções deselvolvidas pelas entidades
"""


class Uespi:

    """
    - Nomes e matrículas fictícios. (nomes: https://gerador-nomes.herokuapp.com/)
    """

    alunos = [
        {
            'nome': 'Nataniel Fernandes Lins',
            'matricula': 1,
            'bloco': 3,
            'ativo': True
        },
        {
            'nome': 'Ayumi Ribeiro Tedim',
            'matricula': 2,
            'bloco': 8,
            'ativo': True
        },
        {
            'nome': 'Lucas Félix Marçal',
            'matricula': 3,
            'bloco': 4,
            'ativo': True
        },
        {
            'nome': 'Suzana Rocha Cedro',
            'matricula': 4,
            'bloco': 1,
            'ativo': True
        },
        {
            'nome': 'Célio Belo Paiva',
            'matricula': 5,
            'bloco': 7,
            'ativo': True
        },
        {
            'nome': 'Noa Grande Pederneiras',
            'matricula': 6,
            'bloco': 10,
            'ativo': True
        },
        {
            'nome': 'Erik Rosado Bonito',
            'matricula': 7,
            'bloco': 2,
            'ativo': False
        },
        {
            'nome': 'Aarnav Santos Abreu',
            'matricula': 8,
            'bloco': 6,
            'ativo': True
        },
        {
            'nome': 'Jacinta Severiano Albernaz',
            'matricula': 9,
            'bloco': 8,
            'ativo': False
        },
        {
            'nome': 'Bryan Galvão Mantas',
            'matricula': 10,
            'bloco': 5,
            'ativo': True
        },
    ]

    def emitir_declaracao(self, matricula):

        for aluno in self.alunos:
            if aluno['matricula'] == matricula:
                return aluno
        return None


class Dce:
    """
    - Simulação das validações realizadas para a emissão de uma carteira estudantil
    """

    carteira_estudantil = {}

    def emitir_carteira_estudantil(self, declaracao):

        if declaracao['ativo']:
            self.carteira_estudantil['nome'] = declaracao['nome']
            self.carteira_estudantil['matricula'] = declaracao['matricula']
            self.carteira_estudantil['validade'] = datetime.now()\
                .replace(year=datetime.now().year + 1)\
                .strftime('%d/%m/%Y')
            self.carteira_estudantil['emissao'] = datetime.now().strftime('%d/%m/%Y')
            self.carteira_estudantil['instituicao'] = 'Universidade Estadual do Piauí'

            return self.carteira_estudantil

        return None


class Setut:
    """
    Simulação das validações realizadas para a emissão de uma carteira estudantil de transporte
    """

    carteira_transporte = {}

    def emitir_carteira_transporte(self, carteira_estudantil):

        if carteira_estudantil:

            validade = datetime.strptime(carteira_estudantil['validade'], '%d/%m/%Y')

            if validade >= datetime.now():
                self.carteira_transporte['nome'] = carteira_estudantil['nome']
                self.carteira_transporte['validade'] = datetime.now()\
                    .replace(month=datetime.now().month + 6)\
                    .strftime('%d/%m/%Y')
                self.carteira_transporte['emissao'] = datetime.now().strftime('%d/%m/%Y')
                self.carteira_transporte['bloqueado'] = False

                return self.carteira_transporte

            return None
