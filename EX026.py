frase = str(input('Digite uma frase qualquer: ')).strip()
minu = frase.lower()
print('A letra A aparece na sua frase:', minu.count('a'))
print('A letra A aparece pela primeira vez na sua frase na posição:', minu.index('a')+1)
print('A letra A aparece na sua frase pela última vez na posição:', minu.rindex('a')+1)

