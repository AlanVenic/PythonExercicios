#escreva um programa para aprovar um emprestimo.
#o programa vai perguntar o valor da casa, o salario do comprador e o prazo em anos
#calcule o valor das prestações mensais sabendo que
#não pode exceder 30% do salário ou entao o emprestimo sera negativado

print('Bom dia a EMPRESTIMOS DO DIA agradece seu contato!')
print('Deseja fazer uma simulação de emprestimo para um imóvel?')
casa = int(input('Qual o valor do imóvel que você deseja comprar? '))
entrada = int(input('Qual valor da entrada? '))
salario = float(input('Qual o seu salário? '))
prazo = int(input('Em quantos anos você deseja quitar o imóvel? '))

meses = prazo*12
parcela = (casa - entrada)/meses

if parcela >= (salario*30)/100:
    print('Infelizmente seu crédito não foi aprovado, a parcela ficou '
          'no valor de R${:.2f}, o que corresponde a mais de 30% do seu salário'.format(parcela))
else:
    print('Seu crédito foi aprovado!')
    print('A parcela do seu imóvel ficou no valor de R${:.2f} no total de {} meses.'.format(parcela, meses))