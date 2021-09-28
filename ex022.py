
frase = input('Digite seu nome completo: ')
print('Seu nome com todas as letras maiúsculas é:', frase.upper())
print('Seu nome com todas as letras minúsculas é:', frase.lower())
print('O número de letras que seu nome tem é:', len(frase) - frase.count(' '))
palavras = frase.split(' ')
print('O número de letras do seu primeiro nome é:', len(palavras[0]))

