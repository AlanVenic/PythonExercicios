#desenvolva um programa q leia comprimento de 3 retas e diga se elas podem formar um triangulo
r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r3 + r2 > r1):
    print('As retas em questão podem SIM formar um triângulo')
else:
    print('As retas em questão NÃO podem formar um triângulo')
