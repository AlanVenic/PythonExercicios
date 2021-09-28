#aprimore o desafio 093 para q ele funcione com varios jogadores, incluindo um sistema
#de visualização de detalhes do aproveitamento de cada jogador

time = []
jogador = {}
jogos = []
print('RENDIMENTO DE JOGADORES')
while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome: '))
    tot = int(input('Quantas partidas foram jogadas: '))
    jogos.clear()
    for p in range(0, tot):
        jogos.append(int(input(f'Número de gols na {p+1}ª partida: ')))
    jogador['gols'] = jogos[:]
    jogador['total'] = sum(jogos)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Opção inválida! Digite S ou N')
    if resp == 'N':
        break
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'Na {i+1}ª partida, fez {v} gols')
print(f'Fez um total de {jogador["total"]} gols')
while True:
    busca = int(input('Mostrar estatísticas de qual jogador? [999 para]'))
    if busca == 999:
        break
    if busca >= len(time):
        print('Código inválido!')
    else:
        print(f'Estatísticas do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols')