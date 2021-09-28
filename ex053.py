#crie um programa q leia uma frase e diga se ela é um
# palindromo (msm leitura de tras pra frente) desconsiderando espaços


print('Será que sua frase é um palíndromo?')
frase = str(input('Digite uma frase: ')).strip().upper()
junto = frase.replace(" ", "")
print('Sua frase escrita ao contrário fica {}'.format(junto[::-1]))
if junto == junto[::-1]:
    print('Esta frase é um palíndromo.')
else:
    print('Esta frase não é um palíndromo.')
