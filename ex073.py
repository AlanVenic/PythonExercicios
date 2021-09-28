#crie uma tupla preenchia com os 20 primeiros colocados da tabela do campeonato brasileiro
#na ordem de colocação. depois mostre: apenas os 5 primeiros; os 4 ultimos colocados;
#a lista de times em ordem alfabetica; em q posição na tabela esta o time são paulo

camp = ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino', 'Atlético-PR', 'Flamengo', 'Ceará', 'Bahia',
        'Fluminense', 'Santos', 'Atlético-GO', 'Corinthians', 'Internacional', 'Juventude', 'Cuiabá', 'São Paulo',
        'Sport Recife', 'América-MG', 'Grêmio', 'Chapecoense')
print('TOP 5 CAMPEONATO BRASILEIRO')
for p, t in enumerate(camp[0:5]):
        print(f'{p + 1}º: {t}')
print('ZONA DE REBAIXAMENTO')
for p, t in enumerate(camp[-4:]):
        print(f'{p + 17}º: {t}')
print('LISTA DE TIMES')
for times in sorted(camp):
        print(times)
esc = str(input('Você quer saber a posição de qual time? '))
posicao = camp.index(esc)
print(f'O {esc} está na {posicao + 1}ª posição no Campeonato')
