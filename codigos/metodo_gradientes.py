#OTIMIZAÇÃO NÃO LINEAR - MÉTODOS DOS GRADIENTES
import sympy as sy
import solucao_grafica as sg 
import search_result as sr

sy.init_printing(use_latex='png', scale=1.05, order='grlex',forecolor='Black', backcolor='White', fontsize=10)

def gradiente(function, x, y, precision_decimals=4):

    alfa = sy.symbols("alfa")
    symbols = sy.symbols("x1 x2")
    expression = sy.parsing.sympy_parser.parse_expr(function)

    precision = 10**(-precision_decimals)

    k = 0
    pontos = []
    iteracoes = [0]
    lista_x = [x]
    lista_y = [y]
    loop = True
    converged = True
    points = [[x,y]]

    grad1 = sy.diff(expression, symbols[0])         #Gradiente da Função
    grad2 = sy.diff(expression, symbols[1])

    while loop == True:
        
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

        except:                             #Critério de Parada 1
            grad1 = grad1.subs(symbols[0], x)
            grad1 = grad1.subs(symbols[1], y)
        
            grad2 = grad2.subs(symbols[1], y)
            grad2 = grad2.subs(symbols[0], x)
            
            if grad1 == 0 and grad2 == 0:                  
                    k=k+1
                    print("Gradiente: Zero")

                    lista_x.append(x)
                    lista_y.append(y)
                    pontos = sg.function(expression, symbols, lista_x, lista_y)
                    iteracoes.append(k)
                    break
    
        #Substitui o valor da raiz de alfa na expressão de alfa
        x = round(y1.subs(alfa, raiz), precision_decimals)         #Atualiza os valores de x e y
        y = round(y2.subs(alfa, raiz), precision_decimals)

        points.append([x,y])
        k = k + 1 
        iteracoes.append(k)
          
        lista_x.append(x)
        lista_y.append(y)
        pontos = sg.function(expression, symbols, lista_x, lista_y)

        if k >= 5:                                      #Critério de Parada 2         
            fmax = max(pontos[k-5:])
            fmin = min(pontos[k-5:])

            if abs(fmax - fmin) < precision:
                loop = False

        if k>= 100:                                     #Critério de Parada 3
            print("Não Convergiu")
            converged = False
            loop = False    

    sg.graphic_solution(expression, symbols, lista_x, lista_y, pontos, iteracoes)

    return sr.SearchResult(function, points, converged, precision_decimals)

result = gradiente("0.26*(x1**2 + x2**2) - 0.48*x1*x2", 4, 4, 4)
print(result)