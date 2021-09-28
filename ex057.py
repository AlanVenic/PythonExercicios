#faça um programa q leia o sexo de uma pessoa, mas so aceite
#valores M ou F. caso esteja errado, peça q digite o valor correto

sexo = str(input('Informe seu sexo? [F/M] ')).upper().strip()[0]
while sexo not in 'FM':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo? [F/M] ')).upper().strip()[0]
print('Foi registrado seu sexo {} no banco de dados.'.format(sexo))


