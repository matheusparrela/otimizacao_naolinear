#OTIMIZAÇÃO NÃO LINEAR - MÉTODOS DE NEWTON MODIFICADO   
import sympy as sy
import solucao_grafica as sg

def main(): 
  
    sy.init_printing(use_latex='png', scale=1.05, order='grlex',forecolor='Black', backcolor='White', fontsize=10)

    #Condições Iniciais
    x = 0.25
    y = -0.8

    precisao = 0.001

    alfa = sy.symbols("alfa")

    symbols = sy.symbols("x1 x2")
    entrada_funcao = "2*x1**2 - 1.05*x1**4 + ((x1**6)/6) +  x1*x2 + x2**2"
    entrada_funcao = "(4 - 2.1*x1**2 + (x1**4)/3)*x1**2 + x1*x2 + (-4 +4*x2**2)*x2**2"
    expression = sy.parsing.sympy_parser.parse_expr(entrada_funcao)
        
    
    resultado1 = 0
    resultado2 = 0
    k = 0
    laco = True
    pontos = []
    iteracoes = []
    lista_x = []
    lista_y = []

    grad1 = sy.diff(expression, symbols[0])         #Gradiente da Função
    grad2 = sy.diff(expression, symbols[1])

    h11 = sy.diff(grad1, symbols[0])            #Calcula os elementos da hessiana
    h12 = sy.diff(grad1, symbols[1])
    h21 = sy.diff(grad2, symbols[0])
    h22 = sy.diff(grad2, symbols[1])

    #Passa as condições iniciais, elementos da hessiana e o gradiente no pontos iniciais para matrizes

    hessiana = sy.Matrix([[h11, h12],[h21, h22]]) 

    gradiente = sy.Matrix([[grad1], [grad2]])

    try:
        inv_hessiana = -hessiana.inv()       #Inverte a matriz hessiana
        prod = inv_hessiana*gradiente
        

    except:
        print("Hessiana não Inversível")
        laco = False
         

    while laco == True:
        

        prod1 = prod.subs(symbols[0], x)
        prod2 = prod1.subs(symbols[1], y)

        y1 = (x + alfa*prod2[0,0])
        y2 = (y + alfa*prod2[1,0])

        funcao1 = expression.subs(symbols[0], y1)       #Substituição de de y1 e y2 na função 
        funcao2 = funcao1.subs(symbols[1], y2)
       
        d1 = sy.diff(funcao2, alfa)                     #Derivada da função em relação a alfa

        raiz = (sy.solve(d1))
       
        try: 
            raiz = raiz[0]

        except:                             #Critério de Parada 1

            grad1 = grad1.subs(symbols[0], x)
            grad1 = grad1.subs(symbols[1], y)
        
            grad2 = grad2.subs(symbols[1], y)
            grad2 = grad2.subs(symbols[0], x)
            
            if grad1 == 0 and grad2 == 0:
                    k = k+1
                    print("Gradiente: Zero")
                    print('ITERAÇÃO',k,":")
                    print('Ponto X1:',x,'\nPonto X2:',y,'\n')
                    lista_x.append(x)
                    lista_y.append(y)
                    iteracoes.append(k)
                    k = 5
                    break
        
        
        resultado1 = y1.subs(alfa, raiz)                #Substitui o valor da raiz de alfa na expressão de alfa
        resultado2 = y2.subs(alfa, raiz)
        
                         
        x = round(resultado1,4)                         #Atualiza os valores de x e y
        y = round(resultado2,4)  
        
        lista_x.append(x)
        lista_y.append(y)
        pontos = sg.funcao(expression, symbols, lista_x, lista_y)
        
        k = k + 1
        iteracoes.append(k)
        

        print('\nITERAÇÃO',k,":")
        print('Ponto X1:',x,'\nPonto X2:',y)

        
        if k >= 5:                                      #Critério de Parada 2
         
            fmax = max(pontos[k-5:])
            fmin = min(pontos[k-5:])

            if abs(fmax - fmin) < precisao:
                laco = False


    pontos = sg.funcao(expression, symbols, lista_x, lista_y)
    
    if k > 4:
        #Plote dos Gráficos
        sg.plot_convergencia(iteracoes, pontos)
        sg.plot_curvasniveis(expression, symbols, lista_x, lista_y)
        sg.grafico_3d1(expression, symbols, lista_x, lista_y, pontos)
        sg.grafico_3d(expression, symbols)
        #sg.deslocamento_3d(expression, symbols, lista_x, lista_y)


main()