#faça um programa q tenha uma função chamada ficha() q receba 2 parametros opcionais:
#o nome de um jogador e qnt gols ele fez. o programa deve ser capaz de mostrar a ficha do jogador
#msm q algum dado não tenha sido informado corretamente.

def ficha(j='Desconhecido', g=0):
    if g == 1:
        print(f'O jogador {j} fez {g} gol no campeonato.')
    else:
        print(f'O jogador {j} fez {g} gols no campeonato.')


print('CADASTRO DE JOGADORES')
nome = str(input('Qual o nome do jogador: '))
gol = str(input(f'Quantos gols {nome} fez: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(g=gol)
else:
    ficha(nome, gol)

