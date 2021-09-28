def aumentar(n, p, moeda=False):
    a = n + (n * (p/100))
    if moeda == True:
        return (f'R${a:.2f}'.replace('.', ','))
    else:
        return a


def diminuir(n, p, moeda=False):
    d = n - (n * (p/100))
    if moeda == True:
        return (f'R${d:.2f}'.replace('.', ','))
    else:
        return d


def dobro(n, moeda=False):
    d = n * 2
    if moeda == True:
        return (f'R${d:.2f}'.replace('.', ','))
    else:
        return d


def metade(n, moeda=False):
    m = n / 2
    if moeda == True:
        return (f'R${m:.2f}'.replace('.', ','))
    else:
        return m


def moeda(n):
    return (f'R${n:.2f}'.replace('.', ','))


def resumo(n, p, moeda=False):
    a = aumentar(n, p)
    b = diminuir(n, p)
    c = dobro(n)
    d = metade(n)
    if moeda == True:
        return (f'R${n:.2f} + {p}% = R${a:.2f}\n'
                f'R${n:.2f} - {p}% = R${b:.2f}\n'
                f'R${n:.2f} x 2 = R${c:.2f}\n'
                f'R${n:.2f} / 2 = R${d:.2f}'.replace('.', ','))
    else:
        return (f'{n} + {p}% = {a}\n'
                f'{n} - {p}% = {b}\n'
                f'{n} x 2 = {c}\n'
                f'{n} / 2 = {d}')


