#faça um mini-sistema q utilize o InteractiveHelp do python. o usuario vai digiitar o comando
#e o manual vai aparecer. qnd o usuario digitar a palavra 'Fim', o programa sera encerrado.
# obs: use cores

def ajuda(txt):
    help(txt)


def titulo(msg, cor):
    tam = len(msg)
    print('=' * tam)
    print(msg)
    print('=' * tam)

info = ''
while True:
    info = str(input('Deseja ver o manual de qual comando do Python? [fim para encerrar] ')).lower()
    if info == 'fim':
        break
    else:
        ajuda(info)