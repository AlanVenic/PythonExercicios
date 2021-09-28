#crie um programa onde o usuario digite uma expressão matematica qlqr que use parenteses. seu aplicativo
#deve analisar se a expressão está com os parenteses abertos e fechados na ordem correta


exp = str(input('Digite uma expressão matemática que possua parênteses: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')

#caracteres = list(exp)
#if '()' in caracteres:
#    print('Sua expressão está incorreta.')
#    caracteres.remove('(')
#elif '(' in caracteres[-1]:
#    print('Sua expressão está incorreta')
#elif ')' in caracteres[0]:
#    print('Sua expressão está incorreta')
#elif caracteres.count('(') != caracteres.count(')'):
#    print('Sua expressão está incorreta')
#else:
#    print(f'A expressão {exp} está correta')

