#OTIMIZAÇÃO NÃO LINEAR - MÉTODOS DE NEWTON
import sympy as sy
from numpy import *
import numpy as np
from numpy.linalg import inv

def main(): 
  
    sy.init_printing()

    #Condições Iniciais
    x = 3/4
    y = 1/4

    x1 = sy.Symbol('x1')
    x2 = sy.Symbol('x2')

    funcao = ((x1 - 3)**2 + (x2 - 2)**2)

    resultado1 = 0
    resultado2 = 0
    controlex = 1
    controley = 1
    i = 0

    #while (abs(controlex) > 0.000001) or (abs(controlex) > 0.000001):
    while i < 5:

        print('\nINTERAÇÃO ',i+1," :")

        grad1 = sy.diff(funcao, x1)         #Gradiente da Função
        grad2 = sy.diff(funcao, x2)
        
        a = grad1.subs(x1, x)               #Valor de X no gradiente
        a2 = a.subs(x2, y)

        b = grad2.subs(x1, x)               #Valor de Y no gradiente
        b2 = b.subs(x2, y)

        h11 = int(sy.diff(grad1, x1))
        h12 = int(sy.diff(grad1, x2))
        h21 = int(sy.diff(grad2, x1))
        h22 = int(sy.diff(grad2, x2))

        P = np.array([[x], [y]])
        H = np.array([[h11, h12], [h21, h22]])
        G = np.array([[a2], [b2]])

        H_inv = inv(H)
       
        x0 = P - np.dot(H_inv, G)

        resultado1 = x0[0][0]
        resultado2 = x0[1][0]

        print('\nResultado:', int(resultado1),'\n          ', int(resultado2))

        controlex = resultado1 - x          #Calcula a variação dos valores dos pontos encontrados
        controley = resultado2 - y
        
        i = i + 1                            #Atualiza os valores de x e y
        x = resultado1
        y = resultado2

main()