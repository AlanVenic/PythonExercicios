#crie um programa q leia o nome e preço de varios produtos. o programa deve
#perguntar ao usuario se quer continuar. no final mostre:
#qual o total gasto nas compras; qnts produtos custam mais de 1000; qual nome do produto mais barato

print('CARRINHO DE COMPRAS')
n = soma = caro = barato = 0
nomebarato = ''
while True:
    n += 1
    print(f'Adicionando {n}º produto ao carrinho')
    nome = str(input('Nome: '))
    preço = float(input('Preço: '))
    print('Produto adicionado com sucesso.')
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    soma += preço
    if n == 1 or preço < barato:
        barato = preço
        nomebarato = nome
    if preço >= 1000:
        caro += 1
    while cont not in 'SN':
        print('Opção inválida.')
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print('COMPRAS FINALIZADAS.')
print(f'''O total das compras foi R${soma:.2f}.
Dos produtos adicionados ao carrinho, {caro} custam mais de R$1.000,00.
O produto mais barato comprado foi {nomebarato} que custa R${barato:.2f}.''')
