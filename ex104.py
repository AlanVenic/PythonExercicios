#crie um programa q tenha a função leiaInt(), q vai funcionar de forma semelhante a
#função input() do python. so q fazendo a validação para aceitar apenas um valor numerico.
#ex: n=leiaInt('Digite um n')

def leiaInt(txt):
    ok = False
    valor = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! O valor digitado não é um número inteiro.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
