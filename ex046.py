#faça um programa q mostre na tela uma contagem regressiva pra um estouro de fogos
# indo de 10 ate 0, com uma pausa de 1s entre elas

from time import sleep

print('Vai começar a contagem regressiva!')
sleep(1)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('Feliz ano novo!')
