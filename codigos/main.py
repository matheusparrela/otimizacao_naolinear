#OTIMIZAÇÃO NÃO LINEAR - MÉTODOS DOS GRADIENTES

from symtable import Symbol
import sympy as sy
import numpy as ny

pontos_ini = [1/3, 5/2]


x1 = sy.Symbol('x1')
x2 = sy.Symbol('x2')

grad1 = sy.diff(((x1 + 2*x2 - 7)**2 + (2*x1 + x2 - 5)**2), x1)
grad2 = sy.diff(((x1 + 2*x2 - 7)**2 + (2*x1 + x2 - 5)**2), x2)

print(grad1)
print(grad2)