#crie um programa q leia varioa numeros inteiros. o programa so vai parar
#qnd o usuario digitar 999, q é a condição. no final, mostre qnts numeros foram digitados
#e a soma entre eles

print('PARA COM 999')
s = c = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram digitados {c} números e a soma deles é {s}.')
