#faça um programa q tenha função notas() q pode receber varias notas de aluno e vai retornar
#um dicionario com as informações: qnt de notas; maior nota; menor nota; media da turma; situação(opcional)
#adicione tb as docstrings da função


def notas(*num, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos.
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r={}
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['média'] = sum(num)/len(num)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(6, 4.5, 7, 2, 1, sit=True)
print(resp)
help(notas)