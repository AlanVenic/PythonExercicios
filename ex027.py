nome = str(input('Digite seu nome completo: ')).strip()
list = nome.split()
print('Seu primeiro e último nomes são respectivamente:', list[0], list[len(list)-1])