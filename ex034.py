#escreva um programa que pergunte o salario de um funcionario
#e calcule o valor do seu aumento. para salarios superiores a 1250,
#o aumento é 10%. para inferiores ou iguais, o aumento é 15%
sal = int(input('Digite seu salário para saber quanto você teve de aumento: '))
if sal <= 1250:
    print('Você recebeu um aumento de 15% e seu novo salário é de R${:.2f}'.format(sal * 1.15))
else:
    print('Você recebeu um aumento de 10% e seu novo salário é de R${:.2f}'.format((sal * 1.1)))
