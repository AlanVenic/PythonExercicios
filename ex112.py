#dentro do pacote utilidadesCEV q criamos no ex111, temos um modulo chamado dados. crie uma função chamada
#leiaDinheiro() q seja capaz de funcionar como a função input(), mas com validação de dados para aceitar
#apenas valores q sejam monetários


from utilidadesCEV import dados
from utilidadesCEV import moeda

n = dados.leiaDinheiro('Digite um valor: ')
print(moeda.resumo(n, 0, moeda=True))