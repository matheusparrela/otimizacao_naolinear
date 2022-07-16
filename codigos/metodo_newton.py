#OTIMIZAÇÃO NÃO LINEAR - MÉTODO DE NEWTON
import sympy as sy
import solucao_grafica as sg
import search_result as sr

def newton(function, x, y, precision_decimals): 
  
    sy.init_printing(use_latex='png', scale=1.05, order='grlex',forecolor='Black', backcolor='White', fontsize=10)

    points = [[x,y]]
    converged = True
    k = 0
    iterations = [k]
    
    symbols = sy.symbols("x1 x2")
    
    try:    
        expression = sy.parsing.sympy_parser.parse_expr(function)
    
    except:
        print("Erro na função")
        return 1

    grad = []
    grad.append(sy.diff(expression, symbols[0]))        #Gradiente da Função
    grad.append(sy.diff(expression, symbols[1]))

    h11 = sy.diff(grad[0], symbols[0])       #Calcula os elementos da hessiana
    h12 = sy.diff(grad[0], symbols[1])
    h21 = sy.diff(grad[1], symbols[0])
    h22 = sy.diff(grad[1], symbols[1])

    for k in range (0,5):

        a = grad[0].subs(symbols[0], x)               #Valor de X no gradiente
        a2 = a.subs(symbols[1], y)

        b = grad[1].subs(symbols[0], x)               #Valor de Y no gradiente
        b2 = b.subs(symbols[1], y)

        #Passa as condições iniciais, elementos do hesiano e o gradiente no pontos iniciais para matrizes
        P = sy.Matrix([[x], [y]])            
        H = sy.Matrix([[h11, h12], [h21, h22]])
        G = sy.Matrix([[a2], [b2]])

        try:
            H_inv = H.inv()                 #Inverte a matriz hessiana
            x0 = P - H_inv*G                #Calcula do ponto x0 

        except:
            print("Hessina não Invertivel")
            converged = False
            break

        if (x != x0[0,0] or y != x0[1,0]) and k != 0:
            print("Erro - Função não quadrática")
            converged = False
            break

        x = round(x0[0,0], precision_decimals)           #Retira os resultados da matriz
        y = round(x0[1,0], precision_decimals)

        iterations.append(k+1)
        points.append([x,y])
    
    image_z = sg.function(expression, symbols, points)

    if k >= 4:
        sg.graphic_solution(expression, symbols, points, image_z, iterations)

    return sr.SearchResult(function, points, converged, precision_decimals)

result = newton("(x1 + 2*x2 - 7)**2 + (2*x1 + x2 - 5)**2", 4, 4, 4)
print(result)