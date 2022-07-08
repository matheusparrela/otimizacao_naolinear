#OTIMIZAÇÃO NÃO LINEAR - MÉTODOS DOS GRADIENTES
import sympy as sy
import matplotlib.pyplot as mp
import numpy as np
import solucao_grafica as sg 

sy.init_printing(use_latex='png', scale=1.05, order='grlex',forecolor='Black', backcolor='White', fontsize=10)

def main():

    #Condições Iniciais
    x = 4
    y = 4

    x1 = sy.Symbol('x1')
    x2 = sy.Symbol('x2')
    alfa = sy.Symbol('alfa')

    funcao = (((x1 - 3)**2)/4 + ((x2 - 2)**2)/9) + 13

    controlex = 1
    controley = 1
    k = 0
    pontos = []
    iteracoes = []
    lista_x = []
    lista_y = []

    grad1 = sy.diff(funcao, x1)         #Gradiente da Função
    grad2 = sy.diff(funcao, x2)

    #Critério de Parada - Se a variação dos ponto X for maior que 0,001
    while (abs(controlex) > 0.001) or (abs(controley) > 0.001):
        
        k = k + 1 
        
        a = grad1.subs(x1, x)               #Valor de X no gradiente
        a2 = a.subs(x2, y)

        b = grad2.subs(x1, x)               #Valor de Y no gradiente
        b2 = b.subs(x2, y)
    
        y1 = (x - alfa*a2)                  #Expressão do alfa
        y2 = (y - alfa*b2)

        funcao1 = funcao.subs(x1, y1)       #Substituição de de y1 e y2 na função 
        funcao2 = funcao1.subs(x2, y2)
        
        d1 = sy.diff(funcao2, alfa)         #Derivada da função em relação a alfa

        raiz = (sy.solve(d1))               #Raiz da derivada da função
    
        try:               
            raiz = raiz[0]

        except:
            exit()
    
        resultado1 = y1.subs(alfa, raiz)    #Substitui o valor da raiz de alfa na expressão de alfa
        resultado2 = y2.subs(alfa, raiz)

        print('\nITERAÇÃO ',k," :")
        print('Ponto X1:',float((resultado1)),'\nPonto X2:',float(resultado2))
    
        controlex = resultado1 - x          #Calcula a variação dos valores dos pontos encontrados
        controley = resultado2 - y

        iteracoes.append(k)
        pontos.append(sg.funtion(x, y))
        lista_x.append(x)
        lista_y.append(y)
        
        x = resultado1                      #Atualiza os valores de x e y
        y = resultado2

    sg.plot_convergencia(iteracoes, pontos)
    sg.plot_curvasniveis(lista_x, lista_y) 
  

    
main()
