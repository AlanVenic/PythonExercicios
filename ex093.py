#crie um programa q gerencie o aproveitamento de um jogador de futebol. o programa vai ler o nome e
#qnts partidas ele jogou. depois vai ler qnts gols ele fez em cada partida. no final, td isso sera
#guardado em um dicionario, incluindo o total de gols feitos durante o campeonato.

jogador = {}
jogos = []
print('RENDIMENTO DE JOGADORES')
jogador['nome'] = str(input('Digite o nome: '))
tot = int(input('Quantas partidas foram jogadas: '))
for p in range(0, tot):
    jogos.append(int(input(f'Número de gols na {p+1}ª partida: ')))
jogador['gols'] = jogos[:]
jogador['total'] = sum(jogos)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'Na {i+1}ª partida, fez {v} gols')
print(f'Fez um total de {jogador["total"]} gols')
