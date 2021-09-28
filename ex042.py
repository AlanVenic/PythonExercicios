r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))



if (r1 + r2 > r3) and (r1 + r3 > r2) and (r3 + r2 > r1):
    print('As retas em questão podem SIM formar um triângulo.')
    if r1 != r2 and r1 != r3 and r2 != r3:
        print('O triângulo em questão é Escaleno pois todos os lados são diferentes.')
    elif r1 == r2 == r3:
        print('O triângulo em questão é Equilátero, pois todos os seus lados são iguais.')
    else:
        print('O triângulo em questão é Isósceles, pois dois lados são iguais.')
else:
    print('As retas em questão NÃO podem formar um triângulo.')
