#faça um programa q tenha uma função chamada area(), q receba dimensoes de um
#terreno retangular (largura e comprimento) e mostre a area do terreno

def area(l, c):
    a = l * c
    print(f'A área do terreno é {a:.2f}m²')


print('ÁREA DO TERRENO')
larg = float(input('Digite a largura (m): '))
comp = float(input('Digite o comprimento (m): '))
area(larg, comp)
