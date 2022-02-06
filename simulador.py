from entidades import *
from random import randint


"""
    Python 3.10
    
    Tempos de espera simulados com tendência 'aproximada' de uma experiência real.
    Unidade de tempo: HORAS
    
    - A declaração na uespi pode ser obtida pelo AlunoOnline, 
        então foi considerado como tempo aleatório um valor entre 0 e 1
    
    - A carteira de estudante é obtida com duração média entre 5 e 20 dias, 
        então foi considerado como tempo aleatório um valor entre 5 e 20 (em horas: 120 a 480).
        
    - A carteira de transporte é obtida com duração média entre 1 e 4 horas,
        então foi considerado como tempo aleatório um valor entre 1 e 4
"""


# Instanciando objetos
uespi = Uespi()
dce = Dce()
setut = Setut()


# Retorna um valor aleatório de um intervalo
def sorteia_valor_range(inicio, fim):
    return randint(inicio, fim)


matricula = sorteia_valor_range(1, 10)

# Emitir declaração da UESPI
tempo_espera_uespi = sorteia_valor_range(0, 1)
declaracao_uespi = uespi.emitir_declaracao(matricula)

# Emitir carteira estudantil
tempo_espera_dce = sorteia_valor_range(120, 480)
carteira_estudantil = dce.emitir_carteira_estudantil(declaracao_uespi)

# Emitir carteira de transporte público
tempo_espera_setut = sorteia_valor_range(1, 4)
carteira_transporte = setut.emitir_carteira_transporte(carteira_estudantil)

print('*********************\n'
      '** Relatório final **\n'
      '*********************\n')

print(f'Declaração: {declaracao_uespi}')
print(f'Carteira Estudantil: {carteira_estudantil}')
print(f'Carteira de Transporte: {carteira_transporte}\n')

print('\nTempo de Espera em cada entidade envolvida.\n')
print(f'UESPI: {tempo_espera_uespi} hrs')
print(f'DCE: {tempo_espera_dce} hrs')
print(f'SETUT: {tempo_espera_setut} hrs')

espera_total = tempo_espera_uespi + tempo_espera_dce + tempo_espera_setut
print(f'Espera total: {espera_total // 24} dias e {espera_total % 24} hrs')
