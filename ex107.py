#crie um modulo chamado moeda.py q tenha funcoes incorporadas aumentar(), diminuir(), dobro() e metade().
#faça tb um progrma q importe esse modulo e use algumas dessas funções

from utilidadesCEV import moeda

print(f' o dobro de 140 é {moeda.dobro(140)}, '
      f'a metade de 45 é {moeda.metade(45)}, '
      f'560 mais 34% é {moeda.aumentar(560, 34)}, '
      f'675 menos 22% é {moeda.diminuir(675, 22)}')
