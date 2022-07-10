#OTIMIZAÇÃO NÃO LINEAR - MÉTODOS DOS GRADIENTES
import sympy as sy
import solucao_grafica as sg 

sy.init_printing(use_latex='png', scale=1.05, order='grlex',forecolor='Black', backcolor='White', fontsize=10)

def main():

    #Condições Iniciais
    x = 4
    y = 4

    alfa = sy.Symbols("alfa")
    
    symbols = sy.symbols("x1 x2")
    funcao = "(((x1 - 3)**2)/4 + ((x2 - 2)**2)/9) + 13"
    expression = sy.parsing.sympy_parser.parse_expr(funcao)

    controlex = 1
    controley = 1
    k = 0
    pontos = []
    iteracoes = []
    lista_x = []
    lista_y = []

    grad1 = sy.diff(expression, symbols[0])         #Gradiente da Função
    grad2 = sy.diff(expression, symbols[1])

    #Critério de Parada - Se a variação dos ponto X for maior que 0,001
    while (abs(controlex) > 0.001) or (abs(controley) > 0.001):
        
        a = grad1.subs(symbols[0], x)               #Valor de X no gradiente
        a2 = a.subs(symbols[1], y)

        b = grad2.subs(symbols[0], x)               #Valor de Y no gradiente
        b2 = b.subs(symbols[1], y)
    
        y1 = (x - alfa*a2)                  #Expressão do alfa
        y2 = (y - alfa*b2)

        funcao1 = expression.subs(symbols[0], y1)       #Substituição de de y1 e y2 na função 
        funcao2 = funcao1.subs(symbols[1], y2)
        
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
        
        x = resultado1                      #Atualiza os valores de x e y
        y = resultado2

        iteracoes.append(k)
        k = k + 1 

        pontos.append(sg.funcao(expression, symbols, x, y))
        lista_x.append(x)
        lista_y.append(y)
    
    pontos = sg.funcao(expression, symbols, lista_x, lista_y)
        
      
    sg.plot_convergencia(iteracoes, pontos)
    sg.plot_curvasniveis(expression, symbols, lista_x, lista_y)
    sg.grafico_3d(expression, symbols)
    sg.deslocamento_3d(expression, symbols, lista_x, lista_y)

    
main()