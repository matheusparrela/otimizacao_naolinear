#OTIMIZAÇÃO NÃO LINEAR - MÉTODO DE NEWTON MODIFICADO   
import sympy as sy
import solucao_grafica as sg
import search_result as sr

def modificado(function, x, y, precision_decimals=4): 
  
    sy.init_printing(use_latex='png', scale=1.05, order='grlex',forecolor='Black', backcolor='White', fontsize=10)

    points = [[x,y]]
    converged = True
    precision = 10**(-precision_decimals)
    k = 0
    loop = True
    iterations = [k]

    alfa = sy.symbols("alfa")
    symbols = sy.symbols("x1 x2")
    
    try:    
        expression = sy.parsing.sympy_parser.parse_expr(function)
    
    except:
        print("Erro na função")
        return 1
        
    grad1 = sy.diff(expression, symbols[0])         #Gradiente da Função
    grad2 = sy.diff(expression, symbols[1])

    h11 = sy.diff(grad1, symbols[0])                #Calcula os elementos da hessiana
    h12 = sy.diff(grad1, symbols[1])
    h21 = sy.diff(grad2, symbols[0])
    h22 = sy.diff(grad2, symbols[1])

    #Passa as condições iniciais, elementos da hessiana e o gradiente no pontos iniciais para matrizes
    hessiana = sy.Matrix([[h11, h12],[h21, h22]]) 
    gradiente = sy.Matrix([[grad1], [grad2]])

    try:
        inv_hessiana = -hessiana.inv()              #Inverte a matriz hessiana
        prod = inv_hessiana*gradiente
        
    except:
        print("Hessiana não Inversível")
        converged = False
        loop = False
         
    while loop == True:
        
        prod1 = prod.subs(symbols[0], x)
        prod2 = prod1.subs(symbols[1], y)

        y1 = (x + alfa*prod2[0,0])
        y2 = (y + alfa*prod2[1,0])

        funcao1 = expression.subs(symbols[0], y1)           #Substituição de de y1 e y2 na função 
        funcao2 = funcao1.subs(symbols[1], y2)
       
        df_dalfa = sy.diff(funcao2, alfa)                   #Derivada da função em relação a alfa
        raiz = (sy.solve(df_dalfa))
       
        try: 
            raiz = raiz[0]

        except:                                             #Critério de Parada 1
            grad1 = grad1.subs(symbols[0], x)
            grad1 = grad1.subs(symbols[1], y)
        
            grad2 = grad2.subs(symbols[1], y)
            grad2 = grad2.subs(symbols[0], x)
            
            if grad1 == 0 and grad2 == 0:
                    k = k+1
                    print("Gradiente: Zero")
                    points.append[x , y]
                    image_z = sg.function(expression, symbols, points)
                    iterations.append(k)
                    k = 5
                    break
               
        x = round(y1.subs(alfa, raiz), precision_decimals)                #Substitui o valor da raiz de alfa na expressão de alfa
        y = round(y2.subs(alfa, raiz), precision_decimals)
        
        points.append([x,y])
        image_z = sg.function(expression, symbols, points)
        k = k + 1
        iterations.append(k)
        
        if k >= 5:                                                        #Critério de Parada 2
            fmax = max(image_z[k-5:])
            fmin = min(image_z[k-5:])

            if abs(fmax - fmin) < precision:
                loop = False

        if k>= 100:                                                       #Critério de Parada 3
            print("Não Convergiu")
            converged = False
            loop = False

    #if k > 4:
        #Plote dos Gráficos
    #    sg.graphic_solution(expression, symbols, points, image_z, iterations)

    return sr.SearchResult(function, points, converged, precision_decimals)

#result = modificado("(4 - 2.1*x1**2 + (x1**4)/3)*x1**2 + x1*x2 + (-4 +4*x2**2)*x2**2", 0.25, -0.8, 4)
#print(result)