#faça um programa q tenha função chamada escreva() q receba qlqr texto com parametro
#e mostre uma msg com tamanho adaptavel

def escreva(txt):
    print('=' * len(txt))
    print(txt)
    print('=' * len(txt))


print('FORMATAÇÃO DE TEXTO')
esc = str(input('Digite um texto: ')).upper()
escreva(esc)
