#OTIMIZAÇÃO NÃO LINEAR - MÉTODOS DOS GRADIENTES
import sympy as sy
import solucao_grafica as sg 

sy.init_printing(use_latex='png', scale=1.05, order='grlex',forecolor='Black', backcolor='White', fontsize=10)

def gradiente(entrada_funcao, x, y, precisao=0.001):

    alfa = sy.symbols("alfa")
    
    symbols = sy.symbols("x1 x2")
    expression = sy.parsing.sympy_parser.parse_expr(entrada_funcao)

    k = 0
    pontos = []
    iteracoes = []
    lista_x = []
    lista_y = []
    laco = True


    grad1 = sy.diff(expression, symbols[0])         #Gradiente da Função
    grad2 = sy.diff(expression, symbols[1])

    #Critério de Parada - Se a variação dos ponto X for maior que 0,001
    while laco == True:
        
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
                    print('ITERAÇÃO',k,":")
                    print('Ponto X1:',x,'\nPonto X2:',y,'\n')
                    lista_x.append(x)
                    lista_y.append(y)
                    iteracoes.append(k)
                    break
    
        resultado1 = y1.subs(alfa, raiz)    #Substitui o valor da raiz de alfa na expressão de alfa
        resultado2 = y2.subs(alfa, raiz)
        
        x = round(resultado1,4)                      #Atualiza os valores de x e y
        y = round(resultado2,4)
        
        k = k + 1 
        iteracoes.append(k)
          
        lista_x.append(x)
        lista_y.append(y)
        pontos = sg.funcao(expression, symbols, lista_x, lista_y)

        print('\nITERAÇÃO ',k," :")
        print('Ponto X1:',float((resultado1)),'\nPonto X2:',float(resultado2))

        if k >= 5:                                      #Critério de Parada 2
         
            fmax = max(pontos[k-5:])
            fmin = min(pontos[k-5:])

            if abs(fmax - fmin) < precisao:
                laco = False
        
      
    sg.plot_convergencia(iteracoes, pontos)
    sg.plot_curvasniveis(expression, symbols, lista_x, lista_y)
    sg.grafico_3d1(expression, symbols, lista_x, lista_y, pontos)
    sg.deslocamento_3d(expression, symbols, lista_x, lista_y)



gradiente("(((x1 - 3)**2)/4 + ((x2 - 2)**2)/9)+13", 4, 4, 0.001)