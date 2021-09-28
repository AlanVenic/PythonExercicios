def leiaDinheiro(txt):
    ok = False
    valor = 0
    while not ok:
        n = str(input(txt)).replace('R$', '').replace(',', '.').strip()
        if n.isalpha() or n == '':
            print('\033[0;31mErro! Valor inválido.\033[m')
        else:
            ok = True
            return float(n)


def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mO valor digitado é inválido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mNão foi digitado nenhum valor\033[m.')
            return 0
        else:
            return n


def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('\033[31mO valor digitado é inválido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mNão foi digitado nenhum valor\033[m.')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam


def head(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    head('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc


def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        head('PESSOAS CADASTRADAS')
        for linha in a:
            d = linha.split(';')
            d[1] = d[1].replace('\n', '')
            print(f'{d[0]:<30}{d[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na inserção de dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()





